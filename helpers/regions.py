import pandas as pd
from cached_data import store

df = pd.read_csv('specimenDate_ageDemographic-unstacked.csv', low_memory=False)

def region_list():
    target_key = "all_regions"
    
    if target_key in store:
        return store[target_key]
    else:
        all_regions = df.areaName.unique().tolist()
        store[target_key] = all_regions
        return all_regions