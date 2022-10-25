# import streamlit as st
# from streamlit_folium import st_folium
# import folium
#
# m = folium.Map(location=[37.566697, 126.978426])
#
# st_data = st_folium(m, width=725)

import streamlit as st
import streamlit.components.v1 as components

btn = st.button('눌러')
x = 'primary'
if btn:
    x = 'success'



# bootstrap 4 collapse example
components.html(
    """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.2/dist/umd/popper.min.js" integrity="sha384-IQsoLXl5PILFhosVNubq5LC7Qb9DXgDA9i+tQ8Zj3iwWAwPtgFTxbJ8NT4GN1R8p" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.min.js" integrity="sha384-cVKIPhGWiC2Al4u+LWgxfKTRIcfu0JTxR+EQDz/bgldoEyl4H0zUF0QKbrJ0EcQF" crossorigin="anonymous"></script>
    <div class="alert alert-""" + x + """ " role="alert">
      A simple primary alert—check it out!
    </div>

    """,
    height=600,
)

