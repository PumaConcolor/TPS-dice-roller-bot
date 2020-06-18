import math

from random import randint
from iteration_utilities import flatten

from .parse import *

### roll(dice, number, mod)
# takes three values, corresponding to: number of sides of the die, number of dice,
# modifier to the roll, returns the tuple (result, result_list)

def roll(dice, number, mod, single_result_mode=False):
    if number > 100:
       raise Exception('Too many dice. Max allowed is 100')
    else:
        result_list = []
        for i in range(0, abs(number)):
            result_list.append(randint(1, abs(dice)))
        if single_result_mode:
            result = sum(result_list) + mod
        else:
            result = (sum(result_list) + mod, result_list)
    return result


### score_roll()
# returns a list of ability scores

def score_roll():
    score_list = []
    dice = 6
    number = 4
    mod = 0
    for i in range(0, 6):
        score_result_tmp = []
        tmp_result, tmp_result_list = roll(dice, number, mod)
        score_result_tmp.append(tmp_result_list)
        score_result = remove_minimum(score_result_tmp)
        score_list.append(score_result)
    return_list = [sum(scores) for scores in score_list]
    return return_list


### roll_penis(mod)
# rolls a d20 to decide the penis_size of a pc

def roll_penis(mod):
    die = roll(20, 1, 0, True)
    if die == 20:
        result = (die, 'mandingo')
    elif die == 1:
        result = (die, 'micropenis')
    else:
        result = (die, 10 + math.log2(die) + mod)
        if result[1] < 6:
            result = (die, 'weird')
    return result


### remove_minimum(input_list)
# removes the minimum element from input_list

def remove_minimum(input_list):
    input_list = list(flatten(input_list))
    input_list.remove(min(input_list))
    return input_list

