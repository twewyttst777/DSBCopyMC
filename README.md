# DSBCopyMC
Python Program for Monte Carlo Simulation of Potential DSB Insertion via Polymerase Capable of Random versus Templated Mechanism.

## Purpose

We are interested in whether the DNA polymerases that help repair double-strand breaks (DSBs) can copy the sequence at the DSB. We are interested in if the polymerase can copy up to 4 nucleotides (nt) from the bottom strand at the DSB and ligate that short length to the top strand of that same DSB, such that the copy, when moved to the top strand, would be the reverse complement of the sequence on the top strand (the templating sequence) that had served as the template for this event.

A success is defined as the insertion at the break matching the reverse complement of a string of NT bases upstream or downstream, offset by a set amount (default 2). The user submits a csv containing the sequence around the break, and the program runs a Monte-Carlo simulation to determine if the observed results are significant.

# Usage
Requires a seq.csv file with the format:  

>before,ins,after  
>AATTAC,TCA,ACATGG

Where before and after are the positions upstream and downstream of the break, respectively.

Modify config.py and execute command
  `python3 main.py`
To output a graph.

## config.py
Contains settings for the simulation. These are:

  MAXIMUM_OFFSET: Maximum offset to search for copy
  
  TRIALS: Total number of trials to run
  
  WEIGHTS: Weight of each base to set randomness

  TITLE: Title labeled on the graph
  
  ----------------------------------------------------
  
  FILENAME: Filename of output graph
  
  COMP_POINT: The point of comparison of success, that is, the number of successes observed in the actual data contained in seq.csv
  
  AUTO_COMP: If True, overrides COMP_POINT to determine the comparison point automatically. Set to False if you do not want this.
