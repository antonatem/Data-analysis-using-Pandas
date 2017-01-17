# import urllib, json, pandas and matplotlib modules
import urllib.request
import json
import pandas as pd
import matplotlib.pyplot as plt

#defined variable to hold input URL
json_url = "https://raw.githubusercontent.com/onaio/ona-tech/master/data/water_points.json"

#Open url and read data
response = urllib.request.urlopen(json_url)
content = response.read()
data = json.loads(content.decode("utf8"))

# Function to calculate and return results
class data_analysis():
    #Create dataframe df to represent the data
    df = pd.DataFrame(data)
#     print(df)
    
    #Calculate number of water points that are functional
    def num_functional():
        df = pd.DataFrame(data)
        number_functional = df[df.water_functioning == 'yes'].water_functioning.count()
        print("Number of water points that are functional:",number_functional)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
    
    #def num_functioning():
    #Calculate number of functioning water points
    #functioning_water_points = df[df.water_point_condition == 'functioning'].water_point_condition.value_counts()
    #print("Number of functioning water points: \n",functioning_water_points)
    #print("-------------------------------------------------------------------------------------------------------------")
    #print("\n")
    
    #Calculate number of water points per community village
    def num_waterpoints():
        df = pd.DataFrame(data)
        number_water_points = df["communities_villages"].value_counts()
        print("Number of water points per community:\n",number_water_points)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
    
    #Calculate the rank for each community by the percentage of broken water points and plot graph
    def community_ranking():
        df = pd.DataFrame(data)
        gb = df.groupby(['water_point_condition'])
        community_ranking = 100 * df[df.water_point_condition == 'broken'].communities_villages.value_counts() / gb["water_point_condition"].get_group("broken").count()
        print("The rank for each community by the percentage of broken water points:\n",community_ranking)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
        
        get_ipython().magic('matplotlib inline')
        print("Community rank by line graph:\n")
        community_ranking.plot()

data_analysis.num_functional()
data_analysis.num_waterpoints()
data_analysis.community_ranking()


# In[9]:

print("*****************************************************Perform Tests***************************************************")
print("\n")

class test_data():
    def testFunctional():
        df = pd.DataFrame([{"water_functioning": "yes"}, {"water_functioning": "yes"}, {"water_functioning": "yes"}, 
                           {"water_functioning": "no"}, {"water_functioning": "no"},])
        print(df)
        print("\n")
        test_numFunctional = df[df.water_functioning == 'yes'].water_functioning.count()
        print("Number of water points that are functional:",test_numFunctional)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
    
    def test_numWaterpoints():
        df = pd.DataFrame([{"communities_villages": "Community1", "water_pointID": "0"}, 
                           {"communities_villages": "Community1", "water_pointID": "1"}, 
                           {"communities_villages": "Community2", "water_pointID": "2"}, 
                           {"communities_villages": "Community2", "water_pointID": "3"}, 
                           {"communities_villages": "Community3", "water_pointID": "4"}, 
                           {"communities_villages": "Community1", "water_pointID": "5"}])
        print(df)
        print("\n")
        test_numWaterpoints = df["communities_villages"].value_counts()
        print("Number of water points per community:\n",test_numWaterpoints)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
        
    def test_communityRanking():
        df = pd.DataFrame([{"communities_villages": "Community1", "water_point_condition": "broken"}, 
                           {"communities_villages": "Community1", "water_point_condition": "functioning"},
                           {"communities_villages": "Community1", "water_point_condition": "broken"},
                           {"communities_villages": "Community1", "water_point_condition": "broken"},
                           {"communities_villages": "Community2", "water_point_condition": "broken"}, 
                           {"communities_villages": "Community2", "water_point_condition": "broken"},
                           {"communities_villages": "Community2", "water_point_condition": "broken"},
                           {"communities_villages": "Community3", "water_point_condition": "functioning"},
                           {"communities_villages": "Community3", "water_point_condition": "broken"},
                           {"communities_villages": "Community3", "water_point_condition": "broken"},
                           {"communities_villages": "Community4", "water_point_condition": "broken"},
                           {"communities_villages": "Community5", "water_point_condition": "broken"}])
        print(df)
        print("\n")
        test_gb = df.groupby(['water_point_condition'])
        test_totalbroken = df[df.water_point_condition == 'broken'].communities_villages.count()
        print("Number of total broken",test_totalbroken)
        print("\n")
        broken_per_community = df[df.water_point_condition == 'broken'].communities_villages.value_counts()
        print("Number of broken water points per community: \n", broken_per_community)
        print("\n")
        test_community_ranking = 100 * df[df.water_point_condition == 'broken'].communities_villages.value_counts() / test_gb["water_point_condition"].get_group("broken").count()
        print("The rank for each community by the percentage of broken water points:\n",test_community_ranking)
        print("-------------------------------------------------------------------------------------------------------------")
        print("\n")
        
        get_ipython().magic('matplotlib inline')
        print("Community rank by line graph:\n")
        test_community_ranking.plot()


test_data.testFunctional()
test_data.test_numWaterpoints()
test_data.test_communityRanking()
