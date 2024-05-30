# ベースイメージを指定
FROM python:3.9

# 作業ディレクトリを設定
WORKDIR /app

# 依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションが使用するポートを公開
EXPOSE 8000

# コンテナ起動時のコマンドを指定
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]