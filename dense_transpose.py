import os
import sys
import numpy as np
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
	matrix_file = open(argv[1], "rt")
	
	dimension = matrix_file.readline().strip().split()
        row_total = dimension[0]
	col_total = dimension[1]
	
	for row in matrix_file:
            row = row.strip().split()
            row = np.asarray(row, dtype=np.int32)
            row = comm.Scatter(row[0:], row[:9], root=0)

	matrix_file.close()
    else:
	print("I am process " + str(rank))


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
