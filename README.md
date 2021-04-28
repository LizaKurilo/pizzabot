# PizzaBot Challenge

The task is to instruct Pizzabot on how to deliver pizzas to all the houses in a neighborhood. 
In more specific terms, given a grid (where each point on the grid is one house) and a list of points representing houses in need of pizza delivery, 
return a list of instructions for getting Pizzabot to those locations and delivering. 

An instruction is one of: N: Move north S: Move south E: Move east W: Move west D: Drop pizza

**Example:** for input 5x5 (1, 3) (4, 4) which means grid with size 5x5, points of deliver: (1,3), (4,4) one of the correct solution would be: ENNNDEEEND

<img src="https://github.com/LizaKurilo/pizzabot/blob/master/assets/example.png" width="300" height="300">


## Files Structure
1. [validation_parse_module.py](https://github.com/LizaKurilo/pizzabot/blob/master/validation_parse_module.py) - python module with input validation and parsing functions
2. [pizzabot_engine.py](https://github.com/LizaKurilo/pizzabot/blob/master/pizzabot_engine.py) - python file with main logic of pizzabot behavior
3. [pizzabot_main.py](https://github.com/LizaKurilo/pizzabot/blob/master/pizzabot_main.py) - python file with __main__ function
4. [tests.py](https://github.com/LizaKurilo/pizzabot/blob/master/tests.py) - python file with unittests
5. [txtfiles](https://github.com/LizaKurilo/pizzabot/tree/master/txtfiles) folder with [test.txt](https://github.com/LizaKurilo/pizzabot/blob/master/txtfiles/test.txt) file which is used when no parameteres is given
6. [requirements.txt](https://github.com/LizaKurilo/pizzabot/blob/master/requirements.txt) file with needed libraries

## Installation Options
1. Make sure you have python3 installed:
    + `$ python --version` \
    or
    + `$ python3 --version`
2. Install with [`pip`](https://pypi.org/project/stronghold/) 
    + `$ pip install -r requirements.txt` 

## Usage
In command line run:
  ```sh
$ python pizzabot_main.py "5x5 (0, 0) (1, 3) (4,4) (4, 2) (4, 2) (0, 1) (3, 2) (2, 3) (4, 1)"
```
Notice, than first argument should contain grid size **seperated by 'x'**, points coordinates should be in round brackets, in which x-coordinate and y-coordinate should be **integer** and **positive** and **seperated by comma** 

If you will not provide parametres it would be read out form [txtfiles/test.txt](https://github.com/LizaKurilo/pizzabot/blob/master/txtfiles/test.txt) 

If your input will not be correct you will have a message with correct example and will be needed to restart the command.

## Tests
In command line run unittests:
  ```sh
$ python tests.py"
```
