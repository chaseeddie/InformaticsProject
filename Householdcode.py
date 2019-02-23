#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd


sr = 3
head = [0, 1, 2]
sf = 1
ic = 0
na = 'null'

data = pd.read_excel('Household income.xls',
                       skiprows=sr,
                       header=head,
                       na_values=na,
                       skipfooter=sf,
                       index_col=ic
                       )

data.dropna(how='all', inplace=True)
data = data.stack(head)
data = data.reset_index()
data.rename(columns={data.columns[0]: 'State',
                     data.columns[1]: 'Currency',
                     data.columns[2]: 'Year',
                     data.columns[3]: 'Median Income/Standard Error',
                     data.columns[4]: 'USD$'},
            inplace=True)
for i, row in data.iterrows():
    data.at[i, 'Year'] = str(data.at[i, 'Year']).split('(')[0]
    
    
new_csv_name = str(input("Enter a name for the new CSV (Include .csv): "))
print('CSV NAME: '+new_csv_name)
data.to_csv(new_csv_name, index=False)  #Creates the CSV
print('Created the CSV successfully.')