from pinecone import ServerlessSpec
from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
import os


os.environ['OPENAI_API_KEY'] = 'sk-proj-lhrGw7CEUgR5WPe121plT3BlbkFJrbDuDxFBIgADbCxugJnF'
os.environ['PINECONE_API_KEY'] = '39e6ca0c-4d12-419b-9623-d4e1c0f871ca'
index_name = "writing-history"
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)
embeddings = OpenAIEmbeddings()


def upload_doc(str_doc, user_id, doc_id):
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    document = Document(page_content=str_doc, metadata={"user_id": user_id, "source": doc_id})
    docs = text_splitter.split_documents([document])
    vectorstore.add_documents(docs)


def generate_writing_prompt(user_id):
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={
        'filter': {"user_id": user_id}
    },)
    chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)
    answer = chain({"question": "give me a prompt to journal"}, return_only_outputs=True)
    return answer


def main():
    # upload_doc("I'm a 22 years old soldier. I lost my best friend right in front of my eyes in Gaza.", user_id="123", text_id="1")
    # upload_doc("I'm 70 years old civilian, I lost my grandson at the october attack.", user_id="456", text_id="2")
    generate_writing_prompt("123")
    print("hi")


if __name__ == "__main__":
    main()