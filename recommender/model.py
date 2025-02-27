import pandas as pd
from openai import OpenAI
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
import re
import streamlit as st
#setup - embedding
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=st.secrets["API_KEY"]
    )
#import vector databases
VS_content_based = FAISS.load_local(
    "../data/04_vector_store/VS_content_based",
    embeddings, allow_dangerous_deserialization=True
    )
VS_collab_based = FAISS.load_local(
    "../data/04_vector_store/VS_content_based", embeddings, allow_dangerous_deserialization=True
)

def recommender(purchased_games, df_feats):
    #treating game list
    purchased_games = [re.sub('[^A-Za-z0-9]+', '', i) for i in purchased_games]
    purchased_games = [i.lower() for i in purchased_games]
    purchased_games = [i.replace(' ','') for i in purchased_games]
    
    #filter DF
    df_feats = df_feats[df_feats.FK_GAME_NAME.isin(purchased_games)]
    df_feats = df_feats.drop_duplicates(subset='FK_GAME_NAME')
    df_feats['explicative_features'] =\
    df_feats['Tags'].astype(str)\
    + '|' + df_feats['Categories'].astype(str)\
    + '|' + df_feats['Supported languages'].astype(str)\
    + '|' + df_feats['Estimated owners'].astype(str)\
    + '|' + df_feats['Price'].astype(str)
    
    df_feats['explicative_features'] = df_feats['explicative_features'].astype(str).str.replace("'",'No description').str.replace("None",'No description')
    explicative_features = ' '.join(df_feats['explicative_features'].to_list())
    content_results = VS_content_based.similarity_search(
    str(explicative_features),
    k=30,
    )
    content_results_list=[]
    for i in content_results:
        content_results_list.append(i.id)
    collab_results = list(set(content_results_list)-set(purchased_games))
    return collab_results