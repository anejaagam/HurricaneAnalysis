# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

#Function to take values of damage list and turn them into floats instead of having M or B. 
damagesFloated= []
def damagesToFloat(damages): 
    
    for i in damages:
        if i == 'Damages not recorded':
            damagesFloated.append(i)
        elif i[-1]=='B':
            i= float(i.replace('B',''))*(10**9) #if the value had a B it would take the B out and times the value by 1,000,000,000
            damagesFloated.append(i)
        elif i[-1]=='M':
            i = float(i.replace('M',''))*(10**7) #if the value had an M it would take the B out and times the value by 1,000,000
            damagesFloated.append(i)
    return damagesFloated


# Function to construct a dictionary of Hurricanes sorted by name. Each Key in dictionary will give you another dictionary with the values for
# name, Month, Year, Max Wind, Damage, Areas Affected, and deaths of the hurricane
HurricaneInfo={}
def HurricaneDictConst(name, month, year, max_wind,area,damage,death):
    for i in range(len(name)):

        HurricaneInfo.update({
            name[i]: {
                "Name" : name[i],
                "Month": month[i],
                "Year": year[i],
                "Max Sustained Wind": max_wind[i],
                "Areas Affected": area[i],
                "Damage": damage[i],
                "Deaths": death[i]
            }
        })
    return HurricaneInfo

#Run the function, therefore we can now use the dictionary throughout the program
HurricaneDictConst(names,months,years,max_sustained_winds,areas_affected,damagesToFloat(damages),deaths) 

# Function to construct a dictionary, sorted by the Year it happend. Some Years have more than one Hurricane.
HurricaneInfoYear ={}
def HurricaneDictConstYear(name, month, year, max_wind,area,damage,death):
    for i in range(len(year)):
        hurricaneNum=1
        if year[i] == year[i-1]:
            hurricaneNum += 1
            year[i] = str(year[i]) + " Hurricane #{}".format(hurricaneNum)
        else:
            hurricaneNum = 1
        
        HurricaneInfoYear.update({
                year[i]:{
                    "Name" : name[i],
                    "Month": month[i],
                    "Year": year[i],
                    "Max Sustained Wind": max_wind[i],
                    "Areas Affected": area[i],
                    "Damage": damage[i],
                    "Deaths": death[i]
                }
            })
    return HurricaneInfoYear

#Optional, wont be used throughout the program
HurricaneDictConstYear(names,months,years,max_sustained_winds,areas_affected,damages,deaths)


# Function to sort areas affected by the times they were affected
affectedAreasCounted={}
def countAffectAreas(HurricaneInfo):
    
    areasAffected = []
    for i,j in HurricaneInfo.items():
        areasAffected.append(j["Areas Affected"])
    

    for i in areasAffected:
       for j in i:
            try:
                affectedAreasCounted[j] += 1
            except KeyError:
                affectedAreasCounted[j] = 1
    return affectedAreasCounted

#Run the function to now have the affected areas in a dictionary and the amount of times it was affected as values
countAffectAreas(HurricaneInfo)


# Function to find the areas most hit by hurricanes
mostAffectedArea = []
def mostAffected(affected):
    affectedV = 0
    affectedK = "Nothing"

    for i,j in affected.items():
        if j > affectedV:
            affectedV = j
            affectedK = i
        else:
            continue
    mostAffectedArea = [affectedK,affectedV]
    return mostAffectedArea

#This would print out in [Most Affected Area, Number of times it was affected]
mostAffected(affectedAreasCounted)    

# Function to find the hurricane with the most deaths
mostDeaths=[]
def mostDeathsFunc(HurricaneInfo):
    DeathV = 0
    DeathK = "Nothing"

    for i,j in HurricaneInfo.items():
        if j["Deaths"] > DeathV:
            DeathV = j["Deaths"]
            DeathK = i
        else:
            continue
    mostDeaths = [DeathK,DeathV]
    return mostDeaths

#This would print out as [Name, Number of deaths] 
mostDeathsFunc(HurricaneInfo)


# Function to Categorize the Huricanes by Mortality rate, scale shown below
#mortality_scale = {0: 0, 1: 100, 2: 500, 3: 1000,4: 10000}
HurricaneCategoryDeath = {0 : [],1: [],2: [],3:[],4:[],5:[]}
def categorizeByMortatility(HurricaneInfo):
    for i,j in HurricaneInfo.items():
        if (j["Deaths"] > 0 ) and (j["Deaths"] <= 100):
            HurricaneCategoryDeath[1].append(i)
        elif (j["Deaths"] > 100 ) and (j["Deaths"] <= 500):
            HurricaneCategoryDeath[2].append(i)
        elif (j["Deaths"] > 500 ) and (j["Deaths"]<= 1000):
            HurricaneCategoryDeath[3].append(i)
        elif j["Deaths"] > 1000 and (j["Deaths"] <= 10000):
            HurricaneCategoryDeath[4].append(i)
        else:
            HurricaneCategoryDeath[5].append(i)
    return HurricaneCategoryDeath

#This would print out the list of the hurricanes categorized by mortality rate
categorizeByMortatility(HurricaneInfo)


# Function to find the most damaging hurricane
mostDamage=[]
def mostDamageFunc(HurricaneInfo):
    DamageV = 0
    DamageK = "Nothing"

    for i,j in HurricaneInfo.items():
        if j["Damage"] == 'Damages not recorded':
            continue
        elif j["Damage"] > DamageV:
            DamageV = j["Damage"]
            DamageK = i
        else:
            continue
    mostDeaths = [DamageK,DamageV]
    return mostDeaths

#This would print as [Name, Amount of Damage done ($)]
mostDamageFunc(HurricaneInfo)

# Function to Categorize the Huricanes by Damage, scale shown below, all values in $
#damage_scale = {0: 0, 1: 100000000,2: 1000000000,3: 10000000000,4: 50000000000}
HurricaneCategoryDamage = {0:[],1:[],2:[],3:[],4:[],5:[]}
def categorizeByDamage(HurricaneInfo):
    for i,j in HurricaneInfo.items():
        if (j["Damage"]) == 'Damages not recorded':
            HurricaneCategoryDamage[0].append(i)
        if (j["Damage"] > 0 ) and (j["Damage"] <= 100000000):
            HurricaneCategoryDamage[1].append(i)
        elif (j["Damage"] > 100000000 ) and (j["Damage"] <= 1000000000):
            HurricaneCategoryDamage[2].append(i)
        elif (j["Damage"] > 1000000000 ) and (j["Damage"]<= 10000000000):
            HurricaneCategoryDamage[3].append(i)
        elif j["Damage"] > 10000000000 and (j["Damage"] <= 50000000000):
            HurricaneCategoryDamage[4].append(i)
        else:
            HurricaneCategoryDamage[5].append(i)
    return HurricaneCategoryDamage

#This would print out the list of hurricanes categorized by Damage Scale
categorizeByDamage(HurricaneInfo)