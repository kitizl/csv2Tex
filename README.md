# csv2Tex

A CLI python program that converts CSV files into LaTeX tables.

## Download

Clone this repo in whichever way you want.

## Usage
For this program to work properly you will need at least `python3` along with `pandas` installed.

If you don't have `python3` installed, you can get it [here](https://www.python.org/downloads/).

If you don't have pandas installed, you need to follow the following steps:
- Get `pip` from [here](https://pip.pypa.io/en/stable/installing). Instructions vary by OS and preferences.
- Install `pandas` using `pip` from the command line using the command, `pip install pandas`

A much quicker way of getting this done is installing [Anaconda 3](https://www.anaconda.com/download) although mind you, this is a very big file.

For Unix Systems:

```
python3 csv_to_tex.py [filename]
```
For Windows Systems:

```
python csv_to_tex.py [filename]
```

The file (as of this current version) has to be CSV, otherwise everything would go to hell. A future update perhaps might have something that allows for more flexibility in the file options.

You need to install `pandas` for this to work properly.

## TODO
- [] Make an automated dependency installing thingamajig
- [] Include .xls, .ssv, and other data managing filetypes.
