import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from solve import calculate_real_size, print_solution
 

data = pd.read_csv('dataset.csv')

real_df = calculate_real_size(data)

#define Matplotlib figure and axis
fig, ax = plt.subplots()
min_x = np.max(data['x'])
min_y = np.min(data['y'])

ax.scatter(min_x, min_y, s=0.1)

for index, row in data.iterrows():
    ax.add_patch(Rectangle((row['x'],row['y']), row['Width']/row['Scale'],row['Height']/row['Scale']))
    
for index, row in real_df.iterrows():
    ax.add_patch(Rectangle((row['x'],row['y']), row['Width'],row['Height'],rotation_point='center',angle=row['Rotation']*180/np.pi,facecolor = 'pink'))


print_solution(data, real_df)

#display plot
plt.show()
