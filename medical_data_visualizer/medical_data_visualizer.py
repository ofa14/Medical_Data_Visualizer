import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
url = 'https://raw.githubusercontent.com/a-mt/fcc-medical-data-visualizer/refs/heads/master/medical_examination.csv'
df = pd.read_csv(url)

# Adding 'overweight' column
df['BMI'] = df['weight'] / (df['height'] / 100) ** 2
df['overweight'] = (df['BMI'] > 25).astype(int)
df.drop(columns=['BMI'], inplace=True)

# Normalize data
for col in ['cholesterol', 'gluc']:
    df[col] = (df[col] > 1).astype(int)

#Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt`
    df_cat = pd.melt(df, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])
    
    # Group and reformat the data
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).size().reset_index(name="total")
    
    #  catplot
    g = sns.catplot(x="variable", y="total", hue="value", col="cardio", kind="bar", data=df_cat)
    
    return g.fig

#  Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]
    
    # Calculate the correlation matrix
    corr = df_heat.corr()
    
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))
    
    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12, 8))
    
    # Draw the heatmap
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", linewidths=0.5, cmap="coolwarm", ax=ax)
    
    return fig


cat_plot = draw_cat_plot()
heat_map = draw_heat_map()
plt.show()
