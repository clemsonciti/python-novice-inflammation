---
layout: page
title: Setup
permalink: /setup/
---

You need to download some files to follow this lesson:

1. After logging into JupyterHub, open a new terminal
1. Type in exactly the following three commands - don't include the dollar sign (`$`)

~~~
$ cd
$ mkdir python-novice-inflammation
$ cd python-novice-inflammation
$ wget https://github.com/clemsonciti/python-workshop/raw/gh-pages/data/python-novice-inflammation-data.zip
$ unzip python-novice-inflammation-data.zip
~~~
{: .source}

If you will be using the Jupyter (IPython) notebook for the lesson,
you should have already
[installed Anaconda](http://swcarpentry.github.io/workshop-template/#setup)
which includes the notebook.

To start the notebook, open a terminal or git bash and type the command:

~~~
$ jupyter notebook
~~~
{: .source}

To start the Python interpreter without the notebook, open a terminal or git bash and type the command:

~~~
$ python
~~~
{: .source}
