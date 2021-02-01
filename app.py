import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from __main__ import *
import Calculations
import Controls
import Callbacks

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])


#############################################################################
# LAYOUT

app.layout = dbc.Container(
    [
        html.H1(children='Title Here'),
        html.Hr(),

        dbc.Row([
            dbc.Col(Controls.Card, md=4),
            dbc.Col(dcc.Graph(id="RawDataGraph"), md=8),
        ], align="center",),
        html.Hr(),

#        dbc.Row([
#            dbc.Col(BulkControls.Bulk_Cards, md=4),
#            dbc.Col(dcc.Graph(id="BulkGraph"), md=8),
#        ], align="center",),
#        html.Hr(),

    ],
    fluid=True,
)
##################################################################
##################################################################
# CALLBACKS

@app.callback(
    Output('RawDataGraph', 'figure'),
    [Input('ExponentSlider', 'value')])
def update_figure(slider_exponent):
    fig = Callbacks.fig(slider_exponent)
    return fig

@app.callback(
    Output('ExponentText', 'children'),
    [Input('ExponentSlider', 'value')])
def update_output(slider_exponent):
    return '{0:.4g}'.format(slider_exponent)


#############################################################################
# RUN ON SERVER
if __name__ == '__main__':
    app.run_server(debug=True)
