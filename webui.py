import os
import streamlit as st

from func import insert_pdf, ask


def process_file(file):
  tmp_path = "./pdf/tmp.pdf"
  # ファイルの処理を行う
  # ファイルのバイナリを取得する
  file_bytes = file.read()
  # 実ファイルとして格納する、そのパスをinsert_pdfに渡す
  with open(tmp_path, "wb") as f:
    f.write(file_bytes)
  # PDFをベクトルストアに挿入する
  insert_pdf(tmp_path)
  # ファイルを削除する
  os.remove(tmp_path)

  return "ベクトルを格納しました"


def ask_question(question):
  # 質問に対する回答を取得する
  result = ask(question)
  return result


# サイドメニューのUIを表示する
st.sidebar.title("メニュー")
FILE_UPLOAD = "マニュアルアップロード"
QUESTION = "Manual Boter"
FILE_UPLOAD_TITLE = "質問したいマニュアルをアップロードしてください"
QUESTION_TITLE = "your question"
ANSWER_BUTTON = "ask"

menu_options = [QUESTION, FILE_UPLOAD]
menu = st.sidebar.radio("", menu_options)

if menu == menu_options[0]:
  # 質問のUIを表示する
  st.title(QUESTION)
  question = st.text_area(QUESTION_TITLE)
  if st.button(ANSWER_BUTTON, key="answer_button") or question:
    with st.spinner("処理中..."):
      result = ask_question(question)
      st.write(result)
elif menu == menu_options[1]:
  # ファイルアップロードのUIを表示する
  st.title(FILE_UPLOAD)
  uploaded_file = st.file_uploader(FILE_UPLOAD_TITLE)
  if uploaded_file is not None:
    with st.spinner("処理中..."):
      result = process_file(uploaded_file)
      st.write(result)
