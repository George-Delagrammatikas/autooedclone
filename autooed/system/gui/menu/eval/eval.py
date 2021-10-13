from autooed.system.gui.menu.eval.start_eval import StartEvalController
from autooed.system.gui.menu.eval.stop_eval import StopEvalController


class MenuEvalView:

    def __init__(self, root_view):
        self.root_view = root_view
        self.root = self.root_view.root


class MenuEvalController:

    def __init__(self, root_controller):
        self.root_controller = root_controller
        self.root_view = self.root_controller.view

        self.agent = self.root_controller.agent
        self.scheduler = self.root_controller.scheduler

        self.view = MenuEvalView(self.root_view)

    def get_table(self):
        '''
        Get table of database
        '''
        return self.root_controller.controller['viz_database'].table

    def start_eval(self):
        '''
        Manually start local evaluation workers for certain rows (TODO: disable when no eval program linked)
        '''
        StartEvalController(self)

    def stop_eval(self):
        '''
        Manually stop evaluation workers for certain rows (TODO: disable when no eval program linked)
        '''
        StopEvalController(self)

    def get_problem_cfg(self):
        return self.root_controller.get_problem_cfg()

    def get_config(self):
        return self.root_controller.get_config()