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
st.dataframe(df_feat.head())

content = model.recommender(purchased_games, df_feat)
st.dataframe(df_feat[df_feat.FK_GAME_NAME.isin(content)])
st.markdown(content)

if len(purchased_games)==0:
    st.header("Welcome to the plaform! You don't have any game yet, so here are popular games:")
    col_norec_a, col_norec_b, col_norec_c = st.columns(3)
    with col_norec_a:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_norec_b:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_norec_c:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
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
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_content_b:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    with col_content_c:
        st.image('https://cdn.akamai.steamstatic.com/steam/apps/72850/ss_4e95fbcf72ce2a9f86075738fa9930ef2bed1ac7.1920x1080.jpg?t=1647357402')
        st.markdown('The Elder Scrolls V Skyrim')
    
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
    
