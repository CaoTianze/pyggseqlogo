# Pyggseqlogo
Python version of [ggseqlogo](https://github.com/omarwagih/ggseqlogo). Based on [plotnine](https://pypi.org/project/plotnine/) (Python version of ggplot2). A derivative of [plotnineSeqSuite](https://pypi.org/project/plotnineseqsuite/).
## Installation
`pip install pyggseqlogo`
## Getting Started
```Python
from plotnine import ggplot
from plotnineseqsuite import geom_logo
from plotnineseqsuite.data import seqs_dna
from pyggseqlogo import ggseqlogo, theme_logo
# The code is based on plotnineSeqSuite.
ggplot() + geom_logo(data=seqs_dna['MA0001.1']) + theme_logo()
```
![https://caotianze.github.io/pyggseqlogo/started_1.png](https://caotianze.github.io/pyggseqlogo/started_1.png)
```Python
# Pyggseqlogo provides a wrapper function for the above code.
ggseqlogo(seqs_dna['MA0001.1'])
```
![https://caotianze.github.io/pyggseqlogo/started_2.png](https://caotianze.github.io/pyggseqlogo/started_2.png)
```Python
# facet_wrap
ggseqlogo(seqs_dna, ncol=4)
```
![https://caotianze.github.io/pyggseqlogo/started_3.png](https://caotianze.github.io/pyggseqlogo/started_3.png)