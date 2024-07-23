import streamlit as st

# if you want to control the page using html it is also possible, but as you can see is not my strenght. 

st.set_page_config(
    page_title="Credits",
    page_icon="🎬",
    layout="wide"
)

st.markdown(
    """
    <style>
        body {
            background-color: #000000;
            color: #FFD700;
        }
        .stApp {
            max-width: 1200px;
            margin: 0 auto;
        }
        .stMarkdown h1 {
            color: #FFD700;
            text-align: center;
        }    
        .stMarkdown h3 {
            color: #FFD700;
            text-align: center;
        }
        .stMarkdown p {
            color: #FFD700;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)


credits_content = """

<h1>  </h1>
<h1>  </h1>

<h1> <strong>WRITTEN AND <span style="text-decoration: line-through;">DIRECTED</span> CODED </strong></h1>
<h3> by Gonzalo Quesada </h3>

<p> ------------------------------------------------------------------------ </p>

<p> <strong> Special Thanks to: Gonzalo Quesada </strong> </p>

<p> Stolen by: Santi Aguilar </p>
<p><i> Just kidding, he just steal hearts </i></p>
"""

st.markdown(credits_content, unsafe_allow_html=True)
