import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
from collections import deque, Counter

########### Define your variables ######

myheading1='Prepare your ANGRY Tweets here'
initial_value="Shouting placeholder"
longtext='''
        _Suggestions you might try:_
        * No you!
        * Bite me
        * Piss off mate
        '''
tabtitle = 'AutoTweet'
sourceurl = 'https://www.twitter.com'
githublink = 'https://github.com/ihdorfman/dash-simple-callback'

########### Define a function for your callback:
def my_function(letters):
    return(letters.upper()+'!!!!!!!!!')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1(myheading1),
    html.Div(children=[dcc.Markdown(longtext)]),
    dcc.Input(id='my-id', value=initial_value, type='text'),
    html.Div(id='my-div'),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########## Define Callback
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    angry=my_function(input_value)
    return f"The next time someone disagrees with you on Twitter the proper response is: '{angry}'"

############ Deploy
if __name__ == '__main__':
    app.run_server()
