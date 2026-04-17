# DSBCopyMC
Python Program for Monte Carlo Simulation of Potential DSB Insertion via Polymerase Capable of Random versus Templated Mechanism.

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
