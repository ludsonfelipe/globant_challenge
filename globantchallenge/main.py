from fastapi import FastAPI, File, HTTPException, UploadFile

app = FastAPI()


@app.post("/upload-csv/")
async def upload_csv(file: UploadFile = File(...)):
    try:
        return {"filename": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
