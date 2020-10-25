from typing import Optional
from fastapi import FastAPI,Form
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"hello": "fastapi"}

@app.post("/cccalccc",description="安全的计算器")
def calc(q: Optional[str] = Form(...)):
    try:
        hint = "flag is in /mnt/f1a9,try to read it"
        block_list = ['import','open','eval','exec']
        for keyword in block_list:
            if keyword in q:
                return {"res": "hack out!", "err": False}
        return {"res": eval(q), "err": False}
    except:
        return {"res": "", "err": True}

if __name__ == '__main__':
    uvicorn.run(app=app, host="0.0.0.0", port=8000, workers=1)
