import os
import sys
#import numpy as np
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    if rank == 0:
        data = []
        lines = 0
        matrix_file = open("test1.txt", "rt")

	dimension = matrix_file.readline().strip().split()
        
        for line in matrix_file:
            lines = lines + 1
            this_line = line.strip().split()
            data = data + this_line
      
        print(data)
        #i = 0
        #new_list=[]
        #while i < len(data):
        #    new_list.append(data[i:i+lines])
        #    i+=lines

        #data = (new_list)
        comm.Barrier()
    else:
        data = []
        comm.Barrier()	
    
    data = comm.scatter(data, root=0)

    print("I am process " + str(rank) + " and I have " + str(data))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
