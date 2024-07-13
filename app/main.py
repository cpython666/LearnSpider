from fastapi.responses import HTMLResponse
from fastapi import FastAPI,Depends, Header
from fastapi.staticfiles import StaticFiles
import os
import uvicorn

app = FastAPI()
app.mount("/templates", StaticFiles(directory=os.path.join(os.path.dirname(__file__),'templates')), name="templates")
app.mount("/static", StaticFiles(directory=os.path.join(os.path.dirname(__file__),'static')), name="static")

@app.get("/",response_class=HTMLResponse)
async def index():
    file=open(os.path.join('templates','0.index.html'),'r',encoding='utf-8').read()
    return file
@app.get("/get_headers")
async def get_headers(user_agent: str = Header(None), x_token: str = Header(None)):
    return {"User-Agent": user_agent, "X-Token": x_token}

# 根据请求id返回对应页面
@app.get("/{number}", response_class=HTMLResponse)
async def get_number_html(number: int):
    file_list=os.listdir('templates')
    try:
        hello_file=list(filter(lambda x:x.startswith(f'{number}.'),file_list))[0]
        html_content=open(os.path.join('templates',hello_file),'r',encoding='utf-8').read()
        return HTMLResponse(content=html_content, status_code=200)
    except FileNotFoundError:
        return HTMLResponse(content=f"改题目id不存在", status_code=404)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000,reload=True)