import pandas as pd
import csv


data_info = []
for page in range(1,3):
    #Url of Website you want to Scrape
    page_url = "http://integrity.ng/index.php/units/browse/{}".format(page)
    
    #Append each page data in an array
    data_info.append(pd.read_html(page_url)[0])


dataf = pd.concat(data_info)

export_csv = dataf.to_csv(r'C:\Users\X\Desktop\export_dataframe.csv', index = None, header=True)