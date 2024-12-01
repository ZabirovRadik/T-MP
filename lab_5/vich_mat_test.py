import numpy as np
import pytest

from vich_mat.first_lab import first_func, rand_matrix, find_integral


def test_first_func():
    matrix = np.array([[2, 1, 3, 6],
                        [4, 1, 3, 3],
                        [5, 2, 4, 1],
                        [5, 1, 2, 2]])
    assert first_func(matrix) == 5


@pytest.mark.parametrize("shape",
                         [10, 5, 12])
def test_rand_matrix(shape):
    A, B, X = rand_matrix(shape)
    assert A.shape == (shape, shape)
    assert B.shape == (shape, 1)
    assert X == np.linalg.solve(A, B)


def test_find_integral():
    assert find_integral() == (0.4689050339872516,-591.123779986244)
