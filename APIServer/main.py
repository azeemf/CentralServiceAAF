from fastapi import FastAPI
import psutil
import time

app = FastAPI()

# Store CPU usage samples
cpu_usage_samples = []

@app.get("/ping")
async def ping():
    return {"message": "pong"}

@app.get("/cpu-usage")
async def get_cpu_usage():
    global cpu_usage_samples
    # Record current CPU percentage
    cpu_percentage = psutil.cpu_percent(interval=1)
    cpu_usage_samples.append(cpu_percentage)
    
    # Keep only the last 30 seconds of data
    if len(cpu_usage_samples) > 30:
        cpu_usage_samples.pop(0)
    
    return {"cpu_usage": cpu_usage_samples}
