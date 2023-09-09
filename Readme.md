# Tools for writing Pygments Lexers

We develop a number of tools to help tracing the behaviour of RegexLexer
sub-classes during their development.

We do this by monkey patching the `RegexLexer.get_tokens_unprocessed` function.

To do this, once you have installed this python package, you need to run the
command:

```
  ./scripts/extractMonkeyPatches
```

This extracts the latest source of the `RegexLexer.get_tokens_unprocessed` and
patches it using the file `pygmentsTools/monkeyPatch.patch`.

These patches add print statements at various points in the
`get_tokens_unprocessed` function, provding a "trace" of how the RegexLexer
based lexing is progressing.

You can **install this tool globally** by typing:

```
  ./scripts/installEditablePygTracerCommands
```

**To run this tool**, type:

```
  pygTracer <LexerName> <codeToHighLight>
```

Type: 

```
  pygTracer -h
```

for help.