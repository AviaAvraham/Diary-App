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

# vectorstore = PineconeVectorStore(index_name=index_name, embedding=embeddings)

loader = TextLoader("history.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

vectorstore = PineconeVectorStore.from_documents(
    docs,
    index_name=index_name,
    embedding=embeddings
)

# Convert documents to embeddings
# texts = [doc for doc in documents]
# metadatas = [{"source": doc.metadata["source"]} for doc in documents]
# embeddings_vectors = [embeddings.embed(text) for text in texts]

retriever = vectorstore.as_retriever()

# Initialize language model
llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)

# Create RetrievalQAWithSourcesChain
chain = RetrievalQAWithSourcesChain.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

# Query the chain
answer = chain({"question": "give me a prompt to journal"}, return_only_outputs=True)
print(answer)
