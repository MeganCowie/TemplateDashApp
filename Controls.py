import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

###########################################################

Card = dbc.Card([
    dbc.FormGroup([
        dbc.Row([
            dbc.Col(dbc.Label("Exponent", id="ExponentLabel"), md=8),
            dbc.Col(html.Div(id='ExponentText', style = {'text-align': 'right'}), md=4),
        ], justify="between"),
        dbc.Row([
            dbc.Col(dcc.Slider(id='ExponentSlider', min=0, max=10, step=1, value=1,), md=12),
        ]),
    ]),
], body=True,)
