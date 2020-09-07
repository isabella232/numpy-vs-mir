import numpy as np


def restriction(A):
    """
        applies simple restriction to A
        @param A n x n matrix
        @return (n//2 +1, n//2 + 1) matrix
    """
    # indicator for Dimension
    alpha = len(A.shape)
    # initialize result with respect to the wanted shape
    ret = np.empty(np.array(A.shape) // 2 + 1)
    # Index of the second to the last element to mention in ret (depends on
    # the shape of A)
    end = ret.shape[0] - (A.shape[0] + 1) % 2

    # Case: Dimension 1
    if alpha == 1:
        # get every second element in A
        ret[:end:] = A[::2]
        # set the last index correctly
        ret[-1] = A[-1]
    # Case: Dimension 2
    elif alpha == 2:
        # get every second element in A
        ret[:end:, :end:] = A[::2, ::2]
        # special case: borders
        ret[:end, -1] = A[::2, -1]
        ret[-1, :end] = A[-1, ::2]
        # special case: outer corner
        ret[-1, -1] = A[-1, -1]
    # Case: Dimension 3
    elif alpha == 3:
        # get every second element in A
        ret[:end:, :end:, :end:] = A[::2, ::2, ::2]
        # special case: inner borders
        ret[:end, :end, -1] = A[::2, ::2, -1]
        ret[-1, :end, :end] = A[-1, ::2, ::2]
        ret[:end, -1, :end] = A[::2, -1, ::2]
        # special case: outer borders
        ret[:end, -1, -1] = A[::2, -1, -1]
        ret[-1, :end, -1] = A[-1, ::2, -1]
        ret[-1, -1, :end] = A[-1, -1, ::2]
        # special case: outer corner
        ret[-1, -1, -1] = A[-1, -1, -1]
    # Case: Error
    else:
        raise ValueError('restriction: invalid dimension')

    return ret


def weighted_restriction(A):
    # indicator for Dimension
    alpha = len(A.shape)
    # initialize result with respect to the wanted shape
    ret = restriction(A)

    # min length is 3
    assert(A.shape[0] >= 3)

    if alpha == 1:
        # core
        ret[1:-1] /= 2
        # corner
        ret[1:-1] += (A[1:-2:2] + A[3::2]) / 4
    elif alpha == 2:
        # core
        ret[1:-1, 1:-1] /= 4
        # edges
        ret[1:-1, 1:-1] += (A[2:-1:2, 1:-2:2] + A[1:-2:2, 2:-1:2] +
                            A[2:-1:2, 3::2] + A[3::2, 2:-1:2]) / 8
        # corners
        ret[1:-1, 1:-1] += (A[1:-2:2, 1:-2:2] + A[1:-2:2, 3::2] +
                            A[3::2, 1:-2:2] + A[3::2, 3::2]) / 16
    elif alpha == 3:
        # OBACHT: not tested!!!
        # core
        ret[1:-1, 1:-1, 1:-1] *= 8
        # edges
        ret[1:-1, 1:-1, 1:-1] += (
            A[2:-1:2, 2:-1:2, 1:-2:2] + A[2:-1:2, 2:-1:2, 3::2] +
            A[2:-1:2, 1:-2:2, 2:-1:2] + A[2:-1:2, 3::2, 2:-1:2] +
            A[1:-2:2, 2:-1:2, 2:-1:2] + A[3::2, 2:-1:2, 2:-1:2]) * 4
        # more edges
        ret[1:-1, 1:-1, 1:-1] += (
            A[2:-1:2, 1:-2:2, 3::2] + A[2:-1:2, 3::2, 1:-2:2] +
            A[2:-1:2, 1:-2:2, 1:-2:2] + A[2:-1:2, 3::2, 3::2] +
            A[1:-2:2, 2:-1:2, 3::2] + A[3::2, 2:-1:2, 1:-2:2] +
            A[1:-2:2, 2:-1:2, 1:-2:2] + A[3::2, 2:-1:2, 3::2] +
            A[1:-2:2, 3::2, 2:-1:2] + A[3::2, 1:-2:2, 2:-1:2] +
            A[1:-2:2, 1:-2:2, 2:-1:2] + A[3::2, 3::2, 2:-1:2]) * 2
        # corners
        ret[1:-1, 1:-1, 1:-1] += (
            A[3::2, 1:-2:2, 1:-2:2] + A[3::2, 3::2, 1:-2:2] +
            A[3::2, 3::2, 3::2] + A[3::2, 1:-2:2, 3::2] +
            A[1:-2:2, 1:-2:2, 1:-2:2] + A[1:-2:2, 1:-2:2, 3::2] +
            A[1:-2:2, 3::2, 3::2] + A[1:-2:2, 3::2, 1:-2:2])

        ret[1:-1, 1:-1, 1:-1] /= 64
    else:
        raise ValueError('weighted restriction: invalid dimension')

    return ret
