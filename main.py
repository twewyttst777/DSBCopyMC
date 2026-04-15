import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from config import *
from random import choices

def random_word(length, weight = WEIGHTS):
    pop = ['A', 'G', 'C', 'T']
    word = ""
    for x in range(length):
        word += choices(pop, weight)[0]
    return word

def complement(word):
    old = "ATGC"
    new = "TACG"

    tab = str.maketrans(old, new)
    return(word.translate(tab))

def contains(var, cp):
    largest = 0
    offset = 0
    for x in range(len(var)):
        for y in range(MAXIMUM_OFFSET, -1, -1): 
            if var[:x+1] == cp[y:x+1+y]:
                largest = x+1
                offset = y
    return largest

def p_v(observed, n):
    return str(sum(1 for x in observed if x < n)/len(observed)*100) 

def graph(observed_list, title, filename, loc):

    fig, ax = plt.subplots()
    ax.hist(observed_list)
    plt.title(title)
    ax.annotate(str(loc) + ', >' + p_v(observed_list, loc) + '%', xy=(loc,0), xytext=(loc,10000), arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
    plt.xlabel('Occurrences')
    plt.ylabel('Number of Trials')
    plt.savefig(filename)

def search(df):
    return df.query("downstream > 1 or upstream > 1")


def simulate(df):
    df['sim'] =  [complement(random_word(len(i))) for i in df['ins']]
    df['downstream'] = [contains(u[::-1], i) for u, i in zip(df['sim'], df['aft_comp'])]
    df['upstream'] = [contains(u, i) for u, i in zip(df['sim'], df['bef_comp'])]
    return search(df).shape[0] 

if __name__ == '__main__':
    df = pd.read_csv('seq.csv')

    #Ensures parity with Excel files
    df.index += 3

    df['rev_ins'] = [u[::-1] for u in df['ins']]
    df['bef_seq'] = [u[::-1] for u, i in zip(df['before'], df['ins'])]
    df['aft_seq'] = [str(u) for u, i in zip(df['after'], df['ins'])]
    df['bef_comp'] = [complement(i) for i in df['bef_seq']]
    df['aft_comp'] = [complement(i) for i in df['aft_seq']]

    df['downstream'] = [contains(u, i) for u, i in zip(df['rev_ins'], df['aft_comp'])]
    df['upstream'] = [contains(u, i) for u, i in zip(df['ins'], df['bef_comp'])]

    print(search(df))

    if AUTO_COMP:
        comp_point = search(df).shape[0]
    else:
        comp_point = COMP_POINT

    observed_list = []

    for x in range(TRIALS):
        observed_list.append(simulate(df))
        if x % 1000 == 0:
            print(x)

    pd.DataFrame(observed_list).to_csv('observed_values.csv', index=False)

    graph(observed_list, TITLE, FILENAME, comp_point) 
