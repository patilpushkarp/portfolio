import json
from fastapi import FastAPI
import nbformat
from reader import Reader
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_file():
    reader_obj = Reader()
    with open("temp.ipynb", "r") as f:
        notebook = nbformat.read(f, as_version=4)
    notebook_data = reader_obj.data_cleaner(notebook)
    return notebook_data

@app.get("/blogs")
def get_blogs():
    with open("blogs.json") as f:
        data = json.load(f)
    return data

@app.get("/blog/{blog_id}")
def get_blog_with_id(blog_id):
    reader_obj = Reader()
    with open("blogs_data.json") as f:
        blog_data = json.load(f)
    
    relevant_blog = [data for data in blog_data if str(data["id"]) == str(blog_id)]

    if relevant_blog:
        relevant_blog = relevant_blog[0]

    file_name = relevant_blog["blog_file"]
    with open(file_name, "r") as f:
            notebook = nbformat.read(f, as_version=4)
    notebook_data = reader_obj.data_cleaner(notebook)
    return notebook_data


@app.get("/projects")
def get_projects():
    with open("projects.json") as f:
        data = json.load(f)
    return data
