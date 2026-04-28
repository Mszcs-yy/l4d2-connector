from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="L4D2 Connect Helper")

@app.get("/")
async def root():
    return {"message": "L4D2 Connect API is running!"}

@app.get("/connect")
async def connect_to_server(server: str):
    """
    接收参数 server (例如 1.2.3.4:27015)，
    生成 steam://connect/1.2.3.4:27015 的协议并重定向。
    """
    if not server:
        return {"error": "缺少服务器地址参数"}
    
    steam_url = f"steam://connect/{server}"
    return RedirectResponse(url=steam_url)