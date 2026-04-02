import pandas as pd
import numpy as np


def calculate_dimension(w, h, angle, scale):
    th = angle % np.pi;
    b = np.array([w,h])/scale
    a = np.array([[np.abs(np.cos(th)), np.sin(th)], [np.sin(th), np.abs(np.cos(th))]])
    x = np.linalg.solve(a, b)
    return x

def calculate_real_size(data):
    real = []

    for index, row in data.iterrows():
        real_dim = calculate_dimension(row['Width'],row['Height'],row['Rotation'],row['Scale'])
        real_x = row['x']+((row['Width']/2)/row['Scale'])-(real_dim[0]/2)
        real_y = row['y']+((row['Height']/2)/row['Scale'])-(real_dim[1]/2)
        real.append({
            'Item':row['Item'],
            'Group':row['Group'],
            'x': real_x,
            'y': real_y,
            'Width':real_dim[0],
            'Height':real_dim[1],
            'Rotation':row['Rotation']
            })
        

    real_df = pd.DataFrame(real)
    
    return real_df

def print_solution(data, real_df):
    print('\nDataset:\n')
    print(data)
    print('\nReal Sizes:\n')
    print(real_df)

    print('\nSolution:\n')

    max_w = np.max(real_df['Width'])
    min_w = np.min(real_df['Width'])
    print("Biggest item is",real_df[real_df['Width'] == max_w]['Item'].item(),"with",max_w)
    print("Smallest item is",real_df[real_df['Width'] == min_w]['Item'].item(),"with",min_w)

    print("Averages:")
    print(real_df.groupby('Group').agg({'Width': np.average}))


if __name__ == '__main__':

    data = pd.read_csv('dataset.csv')

    real_df = calculate_real_size(data)
    
    print_solution(data, real_df)
    

