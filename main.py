import os
import sys
#import numpy as np
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    lines = 0  
    data = []
    value = []

    if rank == 0:
        matrix_file = open("test1.txt", "rt")

        dimension = matrix_file.readline().strip().split()
        
        for line in matrix_file:
            lines = lines + 1
            this_line = line.strip().split()
            data = data + this_line
        
        comm.Barrier()
    else:
        comm.Barrier()	

    i = 0
    j = 0
    while i < 4:
        value.append(comm.scatter(data[j:j+size], root=0))
        j = j + size
        i = i + 1

    print("I am process " + str(rank) + " and I have " + str(value))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
