# bench.py
import argparse
import time
from matrix_prod import random_matrix, matmul_naive

def run_experiment(n, runs, warmups, seed=None):
    times = []
    for _ in range(warmups):  # Calentamiento (no se mide)
        A = random_matrix(n, seed)
        B = random_matrix(n, seed+1 if seed is not None else None)
        matmul_naive(A, B)
    
    for _ in range(runs):  # Medidas reales
        A = random_matrix(n, seed)
        B = random_matrix(n, seed+1 if seed is not None else None)
        start = time.perf_counter()
        matmul_naive(A, B)
        end = time.perf_counter()
        times.append(end - start)
    
    avg_time = sum(times) / len(times)
    print(f"Tamaño={n}, Promedio={avg_time:.6f}s, Muestras={runs}")
    return avg_time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=256, help="Tamaño de la matriz NxN")
    parser.add_argument("--runs", type=int, default=3, help="Número de repeticiones")
    parser.add_argument("--warmups", type=int, default=1, help="Número de ejecuciones de calentamiento")
    parser.add_argument("--seed", type=int, default=42, help="Semilla aleatoria")
    args = parser.parse_args()

    run_experiment(args.n, args.runs, args.warmups, args.seed)
