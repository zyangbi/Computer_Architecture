all: assignment1
assignment1: assignment1.o searchnew.o searchoriginal.o
	gcc -O3 assignment1.o searchnew.o searchoriginal.o -o assignment1.bin
searchnew.o: searchnew.c
	gcc -c searchnew.c
searchoriginal.o: searchoriginal.c
	gcc -c searchoriginal.c
clean:
	rm searchnew.o searchoriginal.o searchoriginal.inst searchnew.inst assignment1.bin
