# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:48:58 2019

@author: Danielle
"""

#Crime Trends in on var

import pandas as pd




crime=pd.read_excel('CrimeTrendsInOneVar.xlsx', 
                           skiprows=4, 
                                       
                       skipfooter=15,                   
                       na_values= "null",
                      usecols=1,
                       header=[0],
                       index_col = 0)       



crime.dropna(how='all', inplace=True) 

crime= crime.reset_index()
           

crime.to_excel(excel_writer='crime_clean.xlsx',           
                sheet_name='crime',                            
                 
index=False
                                
                )   
