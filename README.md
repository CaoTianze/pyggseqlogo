# Pyggseqlogo
Python version of [ggseqlogo](https://github.com/omarwagih/ggseqlogo). Based on [plotnine](https://github.com/has2k1/plotnine/) (Python version of ggplot2). A derivative of [plotnineSeqSuite](https://github.com/caotianze/plotnineseqsuite/).
## Cite this work
Cao, T., Li, Q., Huang, Y. et al. plotnineSeqSuite: a Python package for visualizing sequence data using ggplot2 style. BMC Genomics 24, 585 (2023). https://doi.org/10.1186/s12864-023-09677-8
## Installation
`pip install pyggseqlogo`
## Getting Started
```Python
from plotnine import ggplot
from plotnineseqsuite import geom_logo
from plotnineseqsuite.data import seqs_dna
from pyggseqlogo import ggseqlogo, theme_logo
```
The code is based on plotnineSeqSuite.
```Python
ggplot() + geom_logo(data=seqs_dna['MA0001.1']) + theme_logo()
```
![https://caotianze.github.io/pyggseqlogo/started_1.png](https://caotianze.github.io/pyggseqlogo/started_1.png)    
Pyggseqlogo provides a wrapper function for the above code.
```Python
ggseqlogo(seqs_dna['MA0001.1'])
```
![https://caotianze.github.io/pyggseqlogo/started_2.png](https://caotianze.github.io/pyggseqlogo/started_2.png)    
facet_wrap
```Python
ggseqlogo(seqs_dna, ncol=4)
```
![https://caotianze.github.io/pyggseqlogo/started_3.png](https://caotianze.github.io/pyggseqlogo/started_3.png)
## Where to go next
If you want to draw more complex sequence logos or other sequence-related diagrams, we recommend visiting the [plotnineSeqSuite homepage](https://github.com/caotianze/plotnineseqsuite/) for details.