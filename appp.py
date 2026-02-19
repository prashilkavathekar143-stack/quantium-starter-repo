from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import datetime

# Load data
df = pd.read_csv(r'D:\quantium\formatted_output.csv')
df['date'] = pd.to_datetime(df['date'], format='mixed', dayfirst=True)
df = df.sort_values('date')

app = Dash(__name__)

app.layout = html.Div(
    style={
        'fontFamily': 'Arial, sans-serif',
        'backgroundColor': '#f4f6f9',
        'minHeight': '100vh',
        'padding': '20px'
    },
    children=[
        # Header
        html.Div(
            style={
                'backgroundColor': '#e91e8c',
                'padding': '25px',
                'borderRadius': '12px',
                'marginBottom': '25px',
                'textAlign': 'center',
                'boxShadow': '0 4px 12px rgba(0,0,0,0.15)'
            },
            children=[
                html.H1('Soul Foods - Pink Morsel Sales Visualiser',
                        style={'color': 'white', 'margin': '0', 'fontSize': '28px'}),
                html.P('Analyse Pink Morsel sales across regions over time',
                       style={'color': '#ffe0f0', 'margin': '8px 0 0 0', 'fontSize': '14px'})
            ]
        ),

        # Radio button filter
        html.Div(
            style={
                'backgroundColor': 'white',
                'padding': '20px 30px',
                'borderRadius': '12px',
                'marginBottom': '20px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
            },
            children=[
                html.H3('Filter by Region', style={'margin': '0 0 12px 0', 'color': '#333', 'fontSize': '16px'}),
                dcc.RadioItems(
                    id='region-filter',
                    options=[
                        {'label': ' All', 'value': 'all'},
                        {'label': ' North', 'value': 'north'},
                        {'label': ' East', 'value': 'east'},
                        {'label': ' South', 'value': 'south'},
                        {'label': ' West', 'value': 'west'},
                    ],
                    value='all',
                    inline=True,
                    style={'fontSize': '15px'},
                    inputStyle={'marginRight': '6px'},
                    labelStyle={'marginRight': '20px', 'color': '#444', 'cursor': 'pointer'}
                )
            ]
        ),

        # Chart
        html.Div(
            style={
                'backgroundColor': 'white',
                'padding': '20px',
                'borderRadius': '12px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)'
            },
            children=[
                dcc.Graph(id='sales-chart', style={'height': '500px'})
            ]
        ),

        # Footer
        html.Div(
            style={'textAlign': 'center', 'marginTop': '20px', 'color': '#999', 'fontSize': '13px'},
            children=[html.P('The red dashed line marks the Pink Morsel price increase on January 15, 2021')]
        )
    ]
)


@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    if selected_region == 'all':
        filtered = df.groupby('date', as_index=False)['sales'].sum()
    else:
        filtered = df[df['region'] == selected_region].groupby('date', as_index=False)['sales'].sum()

    fig = px.line(
        filtered,
        x='date',
        y='sales',
        title=f'Pink Morsel Sales Over Time - {selected_region.capitalize()}',
        labels={'date': 'Date', 'sales': 'Total Sales ($)'}
    )

    fig.add_vline(
        x=datetime.datetime(2021, 1, 15).timestamp() * 1000,
        line_dash='dash',
        line_color='red',
        annotation_text='Price Increase (Jan 15, 2021)',
        annotation_position='top left'
    )

    fig.update_traces(line_color='#e91e8c', line_width=1.5)
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(family='Arial', size=13),
        title_font_size=18,
        xaxis=dict(showgrid=True, gridcolor='#f0f0f0'),
        yaxis=dict(showgrid=True, gridcolor='#f0f0f0'),
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
