# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter
import re

big_str = 'This module provides regular expression matching operations similar to those found in Perl. ' \
    'Both patterns and strings to be searched can be Unicode strings (str) as well as 8-bit strings (bytes). ' \
    'However, Unicode strings and 8-bit strings cannot be mixed: that is, ' \
    'you cannot match a Unicode string with a byte pattern or vice-versa; ' \
    'similarly, when asking for a substitution, the replacement string must be ' \
    'of the same type as both the pattern and the search string. ' \
    'Regular expressions use the backslash character to indicate special forms or to allow special ' \
    'characters to be used without invoking their special meaning. This collides with Python usage of the same character ' \
    'for the same purpose in string literals; for example, to match a literal backslash, one might have to write as the pattern string, ' \
    'because the regular expression must be, and each backslash must be expressed as inside a regular Python string literal.' \
             

cnt = Counter(x for x in re.findall(r'[A-z\']{2,}', big_str))
print(cnt.most_common(10))

