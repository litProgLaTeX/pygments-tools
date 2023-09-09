
import os
import sys

from pygmentsTools.monkeyPatches import MonkeyPatchesMixin
import pygments.lexers.markup

# do the monkey patch!
pygments.lexers.markup.RegexLexer.get_tokens_unprocessed = \
  MonkeyPatchesMixin.get_tokens_unprocessed
# finished the monkey patch!

from pygments.lexers import get_lexer_by_name, \
  load_lexer_from_file

def usage() :
  print("""
  usage: pygTracer <<RegexLexerSubClass>> <<codeToHighlight>>

  arguments:

    RegexLexerSubClass  a subclass of the Pygments RegexLexer whose lexing is to
                        be traced. This can either be an alias for a builtin
                        Pygments lexer, or a path, relative to the current
                        directory, to a lexer to be loaded. If a relative path
                        is used, you can append the path with the class name of
                        the lexer, separated from the relative path by a colon
                        ':'.

    codeToHighLigth     some appropriate code to be highlighted using the given
                        lexer.
  
  options:
    -h, --help          This help text
""")
  sys.exit(1)

def cli() :
  if len(sys.argv) < 3 :
    usage()

  lexerName    = sys.argv[1]
  codeFilePath = sys.argv[2]

  theLexer = None
  if -1 < lexerName.find(':') :
    # we have a relative path and a className
    lexerPath, lexerName = lexerName.split(':')
    try : 
      theLexer = load_lexer_from_file(lexerPath, lexername=lexerName)
    except Exception as err :
      print(repr(err))
  else :
    # we might have a lexer alias
    try :
      print("Trying to load lexer using an alias")
      theLexer = get_lexer_by_name(lexerName)
    except err1 :
      print(repr(err1))
      try :
        print("Trying to load lexer from a file")
        theLexer = load_lexer_from_file(lexerName)
      except err2 :
        print(repr(err2))
  
  if not theLexer :
    print("We could not load any lexers!")
    sys.exit(1)

  codeStr = None
  try : 
    with open(codeFilePath) as codeFile :
      codeStr = codeFile.read()
  except Exception as err :
    print(repr(err))

  if not codeStr :
    print("We could not load the code file")
    sys.exit(1)

  # do the monkey patch!!!
  #theLexer.get_tokens_unprocessed = \
  #  RegexLexerTracingMixin.get_tokens_unprocessed

  os.system("reset")

  print( "pygTracer")
  print(f"     on: {codeFilePath}")
  print(f"  using: {lexerName}")
  print("")
  print("--------------------------------------------------------------")
  print(codeStr)
  print("--------------------------------------------------------------")
  print("")

  for (pos, action, aMatch) in theLexer.get_tokens_unprocessed(codeStr) :
    print("\n------------------------------")
    print("got token tuple:")
    print(f"   pos: {pos}")
    print(f"action: {action}")
    print(f" match: [{aMatch}]")
    print("------------------------------")