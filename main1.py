import pandas as pd
import streamlit as st
import import_ipynb
import Recommendation as rec
import urllib.request
from PIL import Image 

st.set_page_config(
    page_title="Recommender App",
    layout="wide",                
)

movies=pd.read_csv("data.csv") 
Title=movies["Title"]
img_list=movies["Links"]
year=movies["Year"]
genere=movies["Genere"]
desc=movies["Description"]
st.title("Movie Recommendation System")
selectvalue=st.selectbox("Select movie from the dropdown", Title)
def image(url,save_as):
        urllib.request.urlretrieve(url,save_as)
    
def show_recommend(movie):
    index=movies[movies['Title']==movie].index[0]
    url=img_list[index]
    image(url,"img.jpg")
    img =Image.open(r"img.jpg")
    st.image(img)
    st.header(movie)
    st.write("Year: ",year[index])
    st.write("Genere: ",genere[index])
    st.write("Description: ",desc[index])
    
def display(movie_name):
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        show_recommend(movie_name[0])
            
    with col2:
        show_recommend(movie_name[1])
                
    with col3:
        show_recommend(movie_name[2])
        
    with col4:
        show_recommend(movie_name[3])
        
    with col5:
        show_recommend(movie_name[4])

if st.button("Show Recommend"):
    movie_genere = rec.recommend_movies(selectvalue,"Genere")
    movie_desc = rec.recommend_movies(selectvalue,"Description")
    
    col1,col2=st.columns([1,4])
    with col1:
        index=movies[movies['Title']==selectvalue].index[0]
        url=img_list[index]
        image(url,"img.jpg")
        img =Image.open(r"img.jpg")
        st.image(img)
        
    with col2:
        st.header(selectvalue)
        index=movies[movies['Title']==selectvalue].index[0]
        st.write("Year: ",year[index])
        st.write("Genere: ",genere[index])
        st.write("Description: ",desc[index])
        
    st.header("Some Other Recommendations Based On Genere:")
    display(movie_genere)
    st.header("Some Other Recommendations Based On Reviews:")
    display(movie_desc)
    