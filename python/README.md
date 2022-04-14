# MCAV Python Tutorial

MCAV Python training tutorial

## Video
Please see the video for the full tutorial. TODO

### Quickstart

1. Install Miniconda 
    
    https://docs.conda.io/en/latest/miniconda.html

2. Create an tutorial enviornment

```
$ conda create -n mcav_tutorial python=3.6 numpy pip matplotlib
```

3. Activate your anaconda environment

```
$ conda activate mcav_tutorial
```

4. Run Jupyter Notebook

```
$ jupyter notebook 
```

Navigate to MCAV_Python_Training.ipynb and follow the instructions.

## Local Installation and Setup

The following section should help you get setup with Python and libraries on you own computer. 

### Python

Mac and Linux should already come with Python. You can check if you have Python (and which version) installed by opening a terminal and entering:

```
$ python --version
```

which should return something like: 
```
Python 3.5.3
```

> If it says something like ```Python 2.X.Y```. Try entering the following instead:

```
$ python3 --version
```

Python 2 is an older, unsupported version of python. A lot of libraries (including ROS) still use Python 2.7, so it is still hanging around. The python3 command will make sure you are running Python 3. 

#### Installation

If the command above returned at least `Python 3.5` you already have python installed and are good to go. 

Otherwise,  follow the installation instructions here: https://www.python.org/downloads/. We want at least Python 3.5.

Once complete enter the following to confirm your installation:

```
$ python --version
```

For more detailed information about getting started with Python, see the [Additional Resources](https://git.infotech.monash.edu/MonashCAV/get-started/wikis/software/Python#additional-resources) section. 

## Anaconda

Anaconda is a package and environment manager for python. Anaconda: 
* Makes it easy to install and manage python libraries
* Pre-installs the most commonly used libraries (numpy, matplotlib, etc)
* Allows you to have different environments on the one machine (different versions of the same package).  

#### Installation
To install Anaconda, follow the instructions for your system here: https://www.anaconda.com/distribution/

#### Getting Started
The following are some guides for Anaconda:
* [Getting started with Anaconda](https://docs.anaconda.com/anaconda/user-guide/getting-started/)
* [Anaconda Navigator](https://docs.anaconda.com/anaconda/navigator/)
* [Getting started with conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)

## PIP (Python Installer Package)

You should be able to primarily use Anaconda for package management. However, some packages aren't available with anaconda, or there might be times you can't use anaconda. 

pip is python's package manager, which comes installed with Python. Just like conda, you can use pip to install and manage python packages (libraries). However, pip and conda can sometimes clash so try to use anaconda first if you can. 

You can learn more about pip here: [What is PIP?](https://realpython.com/what-is-pip/)

## Additional Resources

### Learn Python
The following are full python tutorials. If you are new to programming or Python, the first is a good place to start. If you have more experience you might prefer the second. 
* [Basic Python Tutorial](https://www.learnpython.org/)
* [Advanced Python Tutorials](https://realpython.com/start-here/)

### Useful Libraries

The following are some additional resources related to Python and some common libraries. Anaconda should install all of these libraries automatically (excluding opencv, and pytorch). 

It is not recommended that you try to read through all this to try to learn. If you get stuck with a project, these resources might be a good place to start. 

#### NumPy 
High performance, multidimensional array object and computing
* [Numpy Documentation](https://numpy.org/devdocs/reference/index.html)
* [Stanford CS231n: Python Numpy Tutorial](http://cs231n.github.io/python-numpy-tutorial/)

#### Matplotlib
Python plotting library
* [Matplotib Documentation](https://matplotlib.org/contents.html)
* [Matplotib Guide](https://realpython.com/python-matplotlib-guide/)

#### Jupyter Notebook
Notebook style IDE. Very popular for Data Science.
* [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/en/stable/)

#### Python Image Library, PILLOW (PIL)
Basic python image processing library.
* [PIL Overview](https://pillow.readthedocs.io/en/3.0.x/handbook/overview.html)
* [PIL Tutorial](https://pillow.readthedocs.io/en/3.0.x/handbook/tutorial.html)

#### OpenCV (Open Source Computer Vision)
A more advanced python computer vision library. Available in a number of different languages. Can be painful to install.
* [OpenCV Documentation](https://docs.opencv.org/3.4/)

#### Scikit Learn (sklearn)
Classical statistics and machine learning library. Very popular for classic machine learning algorithms. 
* [Scikit-Learn Documentation](https://scikit-learn.org/stable/)

#### Pandas 
Open source data structure and data analysis library. Great for tabular and time-series data.

* [Pandas Website](https://pandas.pydata.org/)

#### PyTorch
Deep Learning library. 
* [PyTorch Tutorials](https://pytorch.org/tutorials/)
* [PyTorch Cheat Sheet](https://pytorch.org/tutorials/beginner/ptcheat.html)