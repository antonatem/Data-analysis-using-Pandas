# import urllib, json, pandas and matplotlib modules
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt
from pandas.util.testing import assert_frame_equal

#defined variable to hold input URL
json_url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

#Open url and read data
response = urllib.request.urlopen(json_url)
content = response.read()
data = json.loads(content.decode("utf8"))

# Function to calculate and return results
def data_analysis():
    #Create dataframe df to represent the data
    df = pd.DataFrame((data))
    
    #Calculate number of water points that are functional
    number_functional = df[df.water_functioning == 'yes'].water_functioning.value_counts()
    print("Number of water points that are functional,: \n",number_functional)
    print("-------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    #Calculate number of functioning water points
    functioning_water_points = df[df.water_point_condition == 'functioning'].water_point_condition.value_counts()
    print("Number of functioning water points: \n",functioning_water_points)
    print("-------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    #Calculate number of water points per community village
    number_water_points = df["communities_villages"].value_counts()
    print("Number of water points per community: \n",number_water_points)
    print("-------------------------------------------------------------------------------------------------------------")
    print("\n")
    
    #Calculate the rank for each community by the percentage of broken water points and plot graph
    gb = df.groupby(['water_point_condition'])
    community_ranking = 100 * df[df.water_point_condition == 'broken'].communities_villages.value_counts() / gb["water_point_condition"].get_group("broken").count()
    print("The rank for each community by the percentage of broken water points: \n",community_ranking)
    print("-------------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Community rank by line graph: \n")
    community_ranking.plot()

data_analysis()

df = pd.DataFrame(data)
nl = df.isnull().sum()
print(nl)
df1 = df[df.water_functioning == 'yes'].water_functioning.count()
df2 = df[df.water_functioning == 'no'].water_functioning.count()
df4 = df['water_functioning'].count()

df3 = df1 + df2
(df3 == df4).all()
