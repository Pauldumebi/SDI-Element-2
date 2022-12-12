import pandas as pd
from utils.monthsDict import monthsDict
from cache.store import store

df = pd.read_csv('data/specimenDate_ageDemographic-unstacked.csv', low_memory=False)

def regionList():
    target_key = "allRegions"
    
    if target_key in store:
        return store[target_key]
    else:
        allRegions = df.areaName.unique().tolist()
        store[target_key] = allRegions
        return allRegions

def monthList():
    target_key = "isCovidListMonths"
    
    if target_key in store:
        return store[target_key]
    else:
        isCovidListMonths = df.date.str[5:7].unique().tolist() #get all unique values from date column for months in the csv file
        isCovidListMonths.sort(key = int) #cast to integer
        isCovidListMonths = [ i.lstrip('0') for i in isCovidListMonths ] #remove leading zeros
        isCovidListMonths = [k for k, v in monthsDict().items() if v in isCovidListMonths] #swap number for full month value
        store[target_key] = isCovidListMonths #keep in store cache
        return isCovidListMonths

def yearList():
    target_key = "isCovidListYears"
    
    if target_key in store:
        return store[target_key]
    else:
        isCovidListYears = df.date.str[:4].unique().tolist()
        store[target_key] = isCovidListYears
        return isCovidListYears

def dayList():
    target_key = "isCovidListDays"
    
    if target_key in store:
        return store[target_key]
    else:
        isCovidListDays =  df.date.str[-2:].unique().tolist()
        isCovidListDays = [ i.lstrip('0') for i in isCovidListDays ]
        isCovidListDays.sort(key = int)
        store[target_key] = isCovidListDays
        return isCovidListDays
