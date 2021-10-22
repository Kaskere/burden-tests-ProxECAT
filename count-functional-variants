import os
from collections import Counter
import re


files = os.listdir("./")
for file in files:
    if file.startswith('gnomad_test.txt'):
        fn = file
        #df = pd.read_csv(fn,delimiter='\t',header=None, usecols=[0,11,12,13,14,16,17,19,22,23,24,25,26,27])
        df = pd.read_csv(fn, sep='\t', header=0, usecols=[0,11,12,13,14,16,17,19,22,23,24,25,26,27])

        print(df)

        df.drop_duplicates()
        new_file_name = fn + '_functional_v3.txt'
        df.to_csv(new_file_name, sep='\t', header=True, index=False)
