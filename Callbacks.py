import plotly.graph_objects as go

import Calculations

color_darkgreen ='#2ca02c'
color_lightgreen ='#bcbd22'
color_darkblue ='#1f77b4'
color_lightblue ='#17becf'
color_purple ='#9467bd'
color_pink = '#e377c2'
color_orange ='#ff7f0e'
color_brown ='#8c564b'
color_darkgrey ='#888888'
color_lightgrey ='#a9a9a9'
color_black ='#2f4f4f'

#############################################################################


def fig(slider_exponent):
    exponent = slider_exponent
    x = Calculations.x()
    y = Calculations.y(x,exponent)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x = x, y = y,
        name = "xy", mode='lines',
        line_color=color_darkgrey
        ))
    fig.update_layout(title='Raw Data',
                      xaxis_title='time (s)', yaxis_title='intensity (V)',
                      transition_duration=500)
    return fig
