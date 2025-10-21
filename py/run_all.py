import subprocess

# sizes = [64, 128, 256, 512]  
sizes = [16, 32, 64, 128]
for n in sizes:
    print(f"n={n}")
    subprocess.run(["python", "bench.py", "--n", str(n), "--runs", "3", "--warmups", "1", "--out", "results_python.csv"])
