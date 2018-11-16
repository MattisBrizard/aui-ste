# README #
Speech to emotion algorithm (requires an internet connection)

## Usage ##
1. Download the repository

2. Install Python 3.7 from the [official website](https://www.python.org)

3. Install pip (the python package manager) from [here](https://pip.pypa.io/en/stable/installing/)

4. Open system terminal and run:
   ```bash
   cd path/to/the/downloaded/folder
   pip install -r requirements.txt
   ```
5. To add your config, from terminal run:
   ```bash
   cd path/to/the/downloaded/folder
   cp config.py.example config.py
   ```
   Then fill the config.py file with your config

6. To execute the program, from terminal run:
   ```bash
   cd path/to/the/downloaded/folder
   python main.py
   ```

## Change the language ##
You can change the language directly from the code by modifying the "SPEECH_LANG" 
variable in config.py.
The value of such variable must be a string containing an [ISO Language Code](http://www.lingoes.net/en/translator/langcode.htm)
for languages.