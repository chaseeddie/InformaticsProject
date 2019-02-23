import pandas as pd

mi=pd.read_excel('tab-a-1.xlsx', 
                         skiprows=6, 
                       skipfooter=12,                   
                       na_values = "",
                       header=[0],
                       index_col = [0,1,2,3,4,5,6,7,8])       



mi.dropna(how='all', inplace=True) 
mi = mi.stack().reset_index()
           
mi.rename(columns={mi.columns[0]: 'Mobility Period',
                   mi.columns[1]: 'Total, 1 year old and over',
                   mi.columns[2]: 'Same residence',
                   mi.columns[3]: 'Total movers',
                   mi.columns[4]: 'Different residence total',
                   mi.columns[5]: 'Different residence same county',
                   mi.columns[6]: 'Different county total',
                   mi.columns[7]: 'Different county same state',
                   mi.columns[8]: 'Different county different state',
                   mi.columns[9]: 'Drop5',
                   mi.columns[10]: 'Movers from abroad'
                   }, inplace=True)
mi = mi.drop('Drop5', 1)                                      
mi = mi.round(decimals=1)
mi.to_excel(excel_writer='migration_clean.xlsx',           
                sheet_name='migration',                                     
index=False
                )
