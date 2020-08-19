import glob
import pickle
import random

g = glob.glob("*.abstract")
print(len(g))
abs_list = random.sample(g,10)
for item in abs_list:
    with open(item , "rb") as f:
        l= pickle.load(f)
    print(len(l))