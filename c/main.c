#include <stdio.h>
#include <stdlib.h>
#include <sys/time.h>

#define MAX_SIZE 2048  
#define NUM_TESTS 5    
double a[MAX_SIZE][MAX_SIZE];
double b[MAX_SIZE][MAX_SIZE];
double c[MAX_SIZE][MAX_SIZE];

void initialize_matrices(int size) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            a[i][j] = (double)rand() / RAND_MAX;
            b[i][j] = (double)rand() / RAND_MAX;
            c[i][j] = 0;
        }
    }
}

void multiply_matrices(int size) {
    for (int i = 0; i < size; ++i) {
        for (int j = 0; j < size; ++j) {
            for (int k = 0; k < size; ++k) {
                c[i][j] += a[i][k] * b[k][j];
            }
        }
    }
}


void run_tests(int size) {
    struct timeval start, stop;
    double total_time = 0;

    for (int test = 0; test < NUM_TESTS; ++test) {
        initialize_matrices(size);

        gettimeofday(&start, NULL);
        multiply_matrices(size);
        gettimeofday(&stop, NULL);

        double diff = stop.tv_sec - start.tv_sec
            + 1e-6 * (stop.tv_usec - start.tv_usec);
        total_time += diff;

        printf("Test %d for size %d: %0.6f seconds\n", test + 1, size, diff);
    }

    double average_time = total_time / NUM_TESTS;
    printf("average for size %d: %0.6f seconds\n\n", size, average_time);
}

int main() {
    int matrix_sizes[] = { 256, 512, 1024, 2048 };
    int num_sizes = sizeof(matrix_sizes) / sizeof(matrix_sizes[0]);

    for (int i = 0; i < num_sizes; ++i) {
        int size = matrix_sizes[i];
        printf("=== test for matrix: %dx%d ===\n", size, size);
        run_tests(size);
    }

    return 0;
}