# 開発用のベースイメージを指定
FROM node:14 AS development

# 作業ディレクトリを設定
WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# 依存関係をインストール
RUN npm install

# アプリケーションのソースコードをコピー
COPY . .

# アプリケーションをビルド
RUN npm run build

# 本番用のベースイメージを指定
FROM nginx:stable-alpine AS production

# 本番用のNginx設定ファイルをコピー
COPY nginx.conf /etc/nginx/conf.d/default.conf

# ビルド成果物をNginxの公開ディレクトリにコピー
COPY --from=development /app/dist /usr/share/nginx/html

# ポートを公開
EXPOSE 80

# コンテナ起動時のコマンドを指定
CMD ["nginx", "-g", "daemon off;"]