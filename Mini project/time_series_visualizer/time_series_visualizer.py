import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df.index, df['value'], color='r', linewidth=1)
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.strftime('%B')

    # Create pivot table for bar plot
    df_bar = df_bar.pivot_table(values='value', index='year', columns='month', aggfunc='mean',
                                month_order=['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])

    # Define month order for sorting
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.heatmap(data=df_bar, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Average Page Views'})
    ax.set_xlabel('Year')
    ax.set_ylabel('Months')
    ax.set_title('Average Page Views per Year and Month')
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(16, 6))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')
    axes[0].set_title('Year-wise Box Plot (Trend)')

    sns.boxplot(x='month', y='value', data=df_box, order=month_order, ax=axes[1])
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')
    axes[1].set_title('Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
