#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Add our dependencies.
import csv
import os
import pandas as pd
import numpy as np

# Import vine data as dataframe
url = 'https://raw.githubusercontent.com/heartgears/Amazon_Vine_Analysis/main/vine_table.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))


# In[8]:


# Filter the data and create a new DataFrame or table to retrieve all the rows 
# where the total_votes count is equal to or greater than 20 to pick reviews 
# that are more likely to be helpful and to avoid having division by zero errors later on.
twenty_votes_df = df[df.total_votes >= 20]
twenty_votes_df


# In[12]:


# Filter the new DataFrame or table created in Step 1 and create a new DataFrame 
# or table to retrieve all the rows where the number of helpful_votes divided 
# by total_votes is equal to or greater than 50%.
helpful_df = twenty_votes_df[twenty_votes_df.helpful_votes/twenty_votes_df.total_votes >=0.5]
helpful_df


# In[39]:


# Filter the DataFrame or table created in Step 2, 
# and create a new DataFrame or table that retrieves all the rows 
# where a review was written as part of the Vine program (paid)
paid_df = helpful_df[helpful_df.vine == 'Y']
paid_df


# In[40]:


# Repeat Step 3, but this time retrieve all the rows where the 
# review was not part of the Vine program (unpaid)
unpaid_df = helpful_df[helpful_df.vine == 'N']
unpaid_df


# In[48]:


# Determine the total number of reviews
unpaid_review_count = unpaid_df.star_rating.count()

print(f"There are {unpaid_review_count} unpaid reviews")

paid_review_count = paid_df.star_rating.count()

print(f"There are {paid_review_count} paid reviews")


# In[46]:


# Determine the number of 5-star reviews
unpaid_fivestar_df = unpaid_df[unpaid_df.star_rating == 5]
unpaid_fivestar_count = unpaid_fivestar_df.star_rating.count()

print(f"There are {unpaid_fivestar_count} unpaid five star ratings")

paid_fivestar_df = paid_df[paid_df.star_rating == 5]
paid_fivestar_count = paid_fivestar_df.star_rating.count()

print(f"There are {paid_fivestar_count} paid five star ratings")


# In[60]:


# Determine the percentage of 5-star reviews for the two types of review
unpaid_fivestar_decimal = float(unpaid_fivestar_count/unpaid_review_count)
unpaid_fivestar_percentage = "{:.0%}".format(unpaid_fivestar_decimal)

print(f"The percentage of fivestar unpaid ratings is {unpaid_fivestar_percentage}")

paid_fivestar_decimal = float(paid_fivestar_count/paid_review_count)
paid_fivestar_percentage = "{:.0%}".format(paid_fivestar_decimal)

print(f"The percentage of fivestar paid ratings is {paid_fivestar_percentage}")


# In[ ]:




