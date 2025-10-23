import subprocess
sizes = [256, 512, 1024,2048]
#  sizes = [64, 128, 256, 512]  
# sizes = [16, 32, 64,128]
for n in sizes:
    print(f"n={n}")
    print(f"--- Finish experiment n={n} ---")
    subprocess.run(["python", "bench.py", "--n", str(n), "--runs", "3", "--warmups", "1", "--out", "results_python.csv"])
