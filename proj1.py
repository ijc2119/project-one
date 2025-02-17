import pandas as pd
import numpy as np

#get headers for communities and crime dataset
headers = pd.read_fwf('comm_crime_headers.txt')
headers.to_csv('comm_crime_headers.csv')
headers = pd.read_csv("comm_crime_headers.csv",sep=',',engine='python', names = ['attribute', 'ID'])

headers['ID'] = [row.split(' ')[0] for row in headers['ID']]
headers = headers.drop(['attribute'], axis=1)
print(headers.head())


#import communities and crime dataset and add headers
df = pd.read_fwf('CommViolPredUnnormalizedData.txt')
df.to_csv('comm_crime.csv')
df = pd.read_csv('comm_crime.csv',sep='\s*,\s*',engine='python',na_values=['?'])
df = df.drop(df.columns[0], axis=1)
df.columns = headers['ID']


# data cleaning
# replacing ?" with NaN in nonViolPerPop col
df['nonViolPerPop'] = df['nonViolPerPop'].replace('?"', np.nan)

#remove " from communityName and nonViolPerPop cols
df['communityname'] = df['communityname'].str.replace('"', '')
df['nonViolPerPop'] = df['nonViolPerPop'].str.replace('"', '')


# separate community type from community name
df['communityname'] = df['communityname'].str.replace('city', ' city')
df['communityname'] = df['communityname'].str.replace('town', ' town') #for town and township
df['communityname'] = df['communityname'].str.replace('village', ' village')
df['communityname'] = df['communityname'].str.replace('borough', ' borough')


df["communityName"] = np.vectorize(lambda x : x.split(" ")[0])(np.array(df["communityname"],dtype=str))
df.loc[df['communityName'] =='nan'] = np.nan


#add space before capital letters in communityName
df['communityName'] = df['communityName'].replace(to_replace="(\w)([A-Z])", value=r"\1 \2", regex=True)
print(df.tail())

#reorder columns to have communityName at start and remove communityname
cols = df.columns.tolist()
cols = cols[-1:] + cols[:-1]
df = df[cols]

df['communityname'] = df['communityname'].str.split().str[1:].str.join(' ')
df = df.rename(columns={'communityname':'communityType'})
print(df.head())

#change column types
df = df.astype({'nonViolPerPop':'float'})
print(df.dtypes.value_counts())


#drop duplicates
initial_shape = df.shape
df = df.drop_duplicates()
print(f"Removed {initial_shape[0] - df.shape[0]} duplicate rows. New shape: {df.shape}")


#prepare cities csv
cities = pd.read_csv('uscities.csv')
#drop extra columns
cities = cities.drop(['city_ascii', 'county_fips','source','timezone','ranking','timezone','zips','id'], axis=1)
print(cities.head())
print(cities.dtypes)



### prepare top 22 states dataframe
h = ['violPerThousand', 'propertyPerThousand','','burglaryPerThousand', 'percentViolReported', 'percentPropReported']
files = ['cv22luss1719/cv22luss1719f01.csv', 'cv22luss1719/cv22luss1719f02.csv', 'cv22luss1719/cv22luss1719f03.csv', 'cv22luss1719/cv22luss1719f04.csv', 'cv22luss1719/cv22luss1719f05.csv']

df2 = pd.DataFrame()
for f in files:
    d = pd.read_csv(f, encoding='cp1252')
    df2 = pd.concat([df2,d], axis=1)

#remove excess rows
df2 = df2.iloc[12:33]


#remove excess columns
df2.columns.values[0] = ""
df2 = df2.drop(['Unnamed: 1','Bureau of Justice Statistics'], axis=1)


#rename columns
h = ['ViolPerThousand', 'PropertyPerThousand','ViolPerThousandExcludingAssault','BurglaryPerThousand', 'PercentViolReported', 'PercentPropReported']
for i in range(5):
    df2.columns.values[4*i+1] = 'rate' + h[i]
    df2.columns.values[4*i+2] = 'sig' + h[i]
    df2.columns.values[4*i+3] = 'LB' + h[i]
    df2.columns.values[4*i+4] = 'UB' + h[i]
df2 = df2.drop(['UBPercentViolReported', 'Unnamed: 7'], axis=1)
df2 = df2.rename(columns={'Unnamed: 6':'UBPercentViolReported'})

# Add column for if significant compared to US national value
for i in range(5):
    orig = 'sig' + h[i]
    name= '90%CIsig' + h[i]
    name2 = '95%CIsig' + h[i]

    df2[name] = ((df2[orig] =='‡') | (df2[orig] == '†'))
    df2[name2] = (df2[orig] == '†')

#change types of df2
df2 = df2.astype({'':'str','rateViolPerThousand':'float', 'LBViolPerThousand':'float', 'UBViolPerThousand':'float',
                  'ratePropertyPerThousand':'float','LBPropertyPerThousand':'float','UBPropertyPerThousand':'float',
                  'rateViolPerThousandExcludingAssault':'float','LBViolPerThousandExcludingAssault':'float','UBViolPerThousandExcludingAssault':'float',
                  'rateBurglaryPerThousand':'float','LBBurglaryPerThousand':'float','UBBurglaryPerThousand':'float',
                  'ratePercentViolReported':'float','LBPercentViolReported':'float', 'UBPercentViolReported':'float'})

#reorder columns and remove excess columns, add State to name
df2 = df2[['', 'rateViolPerThousand', '90%CIsigViolPerThousand', '95%CIsigViolPerThousand',
       'LBViolPerThousand', 'UBViolPerThousand', 'ratePropertyPerThousand',
       '90%CIsigPropertyPerThousand', '95%CIsigPropertyPerThousand', 'LBPropertyPerThousand',
       'UBPropertyPerThousand', 'rateViolPerThousandExcludingAssault',
       '90%CIsigViolPerThousandExcludingAssault',
       '95%CIsigViolPerThousandExcludingAssault',
       'LBViolPerThousandExcludingAssault',
       'UBViolPerThousandExcludingAssault', 'rateBurglaryPerThousand',
        '90%CIsigBurglaryPerThousand', '95%CIsigBurglaryPerThousand','LBBurglaryPerThousand',
       'UBBurglaryPerThousand', 'ratePercentViolReported',
       '90%CIsigPercentViolReported', '95%CIsigPercentViolReported', 'LBPercentViolReported', 'UBPercentViolReported',]]
df2=df2.add_prefix("state")
print(df2.dtypes.value_counts())
print(df2.columns)

print(cities.columns)
# merge cities and communities+crime
merge1 = pd.merge(df, cities, how= 'left', left_on=['communityName','State'], right_on=['city', 'state_id'])
print(merge1.head())

final = pd.merge(merge1,df2, how = 'left', left_on = 'state_name', right_on = 'state')
print(final.head())

final = final.drop(['state', 'city', 'state_name', 'state_id'], axis=1) # removing redundant state column
final.to_csv('final_data.csv')


#number missing
print(final.isna().sum())


# Data Sources
# https://archive.ics.uci.edu/dataset/211/communities+and+crime+unnormalized
# https://bjs.ojp.gov/library/publications/criminal-victimization-22-largest-us-states-2017-2019
# https://simplemaps.com/data/us-cities


# References
# https://stackoverflow.com/a/53527413
# https://stackoverflow.com/a/62711050
# https://stackoverflow.com/questions/56479689/how-do-i-insert-space-before-capital-letter-if-and-only-if-previous-letter-is-no
# https://stackoverflow.com/a/13148611
# https://www.w3schools.com/python/pandas/ref_df_add_prefix.asp#:~:text=The%20add_prefix()%20method%20inserts,use%20the%20add_suffix()%20method.