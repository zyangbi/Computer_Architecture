CHECK IF YOUR OPTIMIZED CODES ARE PASSED FIRST BEFORE CREATING YOUR TRACES

You need to create traces and compress them to use for the Champsim.
1. Create your traces with the following command
    $ bash generate_trace.sh <0-3> 
        0: Make trace for the base matrix multiplication code (matmul_basic.c)
        1: Make trace for the opt1 matrix multiplication code (matmul_opt1.c)
        2: Make trace for the opt2 matrix multiplication code (matmul_opt2.c)
2. Change to the traces directuly and compress the trace with the following command
    $ cd traces
    $ xz -v3 <YOUR TRACE NAME>

ALWAYS COMPRESS YOUR TRACE FIRST BEFORE GENERATING NEW ONE