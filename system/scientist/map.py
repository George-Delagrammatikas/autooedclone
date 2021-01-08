config_map = {
    'general': {
        'n_worker': 'Max number of evaluation workers',
        'batch_size': 'Batch size',
        'n_iter': 'Number of iterations',
    },
    'problem': {
        'name': 'Name of problem',
        'n_var': 'Number of design variables',
        'n_obj': 'Number of objectives',
        'n_constr': 'Number of constraints',
        'performance_eval': 'Performance evaluation script',
        'constraint_eval': 'Constraint evaluation script',
        'minimize': 'Minimize',
        'var_lb': 'Lower bound',
        'var_ub': 'Upper bound',
        'obj_lb': 'Lower bound',
        'obj_ub': 'Upper bound',
        'var_name': 'Names',
        'obj_name': 'Names',
        'ref_point': 'Reference point',
        'n_init_sample': 'Number of random initial samples',
        'init_sample_path': 'Path of provided initial samples',
    },
    'algorithm': {
        'name': 'Name of algorithm',
        'n_process': 'Number of parallel processes to use',
    },
}

algo_config_map = {
    'surrogate': {
        'name': 'Name',
        'nu': 'Type of Matern kernel',
        'n_spectral_pts': 'Number of points for spectral sampling',
        'mean_sample': 'Use mean sample for Thompson sampling',
        'hidden_sizes': 'Size of hidden layers',
        'activation': 'Activation',
        'lr': 'Learning rate',
        'weight_decay': 'Weight decay',
        'n_epoch': 'Number of training epoch',
    },
    'acquisition': {
        'name': 'Name',
    },
    'solver': {
        'name': 'Name',
        'n_gen': 'Number of generations',
        'pop_size': 'Population size',
        'pop_init_method': 'Population initialization method',
    },
    'selection': {
        'name': 'Name',
    },
}

algo_value_map = {
    'surrogate': {
        'name': {
            'gp': 'Gaussian Process',
            'ts': 'Thompson Sampling',
            'nn': 'Neural Network',
        },
    },
    'acquisition': {
        'name': {
            'identity': 'Identity',
            'pi': 'Probability of Improvement',
            'ei': 'Expected Improvement',
            'ucb': 'Upper Confidence Bound',
            'lcb': 'Lower Confidence Bound',
        },
    },
    'solver': {
        'name': {
            'nsga2': 'NSGA-II',
            'moead': 'MOEA/D',
            'parego': 'ParEGO Solver',
            'discovery': 'Pareto Discovery',
        },
        'pop_init_method': {
            'random': 'Random',
            'nds': 'Non-Dominated Sort',
            'lhs': 'Latin-Hypercube Sampling',
        },
    },
    'selection': {
        'name': {
            'hvi': 'Hypervolume Improvement',
            'uncertainty': 'Uncertainty',
            'random': 'Random',
            'moead': 'MOEA/D-EGO Selection',
            'dgemo': 'DGEMO Selection',
        },
    },
}

algo_value_inv_map = {}
for cfg_type, val_map in algo_value_map.items():
    algo_value_inv_map[cfg_type] = {}
    for key, value_map in val_map.items():
        algo_value_inv_map[cfg_type][key] = {v: k for k, v in value_map.items()}

worker_map = {
    'id': 'ID',
    'name': 'Name',
    'address': 'IP address',
    'description': 'Description',
}