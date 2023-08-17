from plotnine import ggplot, facet_grid, facet_wrap
from plotnineseqsuite import geom_logo
from pyggseqlogo.theme import theme_logo


def ggseqlogo(data, facet='wrap', scales='free_x', ncol=None, nrow=None, **kwargs):
    p = ggplot() + geom_logo(data=data, **kwargs) + theme_logo()
    if type(data) is not dict:
        return p
    if facet != 'grid' and facet != 'wrap':
        raise Exception("facet option must be set to 'wrap' or 'grid'")
    if facet == 'grid':
        p = p + facet_grid('~seq_group', scales=scales)
    elif facet == 'wrap':
        p = p + facet_wrap('~seq_group', scales=scales, nrow=nrow, ncol=ncol)
    return p
