import altair as alt
import pandas as pd
import streamlit as st

import altair as alt
import pandas as pd

# Load data
df = pd.read_csv('data/transfer_learning.csv')

# Data transformations
df['n_targets_num'] = pd.to_numeric(df['n_targets'])
pivoted = df.pivot_table(
    index=['bid', 'n_targets_num'],
    columns='mode',
    values='best_val_loss',
    aggfunc='mean'
).reset_index()

# Calculate relative percentages
pivoted['mean_none'] = pivoted['none'].mean()
pivoted['best_percent'] = pivoted['best'] / pivoted['mean_none'] * 100
pivoted['worst_percent'] = pivoted['worst'] / pivoted['mean_none'] * 100

# Create selector for bid
bid_selector = alt.binding_select(
    options=[str(i) for i in range(121) if i not in [15,20,21,32,36,39,43,49,50,52,53,54,57,58,59,60,61,66,67,70,71,91,92,99,100,103,104,105,108,109,115,118]],
    name='bid'
)
bid_selection = alt.selection_point(fields=['bid'], bind=bid_selector)

# Base chart settings
width = 800
height = 200

# Create the layered chart
best_scatter = alt.Chart(pivoted).mark_point(
    color='red'
).encode(
    x=alt.X('n_targets_num:Q', title='Number of source buildings'),
    y=alt.Y('best_percent:Q', title='Validation loss [%]')
).properties(
    width=width,
    height=height
)

worst_line = alt.Chart(pivoted).mark_line(
    color='blue'
).encode(
    x='n_targets_num:Q',
    y='worst_percent:Q'
).properties(
    width=width,
    height=height
)

# Combine charts and add selection
chart = (best_scatter + worst_line).add_params(
    bid_selection
).transform_filter(
    bid_selection
)
st.write(chart)