import numpy as np
import pandas as pd


def ordinal_encoding(df,ordinal_target):
    like = (df[ordinal_target].unique()) # finds the unique values in the ordinal_target (adjectives) from the original df as parameter
    ordinal_map = {value: idx for idx, value in enumerate(like)} # assgins them values based on their indices from unique set
    print(ordinal_map) # adjectives along with their 'linking' equivalent to numbers
    df[ordinal_target] = df[ordinal_target].map(ordinal_map) # mapping the ordinal_map values with the original values in ordinal target
    return df


def O_hotEncoding(df,target):
    # add new columns and encode them
    unique_values = df[target].unique() # finds the unique values in the ordinal_target (adjectives) from the original df as parameter
    print(unique_values) # unique values so that repetitions are ignored
    for value in unique_values: # extracting values and assigning them with 1 or 0
        df[f"{value}"] = np.where(df[target] == value, 1, 0) # if the target column name equals the values then a new column is made with values 1(if same) otherwise 0
    df=df.drop(target,axis=1) # drop the column target
    return df




data = {
    'shows':['Ryukendo','Power Rangers Jungle Fury','Power Puff Girls','Motu Patlu','Chotta Bheem','Mr. Bean','Squid Game','Rescue Force','Digimon','Ultra Man'],
    'likeness': ['Most Favourite','Favourite','Good','Average','Hate','Good','Favourite','Favourite','Most Favourite','Most Favourite']
}


print('Orginial Data Frame\n')
df = pd.DataFrame(data)
print(df)
print('After Ordinal Encoding')
ordinal_encoding(df,'likeness')
print(df)

print('After O hot encoding')
df=O_hotEncoding(df,'shows')
print(df)