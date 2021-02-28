from system.gui.utils.figure import embed_figure
from .view import VizStatsView


class VizStatsController:

    def __init__(self, root_controller):
        self.root_controller = root_controller
        self.root_view = self.root_controller.view

        # set values from root
        self.problem_cfg = self.root_controller.problem_cfg
        self.agent = self.root_controller.agent

        self.view = VizStatsView(self.root_view, self.problem_cfg)

        # connect matplotlib figure with tkinter GUI
        embed_figure(self.view.fig, self.root_view.frame_stat)

        # refresh figure
        self.view.fig.tight_layout()
        self.redraw()

    def redraw(self):
        '''
        Redraw hypervolume and prediction error curves
        '''
        hypervolume = self.agent.load_hypervolume()
        model_error = self.agent.load_model_error()
        n_init_sample = self.agent.get_n_init_sample()

        self.view.redraw(hypervolume, model_error, n_init_sample)

    def save_hv_figure(self, path, title=None):
        self.view.save_hv_figure(path, title=title)

    def save_error_figure(self, path, title=None):
        self.view.save_error_figure(path, title=title)