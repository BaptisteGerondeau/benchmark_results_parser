#!/usr/bin/env python3

import numpy as np
import yaml

class ResultModel:
    def __init__(self, result_path, benchmark_name, machine_type, toolchain, compiler_flags,
                 run_flags, num_id):
        self.result_path = result_path
        self.benchmark_name = benchmark_name
        self.machine_type = machine_type
        self.toolchain = toolchain
        self.compiler_flags = compiler_flags
        self.run_flags = run_flags
        self.num_id = num_id
        self.iterations = None
        self.fields = []
        self.results_matrix = None

    def _load_result_file(self):
        with open(self.result_path, 'r') as res:
            results_dict = yaml.load(res)

        try:
            self._validate_yaml(results_dict)
        except Exception as err:
            raise(err)

        return results_dict

    def _parse(self):
        yaml_dict = self._load_result_file()

        try:
            results = self._parse_yaml(yaml_dict)
            self.results_matrix = results
        except Exception as err:
            raise(err)
        self.results_matrix = self._parse_yaml(yaml_dict)

    def _validate_yaml(self, yaml_dict):
        if len(yaml_dict) < 1:
            raise ValueError('YAML file does not contain any results')

        for field in self.fields:
            if field not in yaml_dict[0]:
                raise ValueError('The provided YAML file cannot be validated...')

        return True

    def _parse_yaml(self, yaml_dict):
        self.iterations = len(yaml_dict)
        results_mat = None
        for i in range(0, self.iterations):
            print(i)
            print('hry')
            print(self.iterations)
            bench_res = [None] * len(self.fields)
            for field in self.fields:
                index = self.fields.index(field)
                if field in yaml_dict[i]:
                    bench_res[index] = yaml_dict[i][field]
            if results_mat is None:
                results_mat = np.array(bench_res).astype(np.float)
            else:
                results_mat = np.vstack((results_mat,
                                         np.array(bench_res).astype(np.float)))

            print(results_mat)
        return results_mat

