import dash
from dash import dcc, html
import pandas as pd

filepath='resources/final_probs.csv'
df=pd.read_csv(filepath)
names=df['Name'].values
index=df['Name'].index.values
nameslist = list(zip(index, names))

tab_4_layout = html.Div([
    html.H3('Would you survive the Titanic?'),
    html.Div([
        # Title,
        html.Div([
            html.Div('     ', className='one column'),
            html.Div('Siblings and Spouses', className='optionTitle'),
            dcc.Dropdown(
                id='family_dropdown',
                options=[{'label': i, 'value': i} for i in range(0,9)],
                value='2',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Age', className='optionTitle'),
            dcc.Dropdown(
                id='age_dropdown',
                options=[{'label': i, 'value': i} for i in range(1,81)],
                value='25',

                ),
        ],className='four columns'),
        html.Div([
            html.Div('Cabin Class', className='optionTitle'),
            dcc.Dropdown(
                id='cabin_dropdown',
                options=[{'label': i, 'value': i} for i in ['First', 'Second', 'Third']],
                value='First',
                ),
        ],className='four columns'),
        html.Div('     ', className='one column')
    ],className='twelve columns'),

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    html.Div([
        html.Div('     ', className='one column'),
        html.Div('     ', className='one column'),
        html.Div('     ', className='one column'),
        html.Div([
            html.Div('Title', className='optionTitle'),
            dcc.RadioItems(
                id='title_radio',
                options=[{'label': i, 'value': i} for i in ['Mr.', 'Miss', 'Mrs.', 'VIP']],
                value='None',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Sex', className='optionTitle'),
            dcc.RadioItems(
                id='sex_radio',
                options=[{'label': i, 'value': i} for i in ['Male', 'Female']],
                value='None',
                ),
        ],className='three columns'),
        html.Div([
            html.Div('Port of Embarkation', className='optionTitle'),
            dcc.RadioItems(
                id='port_radio',
                options=[{'label': i, 'value': i} for i in ['Cherbourg', 'Queenstown', 'Southampton']],
                value='None',
                ),
        ],className='five columns'),
    ],className='fifteen columns'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
    # Output results
    html.Div([
        html.Div(id='user-inputs-box', style={'text-align':'center','fontSize':18}),
        html.Div(id='final_prediction', style={'color':'red','text-align':'center','fontSize':18})
    ],className='twelve columns'),



], className='container')
