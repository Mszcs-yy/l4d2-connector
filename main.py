from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="L4D2 Connect Helper")

@app.get("/")
async def root():
    return {"message": "L4D2 Connect API is running!"}

@app.get("/connect")
async def connect_to_server(server: str):
    """
    生成 Steam 一键连接链接，并提供友好的手动点击页面
    """
    if not server:
        return {"error": "缺少 server 参数，例如 ?server=1.2.3.4:27015"}
    
    # 生成 Steam 协议链接
    steam_url = f"steam://connect/{server}"
    
    # 返回一个友好的 HTML 页面（自动尝试跳转 + 手动点击按钮）
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>正在连接 L4D2 服务器</title>
        <meta http-equiv="refresh" content="0; url={steam_url}">
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
            h1 {{ color: #2e7d32; }}
            .btn {{
                display: inline-block;
                margin-top: 20px;
                padding: 15px 30px;
                background-color: #1976d2;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-size: 18px;
            }}
            .btn:hover {{ background-color: #1565c0; }}
        </style>
    </head>
    <body>
        <h1>正在唤起 Steam...</h1>
        <p>服务器地址: <strong>{server}</strong></p>
        <p>如果没有自动打开 Steam，请点击下方按钮：</p>
        <a href="{steam_url}" class="btn">🚀 手动打开 Steam 连接服务器</a>
        <br><br>
        <small>如果还是无法打开，请确保 Steam 已经在后台运行</small>
    </body>
    </html>
    """
    
    return HTMLResponse(content=html_content)