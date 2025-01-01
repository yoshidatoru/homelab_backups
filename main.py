# main.py

from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post("/backup")
def create_backup(source: str, destination: str):
    try:
        # Run the rdiff-backup command
        result = subprocess.run(
            ["rdiff-backup", source, destination],
            capture_output=True,
            text=True,
            check=True
        )
        return {"success": True, "message": result.stdout}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=f"Backup failed: {e.stderr}")
