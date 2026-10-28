from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/run")
def run(cmd: str):
    return {"output": run_command(cmd)}

def run_command(cmd):
    import subprocess
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout
