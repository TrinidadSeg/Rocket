import streamlit as st
from pymongo.mongo_client import MongoClient
import pymongo
import urllib
cluster = MongoClient("mongodb+srv://tsegovialtri:C1diUqOmvgu0aIfm@testertrini.jhjnbmv.mongodb.net/")
db = cluster ["test"]
collection = db["test"]
post = {"fanta", "coke", "water"}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
st.text(post_id)
collection.insert_one(post)
print('Hello World')
st.title("Este es tu directorio")
