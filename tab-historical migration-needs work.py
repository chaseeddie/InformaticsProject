# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 17:18:18 2019

@author: Danielle
"""
import pandas as pd




mi=pd.read_excel('tab-a-1.xlsx', 
                         skiprows=4, 
                       skipfooter=12,                   
                       na_values = "(NA)",
                       header=[0,1,2],
                       index_col = 0)       






mi.dropna(how='all', inplace=True) 
mi = mi.stack().stack()       
mi= mi.reset_index()
           
mi.rename(columns={mi.columns[0]: 'Years',
                         mi.columns[1]: 'Type of residence in the United States',
                         mi.columns[2]: 'Different or Same County',
                         mi.columns[3]: 'Different or Same State',
                         mi.columns[4]: 'total',
                         }, inplace=True)                      
                       
                       
                       
                       

mi.to_excel(excel_writer='migration_clean.xlsx',           
                sheet_name='migration',                           
                 
index=False
                                
                )   
