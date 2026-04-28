from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="L4D2 Connect Helper")

@app.get("/")
async def root():
    return {"message": "L4D2 Connect API is running!"}

@app.get("/connect")
@app.get("/connect/{server:path}")   # 新增：支持路径参数 /connect/xxx:xxx
async def connect_to_server(server: str = None):
    """
    支持两种调用方式：
    1. /connect?server=1.2.3.4:27015
    2. /connect/1.2.3.4:27015
    """
    # 如果是通过路径参数传入
    if not server and "server" in locals():
        server = locals().get("server")
    
    # 如果是查询参数传入
    if not server:
        # 从查询参数中获取
        from fastapi import Request
        # 这里我们用依赖注入方式更稳妥，但为了简单，我们直接处理
        pass

    # 兼容处理：如果 server 是 None，尝试从查询参数获取
    if not server:
        # 这个函数会被 FastAPI 自动注入 request，我们用简单方式处理
        return {"error": "缺少服务器地址，请使用 ?server=IP:PORT 或 /connect/IP:PORT"}

    # 生成 Steam 协议链接（使用更高成功率的格式）
    steam_url = f"steam://rungameid/550//+connect {server}"

    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>正在连接 L4D2 服务器</title>
        <meta http-equiv="refresh" content="0; url={steam_url}">
        <style>
            body {{ font-family: "Microsoft YaHei", Arial, sans-serif; text-align: center; padding: 60px 20px; background-color: #f5f5f5; }}
            .container {{ max-width: 600px; margin: 0 auto; background: white; padding: 40px; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
            h1 {{ color: #2e7d32; }}
            p {{ color: #555; font-size: 17px; line-height: 1.6; }}
            .btn {{
                display: inline-block;
                margin-top: 25px;
                padding: 16px 32px;
                background-color: #1976d2;
                color: white;
                text-decoration: none;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
            }}
            .btn:hover {{ background-color: #1565c0; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>正在唤起 Steam 并连接服务器...</h1>
            <p>服务器地址：<strong>{server}</strong></p>
            <p>如果没有自动打开，请点击下方按钮：</p>
            <a href="{steam_url}" class="btn">🚀 手动打开 Steam 连接服务器</a>
            <div style="margin-top: 30px; font-size: 15px; color: #666;">
                <small>提示：请确保 Steam 客户端已经在后台运行</small>
            </div>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content)