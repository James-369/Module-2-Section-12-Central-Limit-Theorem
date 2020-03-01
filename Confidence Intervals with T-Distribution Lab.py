#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import the necessary libraries

import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import random
import math


# In[2]:


np.random.seed(20)
population_ages_one = np.random.normal(20, 4, 100000)
population_ages_two = np.random.normal(22, 3, 100000)
# Calculate how much the sample mean differs from the population means 
population_ages = np.concatenate((population_ages_one, population_ages_two))
pop_ages = pd.DataFrame(population_ages)
pop_ages.hist(bins = 100, range = (5, 33), figsize = (9,9))
pop_ages.describe()
# I observed that the sample mean differed from the original population by 1.13 years 


# In[3]:


np.random.seed(23)
sample_size = 25
sample = np.random.choice( a = population_ages, size = sample_size)
sample_mean = sample.mean()
print("Sample Mean : ", sample_mean)
print("Mean Difference : " , population_ages.mean() - sample_mean)


# In[4]:


# Calculating the t-critical value for 95% confidence 
t_critical = stats.t.ppf(q = 0.975, df = sample_size - 1)
print("T - Critical Value : ")
print(t_critical)


# In[6]:


# calculate the standard deviation 
sample_stdev = sample.std()
# Calculate sigma 
sigma = sample_stdev / math.sqrt(sample_size)
# caculate the margin of error 
margin_of_error = sigma * t_critical
confidence_interval = (sample_mean - margin_of_error,
                      sample_mean + margin_of_error)
print("Confidence Interval : ")
print(confidence_interval)


# In[7]:


stats.t.interval(alpha = 0.95,
                df = 24,
                loc = sample_mean, 
                scale = sigma)
# Same Outcome 


# In[8]:


# Make a function to return the confidence interval
def conf_interval(sample):
    '''
    Input : sample
    Output : Confidence interval
    '''
    n = len(sample)
    x_hat = sample.mean()
    t = stats.t.ppf(q = 0.975, df = 24)
    sigma = sample.std() / math.sqrt(sample_size)
    # caculate the margin of error 
    moe = sigma * t
    conf = (x_hat - moe,
           x_hat + moe)
    return conf 


# In[10]:


np.random.seed(12)
sample_size = 25 
intervals = []
sample_means = []
for sample in range(25):
    sample = np.random.choice(a = population_ages, size = sample_size)
    confidence_interval = conf_interval(sample)
    sample_mean = sample.mean()
    sample_means.append(sample_mean)
    intervals.append(confidence_interval)
    


# In[12]:


plt.figure(figsize = (9,9))

plt.errorbar(x = np.arange(0.1, 25, 1),
             y = sample_means,
             yerr = [(top/bot) / 2 for top, bot in intervals],
             fmt = 'o')

plt.hlines(xmin = 0, xmax = 25,
          y = population_ages.mean(),
          linewidth = 2.0,
          color = 'red')



# In[ ]:




