from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd
import datetime
# Load data
df = pd.read_csv(r'D:\online task\formatted_output.csv')

# Ensure date is sorted
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
df = df.sort_values('date')

# Aggregate sales by date (all regions combined)
df_grouped = df.groupby('date', as_index=False)['sales'].sum()

# Create line chart
fig = px.line(
    df_grouped,
    x='date',
    y='sales',
    title='Pink Morsel Sales Over Time',
    labels={'date': 'Date', 'sales': 'Total Sales ($)'}
)

# Add vertical line for price increase on Jan 15, 2021

fig.add_vline(
    x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
    line_dash='dash',
    line_color='red',
    annotation_text='Price Increase (Jan 15, 2021)',
    annotation_position='top left'
)
fig.update_layout(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Arial', size=13),
    title_font_size=20,
    xaxis=dict(showgrid=True, gridcolor='lightgrey'),
    yaxis=dict(showgrid=True, gridcolor='lightgrey'),
)

# Build Dash app
app = Dash(__name__)

app.layout = html.Div(
    style={'fontFamily': 'Arial', 'maxWidth': '1100px', 'margin': '0 auto', 'padding': '20px'},
    children=[
        html.H1(
            'Soul Foods – Pink Morsel Sales Visualiser',
            style={'textAlign': 'center', 'color': '#333'}
        ),
        html.P(
            'This visualiser displays total Pink Morsel sales over time across all regions. '
            'The red dashed line marks the price increase on January 15, 2021.',
            style={'textAlign': 'center', 'color': '#666'}
        ),
        dcc.Graph(figure=fig, style={'height': '550px'}),
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
