import argparse
import time
from matrix_prod import random_matrix, matmul_naive

def run_experiment(n, runs, warmups, seed=None):
    times = []
    for _ in range(warmups):  
        A = random_matrix(n, seed)
        B = random_matrix(n, seed+1 if seed is not None else None)
        matmul_naive(A, B)
    
    for _ in range(runs):  
        A = random_matrix(n, seed)
        B = random_matrix(n, seed+1 if seed is not None else None)
        start = time.perf_counter()
        matmul_naive(A, B)
        end = time.perf_counter()
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    print(f"Matrix size={n}, Average time={avg_time:.6f}s, Samples={runs}")
    return avg_time

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Matrix multiplication benchmark (naive implementation).")
    parser.add_argument("--n", type=int, default=256, help="Matrix size (NxN).")
    parser.add_argument("--runs", type=int, default=3, help="Number of benchmark repetitions.")
    parser.add_argument("--warmups", type=int, default=1, help="Number of warmup runs (not measured).")
    parser.add_argument("--seed", type=int, default=42, help="Random seed for reproducibility.")
    parser.add_argument("--out", default="results_python.csv", help="Output CSV file for saving results.")

    args = parser.parse_args()

    run_experiment(args.n, args.runs, args.warmups, args.seed)
