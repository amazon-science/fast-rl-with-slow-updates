import os
import pickle as pkl
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.xkcd_rgb["pale red"]
current_palette = sns.color_palette("bright", 10)
sns.color_palette()
sns.palplot(sns.color_palette("bright", 10))

# maps
LEGEND_MAP = {0.0: 'Rainbow', 0.05: 'Rainbow Pro'}
COLOR_MAP = {0.0: current_palette[2], 0.05: current_palette[-2]}


def smoothing(data_, smooth=1):
    """
    smooth data with moving window average.
    that is,
        smoothed_y[t] = average(y[t-k], y[t-k+1], ..., y[t+k-1], y[t+k])
    where the "smooth" param is width of that window (2k+1)
    """
    # print(smooth)
    results = np.zeros_like(data_)
    y = np.ones(smooth)
    for i in range(data_.shape[0]):
        x = np.asarray(data_[i])
        z = np.ones(len(x))
        smoothed_x = np.convolve(x, y, 'same') / np.convolve(z, y, 'same')
        results[i] = smoothed_x

    return results


def plot_results(game_results, game_name,
                 standard_error=False,
                 alpha=0.010, fig_name='', title='',
                 legend_map=None, color_map=None,
                 show_legend=True, legend_loc='lower right',
                 xlabel='Training Frames (Million)', ylabel='Average Return',
                 folder_to_save_plots='./figs/', enable_save=False):
    # set palette
    sns.color_palette('colorblind')
    sns.set(style="darkgrid", font_scale=1.5)
    sns.despine()
    fig, axes = plt.subplots(figsize=(7, 6))

    # for each result
    for info, results in game_results.items():
        # size
        num_seeds, num_iters = results.shape
        assert num_seeds == 5
        assert num_iters == 120

        # error over seeds
        if standard_error:
            num_seeds = results.shape[0]
            y_error = np.std(results, 0) / np.sqrt(num_seeds)
        else:
            y_error = np.std(results, 0)

        # mean over seeds
        y_vals = np.mean(results, 0)
        x_vals = np.arange(num_iters) + 1

        # plot mean
        if color_map and info[1] in color_map:
            if legend_map and info[1] in legend_map:
                axes.plot(x_vals, y_vals,  alpha=1,
                          label=legend_map[info[1]], color=color_map[info[1]], linestyle='solid')
            else:
                axes.plot(x_vals, y_vals,  alpha=1,
                          label=info[0] + '_' + info[1])
        else:
            if legend_map and info[1] in legend_map:
                axes.plot(x_vals, y_vals, alpha=1,
                          label=legend_map[info[1]])
            else:
                axes.plot(x_vals, y_vals, alpha=1,
                          label=info[0] + '_' + info[1])

        # plot error
        if color_map and info[1] in color_map:
            axes.fill_between(x_vals, y_vals - y_error, y_vals + y_error,
                              alpha=alpha, color=color_map[info[1]])
        else:
            axes.fill_between(x_vals, y_vals - y_error, y_vals + y_error,
                              alpha=alpha)

    # labels
    axes.set_xlabel(xlabel, fontweight='bold')
    axes.set_ylabel(ylabel, fontweight='bold')

    # plt.xticks(rotation=0)
    # plt.ticklabel_format(style='plain', axis='x')
    # axes.set_xlabel(xlabel, fontweight='bold')
    axes.set_xticks([40, 80, 120])
    labels = [item.get_text() for item in axes.get_xticklabels()]
    labels[0] = 40
    labels[1] = 80
    labels[2] = 120
    axes.set_xticklabels(labels)

    # title
    if len(title) == 0:
        axes.set_title(game_name, fontsize=20, fontweight='bold')
    else:
        axes.set_title(title, fontsize=20, fontweight='bold')

    # ticker
    # axes.ticklabel_format(style='sci', axis='x', scilimits=(0, 0))

    # legend
    if show_legend:
        axes.legend(loc=legend_loc, fontsize='medium', prop={'weight': 'bold'})#, bbox_to_anchor=(1.04, 0.5))

    # font size
    plt.rc('font', size=60)
    plt.rc('axes', titlesize=60)
    plt.rc('axes', labelsize=60)
    plt.rc('legend', fontsize=60)
    plt.rc('figure', titlesize=60)

    fig.tight_layout()
    sns.despine()
    plt.show()

    if len(fig_name) == 0:
        fname = os.path.join(folder_to_save_plots, game_name + ".png")
    else:
        fname = os.path.join(folder_to_save_plots, fig_name + '_' + game_name + ".png")

    if enable_save:
        fig.savefig(fname, bbox_inches='tight', dpi=100)


# fn for plotting
def plot_learning_curve(full_results_dict,
                        legend_loc='upper left',
                        ylabel='Average Return',
                        smooth=5,
                        enable_save=False,
                        alpha=0.1,
                        fig_name='rainbow',
                        folder_to_save_plots='./',
                        title='',
                        ):
    # for each game
    cnt = 0
    for task_name in full_results_dict:

        # for each model
        for model_name in full_results_dict[task_name]:
            task_result_dict = {}
            # for each c
            for c_value in [0.05, 0.0]:
                result_list = []

                # for each seed
                for seed in full_results_dict[task_name][model_name][c_value]:
                    result_list.append(full_results_dict[task_name][model_name][c_value][seed])

                # stack (seeds x iters)
                result_list = np.stack(result_list, 0)
                if smooth > 0.0:
                    result_list = smoothing(result_list, smooth=smooth)
                task_result_dict[(model_name, c_value)] = result_list

            # plotting
            plot_results(game_results=task_result_dict, game_name=task_name,
                         alpha=alpha, fig_name=fig_name, title=title,
                         legend_map=LEGEND_MAP, color_map=COLOR_MAP,
                         show_legend=True if task_name == 'Zaxxon' else False,
                         legend_loc=legend_loc,
                         ylabel=ylabel,
                         folder_to_save_plots=folder_to_save_plots, enable_save=enable_save)
            cnt += 1
        print(cnt)


# load data
with open('./rainbow_results_full.pkl', 'rb') as handle:
    full_results_dict = pkl.load(handle)
plot_learning_curve(full_results_dict=full_results_dict,
                    legend_loc='lower right',
                    smooth=10,
                    enable_save=True,
                    alpha=0.4,
                    folder_to_save_plots='./rainbow_plots')