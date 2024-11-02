from fastapi import FastAPI
import subprocess

app = FastAPI()

# Store CPU usage samples
cpu_usage_samples = []

def get_cpu_usage_from_proc_stat():
    try:
        # Run the shell command and capture the output
        result = subprocess.run(
            ["bash", "-c", "grep 'cpu ' /proc/stat | awk '{usage=($2+$4)*100/($2+$4+$5)} END {print usage}'"],
            capture_output=True,
            text=True,
            check=True
        )
        # Convert the output to float and return
        return float(result.stdout.strip())
    except Exception as e:
        print(f"Error fetching CPU usage: {e}")
        return 0.0

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/cpu-usage")
async def get_cpu_usage():
    global cpu_usage_samples
    
    # Get CPU percentage using the command
    cpu_percentage = get_cpu_usage_from_proc_stat()
    
    # Append the latest CPU usage to the samples list
    cpu_usage_samples.append(cpu_percentage)
    
    # Keep only the last 30 seconds of data
    if len(cpu_usage_samples) > 30:
        cpu_usage_samples.pop(0)
    
    return {"cpu_usage": cpu_usage_samples}
