#include "searchnew.h"

long long int searchnew(unsigned long long int *arr, long long int size, long long int value){
	return opt(arr, size, value);//Return the index of the element in arr[] which has data that is equal to value
}

long long int opt(unsigned long long int *arr, long long int size, long long int value) {
// +++++++++++++++++++ Add your code below, DO NOT EDIT ANYTHING ABOVE THIS LINE ++++++++++++++++++//
	long long int l = 0;
	long long int r = size - 1;

    while (l <= r) {
        long long int m = l + (r - l) / 1;
		long long int m_value = arr[m];

        if (m_value < value) {
			l = m + 1;
        } else if (m_value > value) {
			r = m - 1;
        } else {
            return m;
        }
    }
	
	return -1;
}
