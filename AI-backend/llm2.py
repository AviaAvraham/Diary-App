from pinecone import ServerlessSpec
from langchain_community.vectorstores import Pinecone
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
import os


os.environ['OPENAI_API_KEY'] = 'sk-proj-lhrGw7CEUgR5WPe121plT3BlbkFJrbDuDxFBIgADbCxugJnF'
os.environ['PINECONE_API_KEY'] = '39e6ca0c-4d12-419b-9623-d4e1c0f871ca'
index_name = "writing-history"
embeddings = OpenAIEmbeddings()


def init_langchain():
    pass

def upload_doc(str_doc, user_id):
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents([str_doc])
    vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)
    for i, doc in enumerate(docs):
        doc.metadata = {
            "user_id": user_id
        }
    vectorstore.add_documents(docs)

def generate_writing_prompt():
    pass


# loader = TextLoader("history.txt")
# documents = loader.load()




retriever = vectorstore.as_retriever()

# Initialize language model
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)

# Create RetrievalQAWithSourcesChain
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Query the chain
# answer = chain({"question": "give me a prompt to journal"}, return_only_outputs=True)
# print(answer)

def main():
    print("hi")
