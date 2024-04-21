# import libraries
import pandas as pd
import numpy as np
import plotly.express as px


# csv file
csv_file = 'V-Bucks Account - All Time.csv'
main_csv = pd.read_csv(csv_file)
# formatted heads: DATE, SEASON, AMOUNT, VALUE, CHANGE, VALUE CHANGE, REASON

# visualize the data
def plot_amount():
    fig = px.line(main_csv, x='DATE', y='AMOUNT', title='V-Bucks Account')
    fig.update_xaxes(rangeslider_visible=True)

    fig.show()

def plot_value():
    fig2 = px.line(main_csv, x='DATE', y='VALUE', title='V-Bucks Account Value')
    fig2.update_xaxes(rangeslider_visible=True)

    fig2.show()

def plot_change():
    fig3 = px.bar(main_csv, x='DATE', y='CHANGE', title='V-Bucks Account Change')
    fig3.update_layout(autotypenumbers='convert types')

    fig3.show()


plot_amount()
plot_value()
plot_change()