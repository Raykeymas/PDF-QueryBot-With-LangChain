import pinecone
import os
from langchain.vectorstores import Pinecone
from typing import List
from langchain.embeddings.openai import OpenAIEmbeddings


class VectorStore:
  def __init__(self, index_name: str) -> None:
    """
    VectorStoreオブジェクトを初期化します。

    Args:
        index_name (str): インデックス名。
    """
    pinecone.init(
        api_key=os.getenv("PINECONE_API_KEY"),
        environment=os.getenv("PINECONE_ENV"),
    )
    self.index_name = index_name

  def get_vectorstore(self, embeddings: OpenAIEmbeddings) -> Pinecone:
    """
    VectorStoreオブジェクトを取得します。

    Args:
        embeddings (OpenAIEmbeddings): OpenAIEmbeddingsオブジェクト

    Returns:
        Pinecone: Pineconeオブジェクト
    """
    return Pinecone(
        pinecone.Index(self.index_name),
        embeddings.embed_query,
        "text",
    )

  def create_index(self) -> None:
    """
    インデックスを作成します。

    Args:
        None

    Returns:
        None
    """
    if self.index_name not in pinecone.list_indexes():
      pinecone.create_index(
          name=self.index_name,
          metric='cosine',
          dimension=1536
      )

  def delete_index(self) -> None:
    """
    インデックスを削除します。

    Args:
        None

    Returns:
        None
    """
    if self.index_name in pinecone.list_indexes():
      pinecone.deinit()
      pinecone.delete_index(name=self.index_name)

  def insert_vectors(self, pages: List[str], embeddings: OpenAIEmbeddings) -> Pinecone:
    """
    ベクトルをインデックスに挿入します。

    Args:
        pages (List[str]): PDFページのリスト
        embeddings (OpenAIEmbeddings): OpenAIEmbeddingsオブジェクト

    Returns:
        Pinecone: Pineconeオブジェクト
    """
    return Pinecone.from_documents(pages, embeddings, index_name=self.index_name)
