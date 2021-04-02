<img width="400" src="docs/source/_static/logo.png">

![Platform](https://img.shields.io/badge/platform-windows|macos|linux-lightgrey) [![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE) 

**[Paper (coming soon)]() | [Website (coming soon)]() | [Documentation]() | [Contact](mailto:autooed-help@csail.mit.edu)**

AutoOED is an optimal experiment design platform powered with automated machine learning to accelerate the discovery of optimal solutions. Our platform solves multi-objective optimization problems and automatically guides the design of experiment to be evaluated. AutoOED is developed by [Yunsheng Tian](https://www.yunshengtian.com/), [Mina Konaković Luković](http://people.csail.mit.edu/mina/), [Timothy Erps](https://www.linkedin.com/in/timothy-erps-15622a49/), [Michael Foshey](https://www.linkedin.com/in/michael-foshey/) and [Wojciech Matusik](https://cdfg.mit.edu/wojciech) from [Computational Design & Fabrication Group](https://cdfg.mit.edu/) at [MIT Computer Science and Artificial Intelligence Laboratory](https://www.csail.mit.edu/).

## Overview

AutoOED is a powerful and easy-to-use tool written in Python for design parameter optimization with multiple objectives, which can be used for any kind of experiment settings (chemistry, material, physics, engineering, computer science…). AutoOED aims at improving the sample efficiency of optimization problems, i.e., using less number of samples to achieve the best performance, by applying state-of-the-art machine learning approaches, which is most powerful when the performance evaluation of your problem is expensive (for example, in terms of time or money). 

One of the most important features of AutoOED is an intuitive graphical user interface (GUI), which is provided to visualize and guide the experiments for users with little or no experience with coding, machine learning, or optimization. Furthermore, a distributed system is integrated to enable parallelized experimental evaluations either by multiple processes on a single computer or by independent technicians in remote locations.

<p>
   	<img width="49%" src="docs/source/_static/manual-personal/run-optimization/auto_control.png">
    <img width="49%" src="docs/source/_static/manual-personal/database/database.png">
</p>

## Installation

AutoOED can be installed either directly from the links to the executable files, or from source code. Source code is the most up-to-date version, while executable files are relatively stable. AutoOED generally works across all Windows/MacOS/Linux operating systems.

### Executable files

Please see the instructions for directly installing executable files in our documentation.

### Source code

Install by conda with pip:

```
conda env create -f environment.yml
conda activate autooed
pip install pymoo==0.4.1 pygco==0.0.16
```

Or install purely by pip:

```
pip install -r requirements.txt
pip install pymoo==0.4.1 pygco==0.0.16
```

*Note: We recommend to install with Python 3.7, because we have not tested on other versions. If you cannot properly run the programs after installation, please check if the version of these packages match our specifications.*

## Getting Started

After installing from source code, please run the following commands to start AutoOED for different versions respectively.

### Personal Version

The personal version of AutoOED has all the supported features except distributed collaboration. This version is cleaner and easier to work with, especially when the optimization and evaluation can be done on a single computer.

```bash
python run_personal.py
```

### Team Version

The team version enables distributed collaboration around the globe by leveraging a centralized MySQL database that can be connected through the Internet. Using this version, the scientist can focus on controlling the optimization and data analysis, while the technicians can evaluate in a distributed fashion and synchronize the evaluated results with other members of the team in real-time, through our provided simple and intuitive user interface. This version provides different software for different roles of a team (manager, scientist, and technician) with proper privilege control implemented. Below are the scripts for different roles respectively:

```bash
python run_team_manager.py
python run_team_scientist.py
python run_team_technician.py
```

For more detailed usage and information of AutoOED, please checkout our documentation.

## Citation

If you find our work helpful to your research, please consider citing our paper (coming soon).

## Contributing

We highly welcome all kinds of contributions, including but not limited to bug fixes, new feature suggestions, more intuitive error messages, and so on.

Especially, [the algorithmic part](https://github.com/yunshengtian/AutoOED/tree/master/algorithm/mobo) of our code repository is written in a clean and modular way, facilitating extensions and tailoring the code, serving as a testbed for machine learning researchers to easily develop and evaluate their own multi-objective Bayesian optimization algorithms. We are looking forward to supporting more powerful optimization algorithms on our platform.

## Contact

If you experience any issues during installing or using the software, or if you want to contribute to AutoOED, please feel free to reach out to us either by creating issues on GitHub or sending emails to autooed-help@csail.mit.edu.