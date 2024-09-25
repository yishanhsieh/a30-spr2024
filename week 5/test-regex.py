
import re

regex = r"[aeiou]"

test_str = "dfjlsajf;alfm;sdfsddererer"

subst = "[a]"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

if result:
    print (result)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.