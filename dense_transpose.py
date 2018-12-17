import os
import sys
from mpi4py import MPI


def main(argc, argv):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    data = []
    row_total = 0

    if rank == 0:
        #data = [(i+1)**2 for i in range(size)] #Works fine without, not sure of purpose.
        matrix_file = open(argv[1], "rt")
	
	dimension = matrix_file.readline().strip().split()
	#col_total = dimension[1]
        
	row_total = 0
	for line in matrix_file:
	    line = line.strip().split()
	    data.append(line)
	    row_total += 1

	#for row in matrix_file:
        #    row = row.strip().split()
        #    row = comm.Scatter(row[0:10], local_a[:], root=0)
        
        comm.Barrier() 
    else:
	for i in range(4):
	    data.append(None)
        comm.Barrier()	

    data[0] = comm.scatter(data[0], root=0)
    data[1] = comm.scatter(data[1], root=0)
    data[2] = comm.scatter(data[2], root=0)
    data[3] = comm.scatter(data[3], root=0)

    wow = [data[0], data[1], data[2], data[3]]

    print("I am process " + str(rank) + " and I have " + str(wow))

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
