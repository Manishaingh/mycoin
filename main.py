import subprocess
import time


scripts_to_run = [
    "scripts/blockchain.py",
    "scripts/coin.py",
    "scripts/exchange.py",
    "scripts/bank-site.py",
    "scripts/wallet.py",
    "api/api.py",
    "scripts/wallet-site.py",
    "scripts/search.py",
]


running_processes = {}


def run_script(script_name):
    while True:
        try:
            print(f"Running {script_name}...")
            process = subprocess.Popen(["python", script_name])
            process.wait()
        except Exception as e:
            print(f"An error occurred while running {script_name}: {e}")
        
        print(f"{script_name} has stopped. Restarting in 5 seconds...")
        time.sleep(5)


for script in scripts_to_run:
    try:
        process = subprocess.Popen(["python", script])
        running_processes[script] = process
    except Exception as e:
        print(f"An error occurred while starting {script}: {e}")


try:
    while True:
        for script, process in running_processes.items():
            if process.poll() is not None:
                print(f"{script} has stopped. Restarting...")
                new_process = subprocess.Popen(["python", script])
                running_processes[script] = new_process
                break  
        time.sleep(1)
except KeyboardInterrupt:
    print("Stopping all scripts...")
    for script, process in running_processes.items():
        process.terminate()
