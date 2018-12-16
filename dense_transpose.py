import os
import sys
#from numpy import transpose
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
	
	print("Matrix from " + argv[1] + ": ")
	for row in matrix_file:
	    print(row.strip())
	
	matrix_file.close()
    else:
	print("I am process " + str(rank))


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)