start = input()
rainList = []
windList = []
avgRain = 0
avgWind = 0

#Collects the data
while start != "-1":
    rain, wind = start.split()
    rain = float(rain)
    wind = float(wind)
    rainList.append(rain)
    windList.append(wind)
    start = input()

#Calculates the averages
for i in range(len(rainList)):
    avgRain += rainList[i]
avgRain /= len(rainList)

for i in range(len(windList)):
    avgWind += windList[i]
avgWind /= len(windList)

weatherSev = avgRain * 10 + avgWind
numDays = len(rainList)

print("The average rain is ", round(avgRain, 2), "inches")
print("The average wind is ", avgWind, "mph")
print("The weather severity for these ", numDays, "readings is: ", weatherSev)