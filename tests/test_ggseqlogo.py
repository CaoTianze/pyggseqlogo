from plotnine import ggplot
from plotnineseqsuite import geom_logo
from plotnineseqsuite.data import seqs_dna
from pyggseqlogo import ggseqlogo, theme_logo

ggseqlogo(seqs_dna['MA0001.1'])
ggplot() + geom_logo(data=seqs_dna['MA0001.1']) + theme_logo()
ggseqlogo(seqs_dna, ncol=4)
