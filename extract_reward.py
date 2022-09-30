import tensorflow as tf
from tensorflow.core.util import event_pb2
import matplotlib.pyplot as plt
import sys, os, string
import numpy
from matplotlib.pyplot import figure
import collections

figure(figsize=(25, 12), dpi=80)

def my_mean(li):
    min_index = numpy.min([len(l) for l in li])
    _li = [l[0:min_index] for l in li]
    return numpy.mean(_li,axis=0)

def smooth(y, win = 5):
    if len(y) > win:
        yhat = [numpy.mean(y[x-win:x+win]) for x in range(len(y))]
        return yhat
    return y

li_smooth = [numpy.mean([])]

import argparse

parser = argparse.ArgumentParser(description='getting results from ec2', 
                                 formatter_class=argparse.RawTextHelpFormatter)

parser.add_argument('--name',
                    type = str,
                    required = True)
args = parser.parse_args()



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
            #if value.tag == "Train/Loss":
                assert prev_step + 1 == event.step
                prev_step = event.step
                reward_list.append(value.simple_value)

    return reward_list

dic_all = {}
li = os.listdir(args.name)
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
    try:
        temp = args.name + '/' + l
        temp = temp + '/' + os.listdir(temp)[0]
        print("*********")
        print(temp)
        temp = load_rewards(temp)
        print(len(temp))
        print("*********")
        if alg not in dic_all[game].keys():
            dic_all[game][alg] = [temp]
        else:
            dic_all[game][alg].append(temp)
    except:
        pass

#print(dic_all)
#assert False


for domain_index, domain in enumerate(dic_all.keys()):
    plt.subplot2grid((2,5), (int(domain_index/5), domain_index%5))
    od = collections.OrderedDict(sorted(dic_all[domain].items()))
    for alg in od.keys():
        if 'd0.005-' in alg or 'd0-' in alg :
            plt.plot(smooth(my_mean(od[alg])),label=alg, lw=3)
            #plt.plot(my_mean(od[alg]),label=alg, lw=3)
    if domain_index + 1 == len(dic_all):
        plt.legend(fontsize=14, loc = 'lower right')
    plt.title(domain)
plt.show()
plt.close()


