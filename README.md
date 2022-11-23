# Fast RL with Slow Updates

### Introduction

This is the official repository for our paper "Faster deep reinforcement learning with slower online network", which we presented at NeurIPS 2022. We built on the [Dopamine](https://github.com/google/dopamine), which is a research framework for fast prototyping of reinforcement learning algorithms.

We make minimal changes to the standard DQN and Rainbow algorithms. Please see `./dopamine/agents/dqn/dqn_agent.py`. Argument `mu` is defined to activate our Proximal Iteration.
If `mu > 0.0', then Proximal Iteration is being used, and otherwise the model is trained without it, meaning we are implementing regular DQN/Rainbow.


### Prerequisites

Dopamine supports Atari environments and Mujoco environments. Install the
environments you intend to use before you install Dopamine:

**Atari**

1. Install the atari roms following the instructions from
[atari-py](https://github.com/openai/atari-py#roms).
2. `pip install ale-py` (we recommend using a [virtual environment](virtualenv)):
3. `unzip $ROM_DIR/ROMS.zip -d $ROM_DIR && ale-import-roms $ROM_DIR/ROMS`
(replace $ROM_DIR with the directory you extracted the ROMs to).

### Installing from Source


The most common way to use Dopamine is to install it from source and modify
the source code directly:

```
git clone https://github.com/google/dopamine
```

After cloning, install dependencies:

```
pip install -r dopamine/requirements.txt
```

Dopamine supports tensorflow (legacy) and jax (actively maintained) agents.
View the [Tensorflow documentation](https://www.tensorflow.org/install) for
more information on installing tensorflow.

Note: We recommend using a [virtual environment](virtualenv) when working with Dopamine.

### Installing with Pip

Note: We strongly recommend installing from source for most users.

Installing with pip is simple, but Dopamine is designed to be modified
directly. We recommend installing from source for writing your own experiments.

```
pip install dopamine-rl
```

### Running tests

You can test whether the installation was successful by running the following
from the dopamine root directory.

```
export PYTHONPATH=$PYTHONPATH:$PWD
python -m tests.dopamine.atari_init_test
```


