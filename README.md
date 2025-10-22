# Language-Benchmark-of-matrix-multiplication
#  Introduction

Matrix multiplication is a fundamental operation in computing, serving as the basis for algorithms in diverse fields such as machine learning, physical simulation, and graphics processing. The standard algorithm used to multiply two square matrices of size $N \times N$ has a time complexity of $O(N^3)$.

The main objective of this work is to perform a **benchmark** analysis of the $O(N^3)$ algorithm in native implementations using three programming languages with different execution architectures: **C** (compiled), **Java** (Virtual Machine - JVM), and **Python** (interpreted). This study aims to provide an objective metric of each language’s efficiency for compute-intensive tasks as a function of matrix size.

---

#  Languages Used and Their Purpose

For the benchmark, three languages were selected to represent different execution paradigms, contrasting the efficiency of compilation versus interpretation and virtual machine execution:

| Language | Execution Architecture | Purpose in the Benchmark | Key Configuration |
| :------- | :---------------------- | :------------------------ | :---------------- |
| **C** | Compiled to machine code | Establish the **fastest performance baseline**. | Compiled with `gcc -O3`. |
| **Java** | Virtual Machine (JVM) | Measure performance optimized by the **Just-In-Time (JIT)** compiler. | Executed in JVM runtime. |
| **Python** | Interpreted (CPython) | Measure performance under the **interpreter overhead**. | Standard interpreter. |

All implementations use the standard matrix multiplication algorithm with three nested loops, without relying on external optimized libraries (such as NumPy, BLAS, or MKL), to ensure a fair comparison of each language’s intrinsic performance.

---

#  Results Table

The table below presents the **average execution times** obtained for the multiplication of $N \times N$ matrices, based on the conducted tests:

| Matrix Size ($N \times N$) | C (s) | Java (s) | Python (s) |
| :-------------------------: | :---: | :------: | :--------: |
| **$256 \times 256$** | 0.0234 | 0.0320 | 3.2477 |
| **$512 \times 512$** | 0.2328 | 0.2980 | 24.8149 |
| **$1024 \times 1024$** | 2.4195 | 7.5650 | 234.4954 |
| **$2048 \times 2048$** | 27.1064 | 92.5630 | 2200.000|

*\* Note: The time for Python at $2048 \times 2048$ is omitted due to being excessively long/not recorded, illustrating its lack of scalability.*

---

#  Conclusion Based on the Results

The performance analysis validates the hypothesis that language architecture significantly impacts efficiency in computationally intensive tasks.

1. **C is the performance leader:** It stands out as the **fastest language**, consistently outperforming the others thanks to direct optimization into machine code.  
2. **Java provides strong intermediate performance:** Its JIT compilation offers much higher speed than Python, proving to be a viable option that balances speed and portability.  
3. **Python shows poor scalability:** The high **interpreter overhead** makes it unsuitable for intensive matrix computation without the support of optimized native libraries.

**In summary:** For projects that demand maximum performance in matrix computations, compiled and low-level languages like C are the preferred choice.
