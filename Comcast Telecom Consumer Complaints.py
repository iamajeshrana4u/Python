#!/usr/bin/env python
# coding: utf-8

# # Project Details

# #### Description
# 
# Comcast is an American global telecommunication company. The firm has been providing terrible customer service. They continue to fall short despite repeated promises to improve. Only last month (October 2016) the authority fined them a $2.3 million, after receiving over 1000 consumer complaints.
# The existing database will serve as a repository of public customer complaints filed against Comcast.
# It will help to pin down what is wrong with Comcast's customer service.
# 
# Data Dictionary
# 
# 
# Ticket #: Ticket number assigned to each complaint
# Customer Complaint: Description of complaint
# Date: Date of complaint
# Time: Time of complaint
# Received Via: Mode of communication of the complaint
# City: Customer city
# State: Customer state
# Zipcode: Customer zip
# Status: Status of complaint
# Filing on behalf of someone
# 
# Question
# 
# Q1-Import data into Python environment.
# Q2-Provide the trend chart for the number of complaints at monthly and daily granularity levels.
# Q3-Provide a table with the frequency of complaint types.
#            Q3.1-Which complaint types are maximum i.e., around internet, network issues, or across any other domains.
# Q4-Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.
# Q5-Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from Q3. Provide insights on:
#            Q5.1-Which state has the maximum complaints
#            Q5.2-Which state has the highest percentage of unresolved complaints
# Q6-Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.

# In[1]:


# load important libraries
import numpy as np
import pandas as pd


# #### Q1-Import data into Python Environment

# In[2]:


telecom_data=pd.read_csv("D:/1.PG & Master/1.Data Science/2.Data Science With Python/Project/Project-2/Comcast_telecom_complaints_data.csv")


# In[3]:


telecom_data


# In[4]:


telecom_data.head()


# In[5]:


# Check and findout data types in columns
telecom_data.dtypes


# In[6]:


# To check columns names
telecom_data.columns


# In[7]:


# (2224, 11) Means 2224 Row, 11 Column
telecom_data.shape


# In[8]:


# No Missing value found in this dataset
telecom_data.info()


# In[9]:


# Note: Describe() only work numerical data, This function helps to findout outlier in columns (Numeric Columns)
telecom_data.describe()


# In[10]:


# Note : There is no missing value in dataset
telecom_data.isna().sum()


# #### Q2-Provide the trend chart for the number of complaints at monthly and daily granularity levels.

# In[11]:


# Adding a new variable in existing dataset, Because i want to find out the month wise complaints
telecom_data["data_time"]=telecom_data["Date_month_year"] + " " + telecom_data["Time"]


# In[12]:


telecom_data


# In[13]:


# Now convert from data_time and Date_month_year to Date Time Format
telecom_data["data_time"]=pd.to_datetime(telecom_data["data_time"])


# In[14]:


# Now convert from data_time and Date_month_year to Date Time Format
telecom_data["data_time"]=pd.to_datetime(telecom_data["data_time"])
telecom_data["Date_month_year"]=pd.to_datetime(telecom_data["Date_month_year"])
telecom_data_monthly=telecom_data.set_index(telecom_data["data_time"])


# In[15]:


# Visualization librabry import
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[16]:


# Provide the trend chart for the number of complaints at monthly granularity levels.
plt.figure(figsize=(12,8))
plt.suptitle('Number of Complaints at Monthly Granularity Levels')
plt.ylabel('Number of Complaints')
telecom_data_monthly.groupby(pd.Grouper(freq="M")).size().plot(color='blue')


# In[17]:


# Provide the trend chart for the number of complaints at daily granularity levels.
telecom_data['Day of Month'] = pd.to_datetime(telecom_data['Date'])
telecom_data_daily = telecom_data.set_index(telecom_data["Day of Month"])
#Increase Graph Size
plt.figure(figsize=(12,8))
plt.suptitle('Number of complaints at Daily granularity levels')
plt.ylabel('Number of Complaints')
telecom_data_daily.groupby(pd.Grouper(freq="D")).size().plot(color='green')


# #### Q3-Provide a table with the frequency of complaint types.

# In[18]:


# To get the frequency of complaint types first we have to see all complaint types and check for duplicate, case sensentive
# Incomplete data so that we can make analytics better
telecom_data_frequency=telecom_data["Customer Complaint"].value_counts()


# In[19]:


telecom_data_frequency


# In[20]:


telecom_data_frequency.head(10)


# In[21]:


# Better to convert all data into uper case or sentence case so duplicate value will shorted
telecom_data_frequency=telecom_data["Customer Complaint"].str.upper().value_counts()


# #### Q3.1-Which complaint types are maximum i.e., around internet, network issues, or across any other domains.

# In[22]:


telecom_data_frequency.head(50)
# COMCAST, COMCAST DATA CAP, COMCAST INTERNET are the Highest top 3 complaint types


# #### Q4-Create a new categorical variable with value as Open and Closed. Open & Pending is to be categorized as Open and Closed & Solved is to be categorized as Closed.

# In[23]:


# Check how many unique values are under Status Column 
telecom_data['Status'].unique()


# In[24]:


# Convert as per Instruction (Task 4) into New Column without changing the main data so that we can use the main data
# in Future
telecom_data['O_P_Status']= ["Open" if Status=="Open" or Status=="Pending" else 
                                      "Closed" for Status in telecom_data["Status"]]


# In[25]:


telecom_data


# In[26]:


# Check whether all status updated or not
telecom_data['O_P_Status'].unique()


# In[27]:


telecom_data_state_status = pd.crosstab(telecom_data["State"],telecom_data ["O_P_Status"])


# In[28]:


telecom_data_state_status


# #### Q5-Provide state wise status of complaints in a stacked bar chart. Use the categorized variable from Q3. Provide insights on:

# #### Q5.1-Which state has the maximum complaints

# In[29]:


pd.crosstab(telecom_data.State,telecom_data.O_P_Status).plot(kind='bar',figsize=(16,6),
                                                      stacked=True,
                                                      title='State Wise Status of Complaints')


# In[30]:


#Georgia has maximum number of complaints


# #### Q5.2-Which state has the highest percentage of unresolved complaints

# In[31]:


telecom_data_unresolved_complaints = telecom_data[telecom_data['O_P_Status']=='Open']


# In[32]:


telecom_data_unresolved_complaints


# In[33]:


telecom_data_unresolved_complaints_count = telecom_data_unresolved_complaints.State.value_counts()
telecom_data_unresolved_complaints_count


# In[34]:


# Georgia has the Highest Number of unresolved complaints
# Show this by Bar Graph
telecom_data_unresolved_complaints_count.plot(kind='bar',figsize=(14,12),color="green")
plt.title('Highest percentage of Unresolved Complaints\n')


# #### Q6-Provide the percentage of complaints resolved till date, which were received through the Internet and customer care calls.

# In[35]:


# Check unique values in Received Via Column
telecom_data['Received Via'].unique()


# In[36]:


# So there are only two values in that columns so no need to short we can directly proceed to task 6


# In[37]:


telecom_data["O_P_Status"].value_counts()


# In[38]:


# Used autopct='%1.1f%%'  to show percentage under the pie chart
myexplode = [0.2, 0]
plt.title('Complaints Status through the Internet & Customer Care Calls\n')
telecom_data["O_P_Status"].value_counts().plot(kind='pie',explode = myexplode,autopct='%1.1f%%',
                        figsize = (14,6))


# ### Summary of this project

# In[40]:


# Important Library Used
# Numpy- For Array and Mathematically Calculation
# Pandas- For EDA
# Seaborn- For Vsualization

