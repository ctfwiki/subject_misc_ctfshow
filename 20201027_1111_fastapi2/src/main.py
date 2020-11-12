from typing import Optional
from fastapi import FastAPI,Form
from fastapi.responses import StreamingResponse
from io import BytesIO
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "fastapi2"}

youdontknow = ['import', 'open', 'eval', 'exec', 'class', '\'', '"', 'vars', 'str', 'chr', '%', '_', 'flag','in', '-', 'mro', '[', ']']

@app.post("/ccccalcccc",description='安全的计算器v2（flag就在根目录，但我不相信你能得到<font color="red">她</font>）')
def calc(q: Optional[str] = Form(...)):
    try:
        for kiword in youdontknow:
            if kiword in q:
                return {"res": "hack out!", "err": False}
        return {"res": eval(q), "err": False}
    except:
        return {"res": "", "err": True}

@app.get("/yuanliang_5_aaxx.zip")
def yl5():
    return StreamingResponse(BytesIO(open("yuanliang_5_aaxx.zip","rb").read()), media_type="application/octet-stream")

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000, workers=1)
