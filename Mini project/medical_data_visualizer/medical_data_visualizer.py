import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('E:/Project/Machine Learning/Freecodecamp - Data Analysis with Python/Mini project/medical_data_visualizer/medical_examination.csv')

# Add 'overweight' column
weight = df['weight']
height = df['height']/100
df['BMI'] = weight/height**2

df['overweight'] = (df['BMI'] >= 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df[['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight', 'cardio']]


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = pd.melt(df_cat, id_vars=['cardio'], var_name='feature', value_name='count')
    

    # Draw the catplot with 'sns.catplot()'
    g = sns.catplot(x='feature', y='count', col='cardio', data=df_cat, kind='bar', height=5, aspect=2)



    # Get the figure for the output
    fig = g.set_axis_labels('Categorical Features', 'Count')

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones(corr.shape), k=1).astype(bool)

    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, annot=True, fmt=".1f", linewidths=.5, cmap='coolwarm', mask=mask, ax=ax)

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
