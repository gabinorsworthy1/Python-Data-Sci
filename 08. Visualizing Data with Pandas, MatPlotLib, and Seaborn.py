# %%
# Change working directory to data file locations
import os
try:
    old_wd = os.getcwd()
    new_wd = old_wd[:old_wd.rindex('-') + 3] + r'\Notes\Data'
    os.chdir(new_wd)
    print(f'Working Direcotry: {os.getcwd()}')
except:
    pass

# %%
# Obligatory imports
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sbn

# %% [markdown]
# # Visualizing Data with Pandas, MatPlotLib, and Seaborn
# %% [markdown]
# 1. Load aalStock.csv, store it in a variable with the index set to the
#    'date' column, and with the rows sorted on the same
# %%
# Write your code below:
stocks = pd.read_csv('C://Users/241556/Documents/00 Co-Op/Python-Data-Sci/resources/aalStock.csv')

stocks = stocks.set_index(
    stocks.date.sort_values()
)

stocks.head()

# %% [markdown]
# 2. Show the daily, 7-day rolling average, and 30-day rolling average
#    lines for the 'high' column
#     * The rolling windows should have data only where the statistic can
#       be fully calculated. The 7-day average, for example should only
#       have data starting on the 7th day.
# %%
# Write your code below:

# %% [markdown]
# 3. Make a vertical 3 plot figure with the x-axes lined up. The first
#    plot will have the volume, the second will have close and open, and
#    the third will have high and low
#%%
# Write your code below:

#%% [markdown]
# 4. Load tips.csv to a variable, add a column for tip percentage, and
#    display the first five rows
#%%
# Write your code below:

#%% [markdown]
# 5. Make a swarm plot comparing tip percentages on each day with the
#    markers coloed by smoker or non-smoker
#%%
# Write your code below:

#%%
