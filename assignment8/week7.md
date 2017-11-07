# Week 7: Regular Expressions

1) `\d+(\.\d+)?` matches a string beginning with at least one number that can be followed by a random character and a group of more numbers.

2) `\b(\w\w)\b` matches two characters between two boundary characters

3) 'the small' and 'big raven'

4) `\b(\d{2})*\b`

5) 
```
gontrum@numerus$ grep "n.o" chaplin.txt
Tango Tangles
Gentlemen of Nerve
A Woman of Paris
```

6) whitespace or 'g'

7) 
```
gontrum@numerus$ grep "[A-Z].$" chaplin.txt
One A.M.
```

8) 
```
gontrum@numerus$ grep -E "[a-Z]+h\>" chaplin.txt
Dough and Dynamite
The Gold Rush
```

9) `<_sre.SRE_Match object; span=(4, 7), match='two'>`

10) `two`

