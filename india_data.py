import numpy as np
import pandas as pd

districts = pd.read_csv('district wise centroids.csv')
census = pd.read_csv('india-districts-census-2011.csv')

india = districts.merge(census,left_on='District',right_on='District name')
india_df = india.drop(columns=[
    'District name',
    'State name',
])
india_df['Literacy_Percentage'] = india_df['Literate'] / india_df['Population']
india_df.to_csv('india.csv')
