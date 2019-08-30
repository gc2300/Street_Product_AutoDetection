##
# This module is the interface with the humans. It takes in the Active Retail Tobacco Vendors CSV,
# filters for locations in NYC, and runs those locations through the Google Street View extraction pipeline.
##

from gsv_extractor import *
 
while True:
    message = input(">> ")
    if message == "stop":
        break
    else:
        bodega_sheet = pd.read_csv('Active_Retail_Tobacco_Vendors.csv')
        NYC_bodega_sheet = bodega_sheet.loc[bodega_sheet['COUNTY'] == 'NEW YORK CITY'].reset_index()
        for i in range(len(NYC_bodega_sheet)):
            GetStreet(NYC_bodega_sheet['LOCATION'][i+1].split('\n')[2].strip('()'), '0', myloc)
            GetStreet(NYC_bodega_sheet['LOCATION'][i+1].split('\n')[2].strip('()'), '90', myloc)
            GetStreet(NYC_bodega_sheet['LOCATION'][i+1].split('\n')[2].strip('()'), '180', myloc)
            GetStreet(NYC_bodega_sheet['LOCATION'][i+1].split('\n')[2].strip('()'), '270', myloc)