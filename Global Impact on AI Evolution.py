#!/usr/bin/env python
# coding: utf-8

# In[10]:





# In[103]:


import pandas as pd
import matplotlib.pyplot as plt


# In[104]:


df =pd.read_csv(r"C:\Users\sande\Downloads\archive (2)\Global_AI_Content_Impact_Dataset.csv")


# In[105]:


df


# In[106]:


# View the first 5 rows
print(df.head())


# In[107]:


# Check data types and missing values
print(df.info())


# In[108]:


# Summary statistics
print(df.describe())


# #  Analyze Trends Over Years

# In[109]:


# Group data by Year and calculate mean adoption rate
yearly_adoption = df.groupby('Year')['AI Adoption Rate (%)'].mean()


# In[110]:


yearly_adoption


# In[111]:


# Plot
yearly_adoption.plot(kind='line', marker='o', color='green')
plt.title("AI Adoption Rate Over Time")
plt.xlabel("Year")
plt.ylabel("Average Adoption Rate (%)")
plt.grid(True)
plt.show()


# # Compare Countries

# In[112]:


# Top 5 countries by average AI adoption
country_adoption = df.groupby('Country')['AI Adoption Rate (%)'].mean().sort_values(ascending=False)
country_adoption


# In[113]:


# Plot
plt.figure(figsize=(10, 5))
country_adoption.plot(kind='bar', color='skyblue')
plt.title('Top 5 Countries by AI Adoption Rate (%)')
plt.xlabel('Country')
plt.ylabel('Average AI Adoption Rate (%)')
plt.xticks(rotation=45)
plt.show()


# # Industry-Specific Analysis

# In[114]:


industry_tools = df.groupby('Industry')['Top AI Tools Used'].value_counts().unstack().fillna(0)


# In[115]:


industry_tools


# In[116]:


# Plot
industry_tools.plot(kind='bar', stacked=True, figsize=(12, 6))
plt.title('Popular AI Tools by Industry')
plt.xlabel('Industry')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='AI Tools')
plt.show()


# # Relationship Between AI Adoption and Job Loss

# In[117]:


plt.figure(figsize=(8, 6))
plt.scatter(df['AI Adoption Rate (%)'], df['Job Loss Due to AI (%)'], alpha=0.5)
plt.title('AI Adoption vs. Job Loss')
plt.xlabel('AI Adoption Rate (%)')
plt.ylabel('Job Loss Due to AI (%)')
plt.grid(True)
plt.show()


# # Regulation Status Distribution

# In[118]:


regulation_counts = df['Regulation Status'].value_counts()


# In[119]:


regulation_counts


# In[120]:


plt.figure(figsize=(8, 6))
regulation_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140)
plt.title('Distribution of AI Regulation Status')
plt.ylabel('')
plt.show()


# # Temporal Trends: Industry-Specific AI Adoption

# In[121]:


# Pivot table for heatmap
industry_year_adoption = df.pivot_table(
    index='Industry', 
    columns='Year', 
    values='AI Adoption Rate (%)', 
    aggfunc='mean'
)


# In[122]:


industry_year_adoption


# In[123]:


import seaborn as sns
# Plot heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(industry_year_adoption, annot=True, cmap='YlGnBu',fmt=".1f")
plt.title('AI Adoption Rate (%) by Industry and Year')
plt.xlabel('Year')
plt.ylabel('Industry')
plt.show()


# In[ ]:





# In[124]:


plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df,
    x='AI-Generated Content Volume (TBs per year)',
    y='Revenue Increase Due to AI (%)',
    hue='Industry',
    palette='tab20',
    s=100
)
plt.title('AI Content Volume vs. Revenue Increase')
plt.xlabel('AI Content Volume (TB/year)')
plt.ylabel('Revenue Increase (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[ ]:





# In[125]:


plt.figure(figsize=(100, 6))
sns.boxplot(
    data=df,
    x='Human-AI Collaboration Rate (%)',
    y='Job Loss Due to AI (%)',
    hue='Regulation Status',
    palette='Set2'
)
plt.title('Job Loss vs. Human-AI Collaboration (by Regulation)')
plt.xlabel('Human-AI Collaboration Rate (%)')
plt.ylabel('Job Loss Due to AI (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# # Tool Popularity by Industry

# In[126]:


tool_industry = pd.crosstab(df['Industry'], df['Top AI Tools Used'])


# In[127]:


tool_industry


# In[128]:


tool_industry.plot(kind='bar', stacked=True, figsize=(14, 8))
plt.title('AI Tool Dominance by Industry')
plt.xlabel('Industry')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.legend(title='AI Tools', bbox_to_anchor=(1.05, 1))
plt.show()


# In[129]:


plt.figure(figsize=(10, 6))
sns.violinplot(
    data=df,
    x='Regulation Status',
    y='Consumer Trust in AI (%)',
    palette='pastel',
    inner='stick'
)
plt.title('Consumer Trust in AI by Regulation Status')
plt.xlabel('Regulation Status')
plt.ylabel('Consumer Trust (%)')
plt.show()


# # Market Share of AI Companies by Country

# In[130]:


top_countries = df.groupby('Country')['Market Share of AI Companies (%)'].mean().nlargest(5)


# In[131]:


top_countries


# In[132]:


plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_countries.index,
    y=top_countries.values
)
plt.title('Top 5 Countries by AI Market Share (%)')
plt.xlabel('Country')
plt.ylabel('Market Share (%)')
plt.xticks(rotation=45)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




