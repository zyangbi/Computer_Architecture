#include "matmul_opt2.h"

void matmul_opt2(unsigned long long int* mat_a, unsigned long long int* mat_b, unsigned long long int* mat_c, unsigned long long int matrix_size){
    //**********************************Add your optimized code below**********************************//
    unsigned long long int B = 64 / sizeof(unsigned long long int);  // block size = 64 bytes

    for (unsigned long long int kk = 0; kk < matrix_size; kk += B) {
        for (unsigned long long int ii = 0; ii < matrix_size; ii += B) {
            for (unsigned long long int j = 0; j < matrix_size; j++) {
                for (unsigned long long int k = kk; k < kk + B && k < matrix_size; k++) {
                    for (unsigned long long int i = ii; i < ii + B && i < matrix_size; i++) {
                        mat_c[j*matrix_size + i] += mat_a[k*matrix_size + i] * mat_b[j*matrix_size + k];
                    }
                }
            }
        }
    }
}