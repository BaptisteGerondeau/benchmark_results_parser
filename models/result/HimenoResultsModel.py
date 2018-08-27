#!/usr/bin/env python3

import yaml
import numpy as np
from models.result.ResultModel import ResultModel

class HimenoResultModel(ResultModel):
    def __init__(self, result_path, benchmark_name, machine_type, toolchain, compiler_flags,
                 run_flags, num_id):
        super().__init__(result_path, benchmark_name, machine_type, toolchain, compiler_flags,
                 run_flags, num_id)
        self.fields = [ 'MFLOPS', 'cpu', 'gosa', 'imax', 'jmax', 'kmax',
                       'mimax', 'mjmax', 'mkmax', 'score']
        self._parse()
