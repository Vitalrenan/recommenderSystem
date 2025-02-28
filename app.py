import streamlit as st
import pandas as pd
from recommender import model

st.title('Recommender systems')
st.markdown("Data scientist: Renan Vital")
st.divider()
purchased_games = st.multiselect(label='Purchase games:',
                options=['The Elder Scroll Svskyrim','Fallout 4','Spore','Left 4 Dead 2']
                )
#
df_feat = pd.read_parquet('https://swp-mvp-media.s3.us-east-1.amazonaws.com/data/02_processed/ABT_feats.parquet')
df_full = pd.read_parquet('/content/ABT_full.parquet',columns=['FK_GAME_NAME','GAME_NAME','Screenshots'])
df_full.drop_duplicates(subset='FK_GAME_NAME',inplace=True)
df_full['Screenshots'] = df_full['Screenshots'].apply(lambda x: x.split(',')[0] if x!=None else 'No Image')


content = model.recommender(purchased_games, df_feat)
st.dataframe(df_full[df_full.FK_GAME_NAME.isin(content)])
st.markdown(content)




if len(purchased_games)==0:
    st.header("Welcome to the plaform! You don't have any game yet, so here are popular games:")
    col_norec_a, col_norec_b, col_norec_c = st.columns(3)
    with col_norec_a:
        norec_a = df_full[df_full.FK_GAME_NAME.isin(content)].sample()
        st.image(norec_a['Screenshots'].item())
        st.image(norec_a['GAME_NAME'].item())
    with col_norec_b:
        norec_b = df_full[df_full.FK_GAME_NAME.isin(content)].sample()
        st.image(norec_b['Screenshots'].item())
        st.image(norec_b['GAME_NAME'].item())
    with col_norec_c:
        norec_c = df_full[df_full.FK_GAME_NAME.isin(content)].sample()
        st.image(norec_c['Screenshots'].item())
        st.image(norec_c['GAME_NAME'].item())
else:
    st.header('Hybrid recommendation - Based on your own games and players with similar interests:')
    col_hybrid_a, col_hybrid_b, col_hybrid_c = st.columns(3)
    with col_hybrid_a:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_hybrid_b:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_hybrid_c:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    
    st.header('Recommendations based on your games:')
    col_content_a, col_content_b, col_content_c = st.columns(3)
    with col_content_a:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>0:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[0])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[0])
        else:
            st.markdown("No recommendations yet")
    with col_content_b:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>1:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[1])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[1])
        else:
            st.markdown("No recommendations yet")
    with col_content_c:
        if df_full[df_full.FK_GAME_NAME.isin(content)].shape[0]>2:
            st.image(df_full[df_full.FK_GAME_NAME.isin(content)]['Screenshots'].iloc[2])
            st.markdown(df_full[df_full.FK_GAME_NAME.isin(content)]['GAME_NAME'].iloc[2])
        else:
            st.markdown("No recommendations yet")
    
    st.header('Recommendations based on similar users:')
    col_colab_a, col_colab_b, col_colab_c = st.columns(3)
    with col_colab_a:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_colab_b:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_colab_c:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    
