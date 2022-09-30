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

def my_mean(li):
    min_index = numpy.min([len(l) for l in li])
    _li = [l[0:min_index] for l in li]
    return numpy.mean(_li,axis=0)

path = sys.argv[1]
# load tensorboard file and return a sequence of rewards
def load_rewards(result_path):
    # init list
    reward_list = []

    # load data
    prev_step = -1
    data = tf.data.TFRecordDataset(result_path)
    for i, serialized_example in enumerate(data):
        event = event_pb2.Event.FromString(serialized_example.numpy())
        for value in event.summary.value:
            if value.tag == "Eval/AverageReturns":
                assert prev_step + 1 == event.step
                prev_step = event.step
                reward_list.append(value.simple_value)

    return reward_list
'''
dic_all = {}
li = os.listdir(path)
for l in li:
    if '.DS_Store' in l:
        continue
    game = l.split("_")[1]
    if game not in dic_all.keys():
        dic_all[game] = {}
    else:
        pass
    alg = l.split("_")[2:-1]
    alg = "-".join(alg)
    temp = path + '/' + l
    try:
        temp = temp + '/' + os.listdir(temp)[0]
        if alg not in dic_all[game].keys():
            dic_all[game][alg] = [load_rewards(temp)]
        else:
            dic_all[game][alg].append(load_rewards(temp))
    except:
        print("problem in {}".format(temp))
'''

dic_all = {}
li = os.listdir(path)
for l in li:
    if '.DS_Store' in l:
        continue
    if '0.075' in l:
        continue
    if '0.025' in l:
        continue
    if '0.005' in l:
        continue
    alg = l.split("_")[2:-1]
    alg = "-".join(alg)
    if alg not in dic_all.keys():
        dic_all[alg] = {}
    else:
        pass
    game = l.split("_")[1]
    if 'Zax' in game or 'Box' in game or 'Kang' in game or 'Seaq' in game:
        continue
    temp = path + '/' + l
    try:
        temp = temp + '/' + os.listdir(temp)[0]
        if game not in dic_all[alg].keys():
            dic_all[alg][game] = [load_rewards(temp)[-1]]
        else:
            dic_all[alg][game].append(load_rewards(temp)[-1])
    except:
        print("problem in {}".format(temp))

dic_all = collections.OrderedDict(sorted(dic_all.items()))


for alg in dic_all.keys():
    for game in dic_all[alg].keys():
        dic_all[alg][game] = numpy.mean(dic_all[alg][game])


li_all = []
for alg in dic_all.keys():
    od = collections.OrderedDict(sorted(dic_all[alg].items()))
    li = list(od.values())
    li_all.append(li)
games = list(dic_all[alg].keys())
print(games)
li_max = numpy.max(li_all,axis=0)

c_li = [0.1,0.2,0.5,1]
li_all_normalized = []
li_marker_symbol = ['circle', 'diamond','square','star']
sns.set_palette("colorblind")
current_palette = sns.color_palette("colorblind")
current_palette = current_palette.as_hex()
for a in li_all:
    temp = [x/y for x,y in zip(a,li_max)]
    li_all_normalized.append(temp)
fig = go.Figure()
for index, c in enumerate(dic_all):
    fig.add_trace(go.Scatterpolar(
          r=li_all_normalized[index],
          name = r"$\tilde c = {}$".format(float(c.split("c")[1].split("-")[0])),
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


