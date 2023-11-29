from fastapi import FastAPI, UploadFile, File
from secrets import token_hex

app = FastAPI(title="File Upload using FastAPI")


@app.get("/")
def index():
    return {"Status": "File upload app running"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_ext = file.filename.split('.').pop()
    file_name = token_hex(10)
    file_path = f'{file_name}.{file_ext}'
    with open(file_path, "wb") as f:
        content = await file.read()
        f.write(content)
        
    return {"success": True, "file_path": file_path, "message": "File uploaded successfully"}