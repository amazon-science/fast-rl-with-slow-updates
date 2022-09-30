import numpy as np
import pickle as pkl
import matplotlib.pyplot as plt
EPS = 1e-10

# set human performance
human = dict()
# human['airraid'] = None
# human['alien'] = 7127.7
# human['amidar'] = 1719.5
# human['assault'] = 742.0
# human['asterix'] = 8503.3
# human['asteroids'] = 47388.7
# human['atlantis'] = 29028.1
# human['bankheist'] = 753.1
# human['battlezone'] = 37187.5
# human['beamrider'] = 16926.5
# human['berzerk'] = 2630.4
# human['bowling'] = 160.7
# human['boxing'] = 12.1
# human['breakout'] = 30.5
# human['carnival'] = None
# human['choppercommand'] = 7387.8
# human['crazyclimber'] = 35829.4
# human['demonattack'] = 1971.0
# human['enduro'] = 860.5
# human['fishingderby'] = -38.7
# human['freeway'] = 29.6
# human['frostbite'] = 4334.7
# human['gopher'] = 2412.5
# human['gravitar'] = 3351.4
# human['hero'] = 30826.4
# human['icehockey'] = 0.9
# human['jamesbond'] = 302.8
# human['journeyescape'] = None
# human['kangaroo'] = 3035.0
# human['krull'] = 2665.5
# human['kungfumaster'] = 22736.3
# human['montezumarevenge'] = 4753.3
# human['mspacman'] = 6951.6
# human['namethisgame'] = 8049.0
# human['phoenix'] = 7242.6
# human['pitfall'] = 6463.7
# human['pong'] = 14.6
# human['pooyan'] = None
# human['privateeye'] = 69571.3
# human['qbert'] = 13455.0
# human['riverraid'] = 17118.0
# human['roadrunner'] = 7845.0
# human['robotank'] = 11.9
# human['seaquest'] = 42054.7
# human['solaris'] = 12326.7
# human['spaceinvaders'] = 1668.7
# human['stargunner'] = 10250.0
# human['timepilot'] = 5229.2
# human['tutankham'] = 167.6
# human['upndown'] = 11693.2
# human['venture'] = 1187.5
# human['videopinball'] = 17667.9
# human['wizardofwor'] = 4756.5
# human['yarsrevenge'] = 54576.9
# human['zaxxon'] = 9173.3

human['airraid'] = None
human['alien'] = 6875.40
human['amidar'] = 1675.80
human['assault'] = 1496.40
human['asterix'] = 8503.30
human['asteroids'] = 13156.70
human['atlantis'] = 29028.1
human['bankheist'] = 734.40
human['battlezone'] = 37800.00
human['beamrider'] = 5774.70
human['berzerk'] = 2630.4
human['bowling'] = 154.80
human['boxing'] = 4.30
human['breakout'] = 31.80
human['carnival'] = None
human['choppercommand'] = 9881.80
human['crazyclimber'] = 35410.50
human['demonattack'] = 3401.30
human['enduro'] = 309.60
human['fishingderby'] = 5.50
human['freeway'] = 29.6
human['frostbite'] = 4334.7
human['gopher'] = 2321.00
human['gravitar'] = 2672.00
human['hero'] = 25762.50
human['icehockey'] = 0.9
human['jamesbond'] = 406.70
human['journeyescape'] = None
human['kangaroo'] = 3035.0
human['krull'] = 2394.60
human['kungfumaster'] = 22736.3
human['montezumarevenge'] = 4366.70
human['mspacman'] = 15693.40
human['namethisgame'] = 4076.20
human['phoenix'] = 7242.6
human['pitfall'] = 6463.7
human['pong'] = 9.30
human['pooyan'] = None
human['privateeye'] = 69571.3
human['qbert'] = 13455.0
human['riverraid'] = 13513.30
human['roadrunner'] = 7845.0
human['robotank'] = 11.9
human['seaquest'] = 20181.80
human['solaris'] = 12326.7
human['spaceinvaders'] = 1652.30
human['stargunner'] = 10250.0
human['timepilot'] = 5229.2
human['tutankham'] = 167.6
human['upndown'] = 9082.00
human['venture'] = 1187.5
human['videopinball'] = 17297.60
human['wizardofwor'] = 4756.5
human['yarsrevenge'] = 54576.9
human['zaxxon'] = 9173.3



random = dict()
random['airraid'] = None
random['alien'] = 227.8
random['amidar'] = 5.8
random['assault'] = 222.4
random['asterix'] = 210
random['asteroids'] = 719
random['atlantis'] = 12850
random['bankheist'] = 14.1
random['battlezone'] = 2360
random['beamrider'] = 363.9
random['berzerk'] = 123.7
random['bowling'] = 23.1
random['boxing'] = 0.1
random['breakout'] = 1.7
random['carnival'] = None
random['choppercommand'] = 811
random['crazyclimber'] = 10780
random['demonattack'] = 152.1
random['enduro'] = 0
random['fishingderby'] = -91.7
random['freeway'] = 0
random['frostbite'] = 65.2
random['gopher'] = 257.6
random['gravitar'] = 173
random['hero'] = 1027
random['icehockey'] = -11.2
random['jamesbond'] = 29
random['journeyescape'] = None
random['kangaroo'] = 52
random['krull'] = 1598
random['kungfumaster'] = 258
random['montezumarevenge'] = 0
random['mspacman'] = 307.3
random['namethisgame'] = 2292.3
random['phoenix'] = 761.4
random['pitfall'] = -229
random['pong'] = -20.7
random['pooyan'] = None
random['privateeye'] = 24.9
random['qbert'] = 163.9
random['riverraid'] = 1338
random['roadrunner'] = 11.5
random['robotank'] = 2.2
random['seaquest'] = 68.4
random['solaris'] = 1236
random['spaceinvaders'] = 148
random['stargunner'] = 664
random['timepilot'] = 3568
random['tutankham'] = 11.4
random['upndown'] = 533.4
random['venture'] = 0
random['videopinball'] = 16256.9
random['wizardofwor'] = 563.5
random['yarsrevenge'] = 3092.9
random['zaxxon'] = 32.5

# load data
with open('./rainbow_results.pkl', 'rb') as handle:
    result_dict = pkl.load(handle)

# init figure size
fig = plt.figure(figsize=(22, 8), dpi=80)
fig.subplots_adjust(bottom=0.35)
fig.subplots_adjust(top=0.95)
fig.subplots_adjust(left=0.075)
fig.subplots_adjust(right=0.925)


# for each task
num_final_episodes = 5
perform_ratio = []
task_name_list = []
for task_name in result_dict:
    baseline = result_dict[task_name]['rainbow'][0.0][-num_final_episodes:].mean()
    prox_itr = result_dict[task_name]['rainbow'][0.050][-num_final_episodes:].mean()
    rand_val = min(result_dict[task_name]['rainbow'][0.0].min(), result_dict[task_name]['rainbow'][0.050].min())
    human_val = baseline if human[task_name.lower()] is None else human[task_name.lower()]

    max_val = max(baseline, human_val) if prox_itr >= baseline else max(prox_itr, human_val)
    perform_ratio.append(100 * (prox_itr - baseline) / (max_val - rand_val + EPS))
    task_name_list.append(task_name)

# rearrange
perform_ratio = np.array(perform_ratio)
perform_ratio_sign = np.sign(perform_ratio)
perform_ratio = perform_ratio * perform_ratio_sign
perform_ratio = np.log10(perform_ratio + EPS)
perform_ratio = perform_ratio * perform_ratio_sign

perform_ratio = sorted(zip(perform_ratio, task_name_list))
perform_ratio = zip(*perform_ratio)
perform_ratio, task_name_list = [list(a) for a in perform_ratio]

for index, y in enumerate(perform_ratio):
    if y > 0:
        break
neg_perform_ratio = perform_ratio[0:index]
neg_task_name_list = task_name_list[0:index]
print(neg_perform_ratio)
pos_perform_ratio = perform_ratio[index:]
pos_task_name_list = task_name_list[index:]
print(pos_perform_ratio)
plt.bar(neg_task_name_list, neg_perform_ratio, lw=4, color='green', alpha=0.4, edgecolor='black')#, hatch='/')
plt.bar(pos_task_name_list, pos_perform_ratio, lw=4, color='orange',  alpha=0.4, edgecolor='black')#, hatch='.')

plt.xticks(rotation=85, fontsize=16)
plt.yticks([-np.log10(50), -np.log10(10), 0, np.log10(10), np.log10(100), np.log10(3000)], ['- 50%', '- 10%', '0%', '+ 10%', '+ 100%', '+ 3000%'], fontsize=24)
plt.tick_params(axis='y', which='both', left=True, right=True, labelleft=True, labelright=True)
plt.ylim([-np.log10(50) - 0.1, np.log10(3000) + 0.1]) # <---this
for x in [-np.log10(50), -np.log10(10), 0, np.log10(10), np.log10(100), np.log10(3000)]:
    plt.plot(range(len(task_name_list)), len(task_name_list) * [x], '-.', color='gray')
plt.box(False)
plt.savefig("rainbow_vs_rainbowPro.pdf")
plt.show()
plt.close()

