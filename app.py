import streamlit as st
import pandas as pd
from recommender import model

st.title('Recommender systems')
st.markdown("Data scientist: Renan Vital")
st.divider()
#
df_feat = pd.read_parquet('https://swp-mvp-media.s3.us-east-1.amazonaws.com/data/02_processed/ABT_feats.parquet')
df_full = pd.read_parquet('https://swp-mvp-media.s3.us-east-1.amazonaws.com/data/02_processed/ABT_full.parquet',columns=['FK_GAME_NAME','GAME_NAME','Screenshots'])
df_full.drop_duplicates(subset='FK_GAME_NAME',inplace=True)
df_full['Screenshots'] = df_full['Screenshots'].apply(lambda x: x.split(',')[0] if x!=None else 'No Image')
purchased_games = st.multiselect(label='Purchase games:',
                options=df_full['GAME_NAME'].to_list()
                )

content = model.content_recommender(purchased_games, df_feat)
collab = model.collab_recommender(purchased_games)
hybrid = set(collab) & set(content)


if len(purchased_games)==0:
    st.header("Welcome to the plaform! You don't have any game yet, so here are popular games:")
    col_norec_a, col_norec_b, col_norec_c = st.columns(3)
    with col_norec_a:
        norec_a = df_full.sample()
        st.image(norec_a['Screenshots'].item())
        st.markdown(norec_a['GAME_NAME'].item())
    with col_norec_b:
        norec_b = df_full.sample()
        st.image(norec_b['Screenshots'].item())
        st.markdown(norec_b['GAME_NAME'].item())
    with col_norec_c:
        norec_c = df_full.sample()
        st.image(norec_c['Screenshots'].item())
        st.markdown(norec_c['GAME_NAME'].item())
else:
    st.header('Hybrid recommendation - Based on your own games and players with similar interests:')
    col_hybrid_a, col_hybrid_b, col_hybrid_c = st.columns(3)
    with col_hybrid_a:
        if df_full[df_full.FK_GAME_NAME.isin(hybrid)].shape[0]>0:
            st.image(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['Screenshots'].iloc[0])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['GAME_NAME'].iloc[0])
        else:
            pass
    with col_hybrid_b:
        if df_full[df_full.FK_GAME_NAME.isin(hybrid)].shape[0]>1:
            st.image(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['Screenshots'].iloc[1])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['GAME_NAME'].iloc[1])
        else:
            pass
    with col_hybrid_c:
        if df_full[df_full.FK_GAME_NAME.isin(hybrid)].shape[0]>2:
            st.image(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['Screenshots'].iloc[2])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(hybrid)]['GAME_NAME'].iloc[2])
        else:
            pass
    
    st.header('Recommendations based on your games:')
    col_content_a, col_content_b, col_content_c = st.columns(3)
    with col_content_a:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>0:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[0])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[0])
        else:
            pass
    with col_content_b:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>1:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[1])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[1])
        else:
            pass
    with col_content_c:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>2:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[2])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[2])
        else:
            pass
    
    st.header('Recommendations based on similar users:')
    col_colab_a, col_colab_b, col_colab_c = st.columns(3)
    with col_colab_a:
        if df_full[df_full.FK_GAME_NAME.isin(collab)].shape[0]>0:
            st.image(df_full[df_full.FK_GAME_NAME.isin(collab)]['Screenshots'].iloc[0])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(collab)]['GAME_NAME'].iloc[0])
        else:
            pass
    with col_colab_b:
        if df_full[df_full.FK_GAME_NAME.isin(collab)].shape[0]>1:
            st.image(df_full[df_full.FK_GAME_NAME.isin(collab)]['Screenshots'].iloc[1])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(collab)]['GAME_NAME'].iloc[1])
        else:
            pass
    with col_colab_c:
        if df_full[df_full.FK_GAME_NAME.isin(collab)].shape[0]>2:
            st.image(df_full[df_full.FK_GAME_NAME.isin(collab)]['Screenshots'].iloc[2])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(collab)]['GAME_NAME'].iloc[2])
        else:
            pass
    
