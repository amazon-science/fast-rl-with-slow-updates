import tensorflow as tf
from tensorflow.core.util import event_pb2
import matplotlib.pyplot as plt
import sys, os, string
import numpy
from matplotlib.pyplot import figure
import collections
import plotly.graph_objects as go
import seaborn as sns

figure(figsize=(25, 12), dpi=80)

c_li = [0.1,0.2,0.5,1]
li_all_normalized = []
li_marker_symbol = ['circle', 'diamond','square','star']
#li_color = ['black', 'blue', 'red', 'green', 'brown']
sns.set_palette("colorblind")
current_palette = sns.color_palette("colorblind")
current_palette = current_palette.as_hex()
li_all_normalized.append([0.8,0.9,0.75,0.6,0.8,0.86])
li_all_normalized.append([1,0.97,1,1,0.8,1])
li_all_normalized.append([1,1,.8,.9,1,0.9])
li_all_normalized.append([1,0.75,.6,.95,0.7,0.76])
games = ['Breakout', 'Amidar','Asterix',  'BeamRider', 'Qbert', 'Gopher']
fig = go.Figure()
for index, c in enumerate(li_all_normalized):
    fig.add_trace(go.Scatterpolar(
          r=c,
          name = r"$\tilde c = {}$".format(c_li[index]),
          theta = games,
          fill='toself',
          marker_symbol = li_marker_symbol[index],
          marker_size = 14,
          line=dict(color=current_palette[index])
    ))
fig.update_layout(
    showlegend=True,
    polar = dict(radialaxis = dict(showticklabels = False ,ticks = "", showline=False)),
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",
    font=dict(
        size=18,
        color="black"
    )
)
fig.update_xaxes(visible=False, zeroline = False)
fig.update_yaxes(visible=False, zeroline = False)
fig.show()
assert False


