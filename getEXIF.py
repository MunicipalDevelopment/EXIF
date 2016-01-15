import exifread


f = open('p.jpg', 'rb')
tags = exifread.process_file(f)

# see all the tags available

#for t in tags:
#    print t



z = str(tags['GPS GPSLongitude'])
x = str(tags['GPS GPSLatitude'])



#Get longtitude in D.M.S

lon1=z.split("[")
lon2 = lon1[1].split(",")
lon3=lon2[0] 
lon4=lon2[1] 
lon5=lon2[2].split("/")
lon6=float(lon5[0])/100


#Get latitude in D.M.S

lat1=x.split("[")
lat2 = lat1[1].split(",")
lat3=lat2[0] 
lat4=lat2[1] 
lat5=lat2[2].split("/")
lat6=float(lat5[0])/100

latitude=(float(lat3)+(float(lat4) *1/60))+(float(lat6)*1/60*1/60)
longitude=(float(lon3)+(float(lon4) *1/60))+(float(lon6)*1/60*1/60)

print latitude
print longitude



#VERIFYING CORRECT ANSWER
#print (lat3).lstrip()
#print str(lat4).lstrip()
#print str(lat6).lstrip()
#lat3=35 lat4=4 lat6=45.69

#VERIFYING CORRECT ANSWER
#print (lon3).lstrip()
#print str(lon4).lstrip()
#print str(lon6).lstrip()
#lon3=106 lon4=38 lon6=26.13
