import math

from eqs import Matrix, Vector
from eqs.validate_sys import validate_system


def conjugate_gradient_solve(
        sys_mat: Matrix,
        sys_vec: Vector,
        max_iter=100,
        max_error=1e-8
):
    """
    The conjugate gradient method is a iterative numeric method to
    solve systems of linear equations.

    The method starts with a vector full of zeroes as the first
    approximation to the solution and improves it in each
    iteration.
    In every iteration the error vector `r` is checked and only in
    the case where every value is less than the `max_error`, the
    solution is considered "good enough" and the solution vector
    returned.

    If after `max_iter` iterations a "good enough" solution hasn't
    been found, the function raises an `ArithmeticError`.

    :param sys_mat: system `Matrix`
    :param sys_vec: system `Vector`
    :param max_iter: `int` max number of iterations
    :param max_error: `float` max error accepted in the solution
    :return:
    """
    validate_system(sys_mat, sys_vec)

    solution = Vector(sys_vec.length)
    r = sys_vec - sys_mat.times_vector(solution)
    p = r.copy()

    def solution_good_enough():
        for i in range(sys_vec.length):
            if math.fabs(r.value_at(i)) > max_error:
                return False

        return True

    for _ in range(max_iter):
        if solution_good_enough():
            return solution

        m_times_p = sys_mat.times_vector(p)
        alpha = (r * r).sum / (p * m_times_p).sum
        solution += p.scaled(alpha)
        old_r = r.copy()
        r -= m_times_p.scaled(alpha)
        beta = (r * r).sum / (old_r * old_r).sum
        p = r + p.scaled(beta)

    raise ArithmeticError(
        f'Reached max number of iterations ({max_iter}) without ' +
        'a good solution '
    )
