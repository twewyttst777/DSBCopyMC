# Monte Carlo Settings

MAXIMUM_OFFSET = 2
TRIALS = 100000

# Weights are ordered:
# [A, G, C, T]

#First set: "Real" values, aka expected weights given whole human genome.
WEIGHTS = [.295, .205, .205, .295]

#Second set: "Observed" values, weights as observed in our testing. Remove # to enable this line.
#WEIGHTS = [.46, .14, .07, .33]



# Graphing


## Graph title
TITLE = "Events length 2-5, Recessed 0, 1, or 2"
## Filename of graph
FILENAME = "out.pdf"

## Comparison point: the point we are testing against to determine significance. i.e. the number of matches observed in the real sample.
COMP_POINT = "33"

## Calculate comparison point automatically from given data. Overrides COMP_POINT
AUTO_COMP = True

#Internal settings

## Line numbering offset to sync with Excel file numbering. This changes nothing with the data but may make testing easier. 
LINE_OFFSET = 3
