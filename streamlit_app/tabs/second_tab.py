import streamlit as st

import pandas as pd
import numpy as np
import plotlyviz


title = "Dataviz"
sidebar_name = "Dataviz"



def run():
    
    if 'year' not in st.session_state:
        st.session_state.year = 2005
        
    
    st.title(title)

    
    tab1, tab2, tab3 = st.tabs(["Tous les accidents", "Distinction qualitative", "Gravité moyenne"])
    with tab1:
        st.plotly_chart(plotlyviz.figplotly_1, theme=None, use_container_width=True)
    with tab2:
        st.plotly_chart(plotlyviz.figplotly_2, theme=None, use_container_width=True)
    with tab3:
        st.plotly_chart(plotlyviz.figplotly_3, theme=None, use_container_width=True)
        
    
    tab4, tab5 = st.tabs(["Évolution", "Comparaison"])
    
    with tab4:
        container = st.container()
        
        container2 = st.container()
        with container2:
            col1, col2, col3, col4, col5 = st.columns([1,1,5,1,1], gap="large")        
                        
            with col1:
                if st.button(label=":black_left_pointing_double_triangle_with_vertical_bar:"):
                    if st.session_state.year != 2005:
                        st.session_state.year = 2005
                        
            with col2:
                backward = st.button(label=":arrow_backward:")
                if st.session_state.year > 2005 and backward:
                    st.session_state.year -= 1
                    
            with col3:
                st.markdown("**Taux d'accidents graves de :red[2005] à :red[2020]**")
            
                        
            with col4:
                forward = st.button(label=":arrow_forward:")
                if st.session_state.year < 2020 and forward:
                    st.session_state.year += 1
            
            with col5:
                if st.button(label=":black_right_pointing_double_triangle_with_vertical_bar:"):
                    if st.session_state.year != 2020:
                        st.session_state.year = 2020
                    
            
        
        
        image = st.slider(label="label", min_value=2005, max_value=2020, key="year", label_visibility="collapsed")

        container.image(f"assets/dep_grav/{image}.png", caption=f"année {image}")
        
    with tab5:
        col_a, col_b, col_c, col_d = st.columns([2,5,2,5])
        with col_a:
            left = st.selectbox(":red[année]",range(2005, 2021), key="l",)
        with col_b:
            st.image(f"assets/dep_grav/{left}.png")
        with col_c:
            right = st.selectbox(":red[année]",range(2005, 2021))
        with col_d:
            st.image(f"assets/dep_grav/{right}.png")
            
                
        