from posixpath import split
import pandas as pd
import itertools
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
print('File loaded')

df = pd.read_csv(file_path)
elementname = df['Element Name'] #you can also use df['column_name']
originaltext = df['Original Text']

fwlist = []
for i in elementname:
    fwlist.append(i)

new_fwlist = [i.split(':', 2)[1] for i in fwlist]

rulelist = []
for i in originaltext:
    rulelist.append(i)

final = [i+'] '+j for i,j in (zip(new_fwlist,rulelist))]
#print(final)

for i in final:
    with open('clean_testbook.txt','a') as file:
        file.write(i+'\n')


