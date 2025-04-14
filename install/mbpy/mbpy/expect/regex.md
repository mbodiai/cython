

# Regular Expression Basics
Character Classes and Brackets
[...] - Character class: matches any single character inside the brackets
[aeiou] matches any vowel
[0-9] matches any digit
[A-Za-z] matches any letter (upper or lowercase)
Negation in Character Classes
[^...] - Negated character class: matches any character NOT inside the brackets
[^0-9] matches any non-digit
[^\t] matches anything except a tab character
Quantifiers
? - 0 or 1 occurrence
* - 0 or more occurrences
+ - 1 or more occurrences
{n} - Exactly n occurrences
{n,} - At least n occurrences
{n,m} - Between n and m occurrences
Anchors
^ - Line start
$ - Line end
\b - Word boundary
\B - Not word boundary
Special Character Sequences
\s - Any whitespace character
\S - Any non-whitespace character
\d - Any digit (same as [0-9])
\D - Any non-digit
\w - Any word character (alphanumeric plus underscore)
\W - Any non-word character
