from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma
import os 
import glob
import shutil

#Set path to Chroma Database & Sources 
CHROMA_PATH = "chroma"
DATA_PATH = "data/resources"

