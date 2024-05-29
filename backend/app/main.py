import sys
import os

# モジュールのあるディレクトリをシステムパスに追加
sys.path.append('libs')
sys.path.append('utils')

from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import JSONResponse
from io import StringIO
import pandas as pd
from mangum import Mangum


# モジュールから関数インポート
from utils.html_to_df import html_to_df_rsa, html_to_df_zap
from utils.csv_to_df import csv_to_df
from libs.compare_toppage import compare_toppage

import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

@app.post("/api/compare/toppage")
async def compare_toppage_endpoint(company: str = Form(...), html: str = Form(...), csv: UploadFile = File(...)):
    try:
        if company == 'rsa':
            html_df = html_to_df_rsa(html)
        elif company == 'zap':
            html_df = html_to_df_zap(html)
        else:
            raise ValueError(f"Unsupported company: {company}")
        

        csv_content = await csv.read()
        csv_file = StringIO(csv_content.decode('utf-8'))
        csv_df = csv_to_df(csv_file)
        comparison_result = compare_toppage(html_df, csv_df)
        return JSONResponse(content=comparison_result)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})
    
@app.get("/hello")
async def hello_world():
    return {"message": "Hello World"}

@app.get("/")
async def hello_top():
    return {"message": "Hello top"}

handler = Mangum(app)



