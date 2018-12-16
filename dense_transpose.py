import os
import sys
#import numpy as np
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        data = [(i+1)**2 for i in range(size)]
        matrix_file = open(argv[1], "rt")
	
	dimension = matrix_file.readline().strip().split()
        #row_total = dimension[0]
	#col_total = dimension[1]
        
        data = matrix_file.readline().strip().split()
        data1 = matrix_file.readline().strip().split()
        data2 = matrix_file.readline().strip().split()
        data3 = matrix_file.readline().strip().split()
	#for row in matrix_file:
        #    row = row.strip().split()
        #    row = comm.Scatter(row[0:10], local_a[:], root=0)
        
        comm.Barrier() 
    else:
        data = None
        data1 = None
        data2 = None
        data3 = None
        comm.Barrier()	

    data = comm.scatter(data, root=0)
    data1 = comm.scatter(data1, root=0)
    data2 = comm.scatter(data2, root=0)
    data3 = comm.scatter(data3, root=0)

    wow = [data, data1, data2, data3]

    print("I am process " + str(rank) + " and I have " + str(wow))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
