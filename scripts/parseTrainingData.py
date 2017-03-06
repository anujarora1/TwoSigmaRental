import json

def getInterestLevel(x):
	return {
		'low': 1,		
		'medium': 2,
		'high': 3,
	}[x]

myKeys = []
listingsIds = []
bedrooms = []
bathrooms = []
price = []
interest_level = []

with open('..\data\\train.json\\train.json') as datafile:
	allData = json.load(datafile)

listingData = allData['listing_id']
bedroomsData = allData['bedrooms']
bathroomsData = allData['bathrooms']
priceData = allData['price']
interestLevelData = allData['interest_level']

for key in listingData.keys():
	myKeys.append(int(key))
	listingsIds.append(int(listingData[key]))
	bedrooms.append(int(bedroomsData[key]))
	bathrooms.append(int(bathroomsData[key]))
	price.append(int(priceData[key]))
	interest_level.append(getInterestLevel(interestLevelData[key].lower()))

counter = 0
totalEntries = len(myKeys)
outputFile = '..\data\\train.csv'
fid = open(outputFile, 'w')
fid.write('local_key,listingId,bedrooms,bathrooms,price,interestLevel\n')
while counter < totalEntries:
	output = "%d,%d,%d,%d,%d,%d\n" % (myKeys[counter], listingsIds[counter],bedrooms[counter],bathrooms[counter],price[counter],interest_level[counter])
	fid.write(output)
	counter = counter + 1

fid.close()
