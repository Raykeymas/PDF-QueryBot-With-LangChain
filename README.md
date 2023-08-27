# LangChain と Pinecone を使ってマニュアルを読み込み、回答を生成するコード

## 環境

- Python 3.9.X
- Pinecode
- OpenAI API

## 利用方法

### 環境変数の設定

以下の環境変数を設定してください  
このディレクトリに`.env`ファイルを作成して定義しても構いません

```
PINECONE_ENV: Pineconeの環境名
PINECONE_API_KEY: PineconeのAPIキー
OPENAI_API_KEY: OpenAIのAPIキー
```

### main.py の書き換え

以下２箇所を必要に応じて変更してください

```
index_name = "langchain-demo"
model_name = "gpt-3.5-turbo"

```

### 必要なライブラリのインストール

```bash
$ pip install -r requirements.txt
```

### 実行

```bash
$ python main.py
```

# 参考ドキュメント

## 公式

https://docs.pinecone.io/docs/langchain
https://python.langchain.com/docs/integrations/vectorstores/pinecone

## その他

https://qiita.com/hiroki_okuhata_int/items/7102bab7d96eb2574e7d  
https://note.com/pharmax/n/n28b23641f3be  
https://book.st-hakky.com/docs/pinecone-use/
