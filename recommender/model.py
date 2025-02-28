from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
import re
import streamlit as st
import ast

#setup - embedding
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key=st.secrets["API_KEY"]
    )
#import vector databases
VS_content_based = FAISS.load_local(
    "data/04_vector_store/VS_content_based",
    embeddings, allow_dangerous_deserialization=True
    )

VS_collab_based = FAISS.load_local(
    "data/04_vector_store/VS_collab_based", embeddings, allow_dangerous_deserialization=True
)

def content_recommender(purchased_games, df_feat):
    #treating game list
    purchased_games = [re.sub('[^A-Za-z0-9]+', '', i) for i in purchased_games]
    purchased_games = [i.lower() for i in purchased_games]
    purchased_games = [i.replace(' ','') for i in purchased_games]
    
    #filter DF
    df_feat = df_feat[df_feat.FK_GAME_NAME.isin(purchased_games)]
    df_feat = df_feat.drop_duplicates(subset='FK_GAME_NAME')
    df_feat['explicative_features'] =\
    df_feat['Tags'].astype(str)\
    + '|' + df_feat['Categories'].astype(str)\
    + '|' + df_feat['Supported languages'].astype(str)\
    + '|' + df_feat['Estimated owners'].astype(str)\
    + '|' + df_feat['Price'].astype(str)
    
    df_feat['explicative_features'] = df_feat['explicative_features'].astype(str).str.replace("'",'No description').str.replace("None",'No description')
    explicative_features = ' '.join(df_feat['explicative_features'].to_list())
    content_results = VS_content_based.similarity_search(
    str(explicative_features),
    k=30,
    )
    content_results_list=[]
    for i in content_results:
        content_results_list.append(i.id)
    content_results = list(set(content_results_list)-set(purchased_games))
    return content_results



def collab_recommender(purchased_games):
    #treating game list
    purchased_games = [re.sub('[^A-Za-z0-9]+', '', i) for i in purchased_games]
    purchased_games = [i.lower() for i in purchased_games]
    purchased_games = [i.replace(' ','') for i in purchased_games]
    
    collab_results = VS_collab_based.similarity_search(
    str(purchased_games),
    k=10,
    )
    
    collab_results_list=[]
    for i in collab_results:
       converted_lists = ast.literal_eval(i.page_content)
       converted_lists = list(set(converted_lists))
       converted_lists = [item.split(',')[0] for item in converted_lists]
       collab_results_list.append(converted_lists)
    #collab_results = list(set(collab_results_list)-set(purchased_games))
    return collab_results_list