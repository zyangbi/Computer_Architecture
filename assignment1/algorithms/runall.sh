#!/bin/bash
./assignment1.bin 0 $1
./assignment1.bin 1 $1
objdump -dS -M intel searchoriginal.o > searchoriginal.inst
objdump -dS -M intel searchnew.o > searchnew.inst
