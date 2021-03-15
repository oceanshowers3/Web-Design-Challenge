import pandas as pd

# read csv
df = pd.read_csv('Visualizations/Resources/cities.csv')

# # save as html (without an index)
# df.to_html('data.html')

# # print the dataset
# table = df.to_html()
with open('cities.html', 'w') as fo:
    df.to_html(fo)