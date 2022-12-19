# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from functools import reduce
from math import log2
import numpy as np
import paddle
from paddle import add, to_tensor
from paddle import kron as kron
from paddle import matmul
from paddle import transpose
from paddle import concat, ones
from paddle import zeros

__all__ = [
    "partial_trace"
]


def partial_trace(rho_AB, dim1, dim2, A_or_B):
    if A_or_B == 2:
        dim1, dim2 = dim2, dim1

    idty_np = np.identity(dim2).astype("complex128")
    idty_B = to_tensor(idty_np)

    zero_np = np.zeros([dim2, dim2], "complex128")
    res = to_tensor(zero_np)

    for dim_j in range(dim1):
        row_top = zeros([1, dim_j], dtype="float64")
        row_mid = ones([1, 1], dtype="float64")
        row_bot = zeros([1, dim1 - dim_j - 1], dtype="float64")
        bra_j = concat([row_top, row_mid, row_bot], axis=1)
        bra_j = paddle.cast(bra_j, 'complex128')

        if A_or_B == 1:
            row_tmp = kron(bra_j, idty_B)
            row_tmp_conj = paddle.conj(row_tmp)
            res = add(res, matmul(matmul(row_tmp, rho_AB), transpose(row_tmp_conj, perm=[1, 0]), ), )

        if A_or_B == 2:
            row_tmp = kron(idty_B, bra_j)
            row_tmp_conj = paddle.conj(row_tmp)
            res = add(res, matmul(matmul(row_tmp, rho_AB), transpose(row_tmp_conj, perm=[1, 0]), ), )

    return res
