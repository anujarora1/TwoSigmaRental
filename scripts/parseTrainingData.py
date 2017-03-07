import json
import datetime

def getInterestLevel(x):
	return {
		'low': 1,		
		'medium': 2,
		'high': 3,
	}[x]


def getDaysOnMarket(x):
	return (datetime.datetime.today().date() - datetime.datetime.strptime(x, "%Y-%m-%d %H:%M:%S").date()).days

def getLocation(x,y):
	quad_1_long = 

myKeys = []
listingsIds = []
bedrooms = []
bathrooms = []
price = []
daysOnMarket = []
location = []
interest_level = []

with open('..\data\\train.json\\train.json') as datafile:
	allData = json.load(datafile)

listingData = allData['listing_id']
bedroomsData = allData['bedrooms']
bathroomsData = allData['bathrooms']
priceData = allData['price']
createdData = allData['created']
interestLevelData = allData['interest_level']
locationData_long = allData['longitude']
locationData_lat = ['latitude']

for key in listingData.keys():
	myKeys.append(int(key))
	listingsIds.append(int(listingData[key]))
	bedrooms.append(int(bedroomsData[key]))
	bathrooms.append(int(bathroomsData[key]))
	price.append(int(priceData[key]))
	daysOnMarket.append(getDaysOnMarket(createdData[key]))
#	location.append(getLocation(longitude[key], latitude[key]))#
	interest_level.append(getInterestLevel(interestLevelData[key].lower()))

counter = 0
totalEntries = len(myKeys)
outputFile = '..\data\\train.csv'
fid = open(outputFile, 'w')
fid.write('local_key,listingId,bedrooms,bathrooms,price,daysOnMarket,interestLevel\n')
while counter < totalEntries:
	output = "%d,%d,%d,%d,%d,%d,%d\n" % (myKeys[counter], listingsIds[counter],bedrooms[counter],bathrooms[counter],price[counter],daysOnMarket[counter],interest_level[counter])
	fid.write(output)
	counter = counter + 1

fid.close()
