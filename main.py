import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from config import *
from random import choices

class Results:
    def __init__(x_total, x_2, x_3, x_4):
       self.total = x_total
       self.sim_2 = x_2
       self.sim_3 = x_3
       self.sim_4 = x_4

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
    plt.xlabel('Occurrences per simulation trial')
    plt.ylabel('Number of Trials where # Occurrences Recorded')
    plt.savefig(filename)

def search(df):
    return df.query("downstream > 1 or upstream > 1").shape[0]
def search2(df, x):
    return df.query("(downstream == {0} and upstream < {0}) or (upstream == {1} and downstream < {1})".format(x, x)).shape[0]

def simulate(df):
    df['sim'] =  [complement(random_word(len(i))) for i in df['ins']]
    df['downstream'] = [contains(u[::-1], i) for u, i in zip(df['sim'], df['dwn_comp'])]
    df['upstream'] = [contains(u, i) for u, i in zip(df['sim'], df['ups_comp'])]
    return [search(df), search2(df, 2), search2(df, 3), search2(df, 4)]

if __name__ == '__main__':
    df = pd.read_csv('seq.csv')
    print(df)

    #Ensures parity with Excel files
    df.index += LINE_OFFSET 

    df['rev_ins'] = [u[::-1] for u in df['ins']]
    df['ups_seq'] = [u[::-1] for u, i in zip(df['upstream'], df['ins'])]
    df['dwn_seq'] = [str(u) for u, i in zip(df['downstream'], df['ins'])]
    df['ups_comp'] = [complement(i) for i in df['ups_seq']]
    df['dwn_comp'] = [complement(i) for i in df['dwn_seq']]

    df['downstream'] = [contains(u, i) for u, i in zip(df['rev_ins'], df['dwn_comp'])]
    df['upstream'] = [contains(u, i) for u, i in zip(df['ins'], df['ups_comp'])]
    
    df.to_csv('test_df.csv')

    print(search(df))
    print(df.query("downstream > 1 or upstream >1"))

    if AUTO_COMP:
        comp_point = search(df)
    else:
        comp_point = COMP_POINT

    observed_list = []
    observed_detailed = []

    for x in range(TRIALS):
        sim = simulate(df)
        observed_list.append(sim[0])
        observed_detailed.append(sim)
        if x % 1000 == 0:
            print(x)

    pd.DataFrame(observed_list).to_csv('observed_values.csv', index=False)
    pd.DataFrame(observed_detailed).to_csv('observed_detailed.csv', index=False)

    graph(observed_list, TITLE, FILENAME, comp_point) 
