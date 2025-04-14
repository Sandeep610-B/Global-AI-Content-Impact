#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[7]:


df =pd.read_csv(r"C:\Users\sande\Downloads\archive (2)\Global_AI_Content_Impact_Dataset.csv")
df


# In[8]:


# Check for missing values
print(df.isnull().sum())


# In[9]:


# Check data types
print(df.dtypes)


# In[10]:


# Remove duplicates
df = df.drop_duplicates()


# In[11]:


df


# # What industries have the highest average AI adoption?"
# 
# 

# In[13]:


industry_adoption = df.groupby("Industry")["AI Adoption Rate (%)"].mean().sort_values(ascending=False)


# In[14]:


industry_adoption


# In[15]:


import matplotlib.pyplot as plt


# # Figuring out top 10 Industries

# In[32]:


plt.figure(figsize=(10,6))
industry_adoption.plot(kind='bar', color='skyblue')
plt.title("Top 10 Industries by AI Adoption Rate")
plt.ylabel("Adoption Rate (%)")
plt.xlabel("Industry")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()


# # How does Job Loss correlate with Revenue Increase?

# In[30]:


plt.figure(figsize=(8,6))
plt.scatter(df["Job Loss Due to AI (%)"], df["Revenue Increase Due to AI (%)"], color='purple', alpha=0.6)
plt.title("Job Loss vs Revenue Increase due to AI")
plt.xlabel("Job Loss Due to AI (%)")
plt.ylabel("Revenue Increase Due to AI (%)")
plt.grid(True)
plt.show()


# # How does Consumer Trust vary by Regulation Status? 

# In[35]:


trust_by_regulation = df.groupby("Regulation Status")["Consumer Trust in AI (%)"].mean()
trust_by_regulation


# In[60]:


plt.figure(figsize=(7,5))
trust_by_regulation.plot(kind='bar', color='salmon')
plt.title("Consumer Trust by Regulation Status")
plt.ylabel("Consumer Trust (%)")
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# #  Which countries have the highest AI-generated content?

# In[33]:


top_countries = df.groupby("Country")["AI-Generated Content Volume (TBs per year)"].mean().sort_values(ascending=False)


# In[34]:


top_countries


# In[37]:


plt.figure(figsize=(10,6))
top_countries.plot(kind='bar', color='limegreen')
plt.title("Top 10 Countries by AI-Generated Content Volume")
plt.ylabel("Volume (TB/year)")
plt.tight_layout()
plt.grid(True)
plt.show()


# # AI Adoption Trends Over Time

# In[40]:


adoption_by_year = df.groupby("Year")["AI Adoption Rate (%)"].mean()


# In[41]:


adoption_by_year


# In[44]:


adoption_by_year.plot(kind='line', marker='o', color='green')
plt.title("AI Adoption Rate Over Time")
plt.xlabel("Year")
plt.ylabel("Average Adoption Rate (%)")
plt.grid(True)
plt.show()


# #  2. Consumer Trust by Country (Top 10)

# In[49]:


trust_by_country = df.groupby("Country")["Consumer Trust in AI (%)"].mean().sort_values(ascending=False)
trust_by_country


# In[50]:


trust_by_country.plot(kind='bar', color='orange')
plt.title("Top 10 Countries by Consumer Trust in AI")
plt.xlabel("Country")
plt.ylabel("Average Trust (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# # Human-AI Collaboration vs AI Adoption

# In[51]:


plt.scatter(
    df["AI Adoption Rate (%)"],
    df["Human-AI Collaboration Rate (%)"],
    color='teal',
    alpha=0.6
)
plt.title("AI Adoption vs Human-AI Collaboration")
plt.xlabel("AI Adoption Rate (%)")
plt.ylabel("Collaboration Rate (%)")
plt.grid(True)
plt.show()


# # Regulation Status vs AI Market Share

# In[52]:


# Group data by 'Regulation Status' and compute average market share
market_share_by_regulation = df.groupby("Regulation Status")["Market Share of AI Companies (%)"].mean()


# In[53]:


market_share_by_regulation


# In[55]:


# Plotting
plt.figure(figsize=(7, 5))
market_share_by_regulation.plot(kind='bar', color='steelblue')

# Chart details
plt.title("Average AI Company Market Share by Regulation Status")
plt.xlabel("Regulation Status")
plt.ylabel("Market Share (%)")
plt.grid(axis='y', linestyle='--', alpha=1.0)
plt.tight_layout()
plt.show()


# How is the dataset split across different AI regulation statuses?# 

# In[56]:


# Count how many rows belong to each regulation status
regulation_counts = df["Regulation Status"].value_counts()

regulation_counts


# In[58]:


# Plot as pie chart
plt.figure(figsize=(7, 7))
plt.pie(regulation_counts, labels=regulation_counts.index, autopct='%1.1f%%', startangle=140, colors=['#66b3ff','#ff9999','#99ff99'])

# Add title
plt.title("Distribution of Regulation Status in the Dataset")
plt.axis('equal') 
plt.show()


# In[ ]:




