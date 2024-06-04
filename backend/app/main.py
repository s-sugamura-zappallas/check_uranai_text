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
from fastapi.middleware.cors import CORSMiddleware


# モジュールから関数インポート
from utils.html_to_df import html_to_df_rsa, html_to_df_zap, input_html_to_df_rsa, input_html_to_df_zap, result_html_to_df_rsa, result_html_to_df_zap
from utils.csv_to_df import csv_to_df
from libs.compare_toppage import compare_toppage
from libs.compare_inputpage import compare_inputpage

import logging
logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 許可するオリジンを指定
    allow_methods=["*"],
    allow_headers=["*"],
)

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

@app.post("/api/compare/inputpage")
async def compare_inputpage_endpoint(company: str = Form(...), input_html: str = Form(...), result_html: str = Form(...)):
    print(f"Received data: company={company}, input_html={input_html[:50]}, result_html={result_html[:50]}")
    try:
        if company == 'rsa':
            input_df = input_html_to_df_rsa(input_html)
            result_df = result_html_to_df_rsa(result_html)
        elif company == 'zap':
            input_df = input_html_to_df_zap(input_html)
            result_df = result_html_to_df_zap(result_html)
        else:
            raise ValueError(f"Unsupported company: {company}")
        
        comparison_result = compare_inputpage(input_df, result_df)
        return JSONResponse(content=comparison_result)
    except ValueError as e:
        return JSONResponse(status_code=400, content={"error": str(e)})    


handler = Mangum(app)



