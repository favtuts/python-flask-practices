# Developing RESTful APIs with Python and Flask

Let's learn how to develop RESTful APIs with Python and Flask.


# Bootstrapping a Flask Application

We will need to install [Python 3](https://docs.python.org/3/), [Pip (Python Package Index)](https://pypi.python.org/pypi/pip), and [Flask](http://flask.pocoo.org/).

## Installing Python 3

```sh
$ pyenv versions
$ pyenv install --list
$ pyenv install 3.8.19
$ pyenv global 3.8.19
$ python --version
Python 3.8.19
$ python3 --version
Python 3.8.19
```

## Installing Pip

```sh
$ pip --version
pip 23.0.1 from /home/tvt/.pyenv/versions/3.8.19/lib/python3.8/site-packages/pip (python 3.8)
```

You can make sure that pip is up-to-date by running:
```sh
$ python3 -m pip install --upgrade pip
$ python3 -m pip --version
pip 24.1.2 from /home/tvt/.pyenv/versions/3.8.19/lib/python3.8/site-packages/pip (python 3.8)
```