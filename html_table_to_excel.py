import csv
import numpy as np
import pandas as pd

file_name = input('Please ener txt file name: ')
excel_name = input('Please enter desired excel file name: ')
fileref = open(f"{file_name}.txt", encoding='UTF-8')
textfile = fileref.read()
lines = textfile.split('\n')
line_lst=[]
for line in lines:
    line_lst.append(line.split('\t'))
header=line_lst[0]
data = np.array(line_lst[1:-1])
data_df=pd.DataFrame(data, columns=header)
data_df.to_excel(f'{excel_name}.xlsx', index=False)