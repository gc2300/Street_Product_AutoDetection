#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
import os
import pandas as pd

# size of 480 x 640 comes from the previous project
base = "https://maps.googleapis.com/maps/api/streetview?size=480x640&location="

# -- define API key
api_key = 'XXXXXXXXXXXXXXXXX'
key = "&key=" + api_key
    
# -- define storage location
myloc = r"xxx_xxx"

# following function borrowed from Andrew Wheeler and updated for Python 3
# by providing a location and local folder pathname, get latest Google Street View images for that location(s)
# location can be either a text string (such as Chagrin Falls, OH) or a lat/lng value (40.457375,-80.009353)

def extract_gsv(Add, Heading, SaveLoc):
    """
    Extract images from Google Street View for a list of locations. 
    """
    
    # -- define API key
    api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    
    # -- define API call
    MyUrl = base + urllib.parse.quote(Add) + "&heading=" + Heading + "&fov=90" + key
    
    # -- retrieve image from GSV
    fi = Add + " - " + Heading + ".jpg"
    urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))
    
if __name__ == "__main__":
    
    # -- read in Active Retail Tobacco Vendors for Brooklyn, NY through SODA API
    df = pd.read_json('https://health.data.ny.gov/resource/35pn-9h5i.json')
    df_bk = df[df['municipality'] == "BROOKLYN"].reset_index().dropna()
    
    # -- save images to folder
    for i in range(len(df_bk['location'])):
        for j in range(4):
            heading = str(j*90)
            extract_gsv(Add=str(df_bk['location'][i+1]['coordinates'][::-1]).strip('[]'), Heading=heading, SaveLoc=myloc)