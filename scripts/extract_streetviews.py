import urllib
import os

# replace with your own Google Street View API
api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

# local storage for extracted images
# replace with your own location
myloc = r"xxxxxxxxxxxxxxxxxxx"
key = "&key=" + api_key

# size of 480 x 640 comes from the previous project
base = "https://maps.googleapis.com/maps/api/streetview?size=480x640&location="

# following function borrowed from Andrew Wheeler and updated for Python 3
# by providing a location and local folder pathname, get latest Google Street View images for that location(s)
# location can be either a text string (such as Chagrin Falls, OH) or a lat/lng value (40.457375,-80.009353)

def GetStreet(Add, Heading, SaveLoc):
  # fov controls zoom: ~60 degrees requires 6 images per location (60 degrees of separation between each) 
  MyUrl = base + urllib.parse.quote(Add) + "&heading=" + Heading + "&fov=90" + key #added url encoding
  fi = Add + Heading + ".jpg"
  urllib.request.urlretrieve(MyUrl, os.path.join(SaveLoc,fi))

# if output required is four images (one for each cardinal direction), use:
def GetCardinal(Add, SaveLoc):
    for i in range(4):
        heading = str(i*90)
        GetStreet(Add, Heading=heading, SaveLoc=myloc)