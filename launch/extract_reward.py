import tensorflow as tf
from tensorflow.core.util import event_pb2
import matplotlib.pyplot as plt


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

li = load_rewards('./results/events.out.tfevents.1649805147.ip-172-31-29-62')
plt.plot(li)
plt.show()
plt.close()
