#Code is obtained from
#https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort

import re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)
