'''
Factory for importing different components of the MOBO framework by name.
'''

from autooed.mobo.surrogate_model import *
from autooed.mobo.acquisition import *
from autooed.mobo.solver import *
from autooed.mobo.selection import *


def get_surrogate_model(name):

    surrogate_model_map = {
        'gp': GaussianProcess,
        'nn': NeuralNetwork,
        'bnn': BayesianNeuralNetwork,
    }

    if name in surrogate_model_map:
        return surrogate_model_map[name]
    else:
        raise Exception(f'Undefined surrogate model {name}')


def get_acquisition(name):

    acquisition_map = {
        'ei': ExpectedImprovement,
        'identity': Identity,
        'pi': ProbabilityOfImprovement,
        'ts': ThompsonSampling,
        'ucb': UpperConfidenceBound,
    }

    if name in acquisition_map:
        return acquisition_map[name]
    else:
        raise Exception(f'Undefined acquisition function {name}')


def get_solver(name):

    solver_map = {
        'nsga2': NSGA2,
        'moead': MOEAD,
        'parego': ParEGO,
        'discovery': ParetoDiscovery,
    }

    if name in solver_map:
        return solver_map[name]
    else:
        raise Exception(f'Undefined solver {name}')


def get_selection(name):

    selection_map = {
        'direct': Direct,
        'hvi': HypervolumeImprovement,
        'random': Random,
        'uncertainty': Uncertainty,
    }

    if name in selection_map:
        return selection_map[name]
    else:
        raise Exception(f'Undefined selection {name}')


def init_surrogate_model(name, params, problem):
    '''
    Initialize surrogate model.
    '''
    surrogate_model_cls = get_surrogate_model(name)
    surrogate_model = surrogate_model_cls(problem, **params)
    return surrogate_model


def init_acquisition(name, params, surrogate_model):
    '''
    Initialize acquisition function.
    '''
    acquisition_cls = get_acquisition(name)
    acquisition = acquisition_cls(surrogate_model, **params)
    return acquisition


def init_solver(name, params, problem, acquisition):
    '''
    Initialize multi-objective solver.
    '''
    solver_cls = get_solver(name)
    solver = solver_cls(problem, acquisition, **params)
    return solver


def init_selection(name, params, surrogate_model):
    '''
    Initialize selection method.
    '''
    selection_cls = get_selection(name)
    selection = selection_cls(surrogate_model, **params)
    return selection
