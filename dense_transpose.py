from numpy import transpose
from mpi4py import MPI

def main():

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    print("test")

