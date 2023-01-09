import pandas as pd
from utils.monthList import monthsDict
from cache.store import store

df = pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

def regionList():
    targetKey = "allRegions"
    
    if targetKey in store:
        return store[targetKey]
    else:
        allRegions = df.areaName.unique().tolist()
        store[targetKey] = allRegions
        return allRegions

def monthList():
    targetKey = "isCovidListMonths"
    
    if targetKey in store:
        return store[targetKey]
    else:
        isCovidListMonths = df.date.str[5:7].unique().tolist() #get all unique values from date column for months in the csv file
        isCovidListMonths.sort(key = int) #cast to integer
        isCovidListMonths = [ i.lstrip('0') for i in isCovidListMonths ] #remove leading zeros
        isCovidListMonths = [k for k, v in monthsDict().items() if v in isCovidListMonths] #swap number for full month value
        store[targetKey] = isCovidListMonths #keep in store cache
        return isCovidListMonths

def yearList():
    targetKey = "isCovidListYears"
    
    if targetKey in store:
        return store[targetKey]
    else:
        isCovidListYears = df.date.str[:4].unique().tolist()
        store[targetKey] = isCovidListYears
        return isCovidListYears

def dayList():
    targetKey = "isCovidListDays"
    
    if targetKey in store:
        return store[targetKey]
    else:
        isCovidListDays =  df.date.str[-2:].unique().tolist()
        isCovidListDays = [ i.lstrip('0') for i in isCovidListDays ]
        isCovidListDays.sort(key = int)
        store[targetKey] = isCovidListDays
        return isCovidListDays
