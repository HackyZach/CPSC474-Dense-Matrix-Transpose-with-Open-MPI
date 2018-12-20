import os
import sys
#import numpy as np
from mpi4py import MPI

def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    lines = 0  
    dimensions =[]
    data = []
    value = []
    
    if rank == 0:
        matrix_file = open("test1.txt", "rt")
        dimensions = matrix_file.readline().strip().split() #need to bcast this information.

	print("Original Matrix")
        for line in matrix_file:
            this_line = line.strip().split()
	    print(this_line)
            data = data + this_line
        
        comm.Barrier()

    else:
        comm.Barrier()	
    
    i = 0
    j = 0
    
    while i < 4:
        value.append(comm.scatter(data[j:j+size], root=0)) #
        j = j + size
        i = i + 1

    new_data = comm.gather(value, root=0)
    if rank == 0:
	print("")
	print("Transposed Matrix")
	for i in range(size):
	    print(new_data[i])

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
