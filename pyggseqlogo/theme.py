from plotnine import theme_minimal, theme, element_blank, element_rect


class theme_logo:
    def __init__(self,base_size=12, base_family=''):
        self.base_size = base_size
        self.base_family = base_family

    def __radd__(self, gg):
        gg = gg + theme_minimal(base_size=self.base_size, base_family=self.base_family) + theme(panel_grid=element_blank(),
                                                          plot_background=element_rect(fill='white',color='white'),
                                                          legend_position='bottom')
        return gg