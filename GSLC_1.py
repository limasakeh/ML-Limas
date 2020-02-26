#!/usr/bin/env python
# coding: utf-8

# # Untuk Read file listings.csv

# In[2]:


import pandas as pd

sgAirbnbData = pd.read_csv("listings.csv", names=["id","name","host_id","host_name","neighbourhood_group","neighbourhood"
                                                 ,"latitude","longitude","room_type","price","minimum_nights","number_of_reviews",
                                                 "last_review","reviews_per_month","calculated_host_listings_count","availability_365"],
                          skiprows = 1, delimiter=",")

print(sgAirbnbData.head())


# # Mencari min value dari tiap data

# In[25]:


minValue = sgAirbnbData.min()

print(minValue)

for index, items in minValue.iteritems():
    print("Lowest", index, "is :", str(items))


# # mencari max value dari tiap data

# In[26]:


maxValue = sgAirbnbData.max()

print(maxValue)

for index, items in maxValue.iteritems():
    print("Highest", index, "is :", str(items))


# # Menghapus 1 row dimana salah satu datanya NULL

# In[14]:


sgAirbnbDataDropNull = sgAirbnbData.dropna()

print(sgAirbnbDataDropNull.isna().values.any())

print(len(sgAirbnbDataDropNull))


# # Mengganti value NULL menjadi 0

# In[15]:


sgAirbnbDataReplaceNull = sgAirbnbData.fillna(0)

print(sgAirbnbDataReplaceNull.isna().values.any())

print(len(sgAirbnbDataReplaceNull))
                                              


# # Mencari satu row secara spesifik, kemudian fill NaN dengan 0

# In[47]:


searchValue = 355955
print(sgAirbnbData.loc[sgAirbnbData["id"] == searchValue].fillna("0"))


# # Mencari 1 column dimana id merupakan paling rendah / tinggi,
# # dan print hanya kolom id hingga host_name

# In[40]:


print("Lowest ID : \n", sgAirbnbData[sgAirbnbData.id == sgAirbnbData.id.min()].loc[:,"id":"host_name"])

print("\n\n")

print("Highest ID :\n", sgAirbnbData[sgAirbnbData.id == sgAirbnbData.id.max()].loc[:,"id":"host_name"])


# # Mencari mean dari integer yang ada dalam data

# In[55]:


meanValue = sgAirbnbData.mean()

pd.options.display.float_format = '{:10,.2f}'.format


for index, items in meanValue.iteritems():
    print("Average ", index, "is :", str(items))


# In[ ]:




