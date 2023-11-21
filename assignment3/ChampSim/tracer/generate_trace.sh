#!/bin/bash
if [ $1 -eq 0 ]; then
    ./pin-3.22-98547-g7a303a835-gcc-linux/pin -t obj-intel64/champsim_tracer.so -o traces/matmul_basic-720M.champsim -s 720000000 -t 3000000 -- ../algorithms/assignment3.bin $1 1000
fi
if [ $1 -eq 1 ]; then
    ./pin-3.22-98547-g7a303a835-gcc-linux/pin -t obj-intel64/champsim_tracer.so -o traces/matmul_opt1-720M.champsim -s 720000000 -t  3000000 -- ../algorithms/assignment3.bin $1 1000
fi
if [ $1 -eq 2 ]; then
    ./pin-3.22-98547-g7a303a835-gcc-linux/pin -t obj-intel64/champsim_tracer.so -o traces/matmul_opt2-720M.champsim -s 720000000 -t  3000000 -- ../algorithms/assignment3.bin $1 1000
fi
