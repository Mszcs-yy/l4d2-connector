from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="L4D2 Connect Helper")

@app.get("/")
async def root():
    return {"message": "L4D2 Connect API is running!"}

@app.get("/connect")
async def connect_to_server(server: str):
    """
    生成 Steam 一键连接链接，并提供友好的国内访问页面
    """
    if not server:
        return {"error": "缺少 server 参数，例如 ?server=1.2.3.4:27015"}

    # 生成 Steam 协议链接
    steam_url = f"steam://connect/{server}"

    # 优化后的 HTML 页面（国内访问友好 + 手动点击保障）
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>正在连接 L4D2 服务器</title>
        <meta http-equiv="refresh" content="0; url={steam_url}">
        <style>
            body {{
                font-family: "Microsoft YaHei", Arial, sans-serif;
                text-align: center;
                padding: 60px 20px;
                background-color: #f5f5f5;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.1);
            }}
            h1 {{
                color: #2e7d32;
                margin-bottom: 10px;
            }}
            p {{
                color: #555;
                font-size: 17px;
                line-height: 1.6;
            }}
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
            .btn:hover {{
                background-color: #1565c0;
            }}
            .info {{
                margin-top: 30px;
                font-size: 15px;
                color: #666;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>正在唤起 Steam...</h1>
            <p>服务器地址：<strong>{server}</strong></p>
            <p>如果没有自动打开 Steam，请点击下方按钮手动连接：</p>
            <a href="{steam_url}" class="btn">🚀 打开 Steam 连接服务器</a>
            
            <div class="info">
                <small>提示：请确保 Steam 客户端已经在后台运行<br>
                如果还是无法打开，请尝试右键复制链接在 Steam 中打开</small>
            </div>
        </div>
    </body>
    </html>
    """

    return HTMLResponse(content=html_content, status_code=200)