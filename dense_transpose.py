import os
import sys
#import numpy as np
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    local_a = []

    if rank == 0:
	matrix_file = open(argv[1], "rt")
	
	dimension = matrix_file.readline().strip().split()
        row_total = dimension[0]
	col_total = dimension[1]
	i = 0
        
	for row in matrix_file:
            row = row.strip().split()
            row = comm.Scatter(row, local_a[i], root=0)
            i = i + 1
        
        print("Process 0 has " + local_a)
        comm.Barrier() 
        matrix_file.close()
    else:
        comm.Barrier()
	print("I am process " + str(rank) + " and I have " + str(local_a))


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
