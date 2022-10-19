from dataclasses import dataclass
import pandas as pd

a = pd.DataFrame({"amimals":["dog","cat","lion","cow","elephant"],"sound":["barks","meow","roars","moo","trumpet"]})

print(a)
print(a.describe())

b = pd.DataFrame({"letters":["a","b","c","d","e","f"],
        "numbers":[12,7,9,3,5,1]})

print(b.sort_values(by="numbers"))

b=b.assign(new_values=b["numbers"]*3)
print(b)
