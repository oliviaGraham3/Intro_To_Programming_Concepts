ohYeah = 0

allRain = []
allWind = []
allRates = []

avgRain = 0
avgWind = 0
avgRate = 0

while ohYeah != "-1":
    rain, wind = input("Enter average rain and average wind separated by a space: ").split()
    float(rain.strip())
    float(wind.strip())
    allRain.append(rain)
    allWind.append(wind)
    weatherSev = rain * 10 + wind
    allRates.append(int(weatherSev))

    ohYeah = input("Enter average rain and average wind separated by a space: ")

for x in range(len(allWind) - 1):
    avgWind = avgWind + float(allWind[x])
avgWind = round(avgWind / len(allWind), 2)

for x in range(len(allRates) - 1):
    avgRate = avgRate + float(allRates[x])
avgRate = round(avgRate / len(allRates), 2)

for x in range(len(allRain) - 1):
    avgRain = avgRain + float(allRain[x])
avgRain = round(avgRain / len(allRain), 2)

print("The average rain is ", avgRain, " inches.")
print("The average wind is ", avgWind, " mph.")
print("The average severity for these ", len(allRain), " is ", avgRate)