from flask import Flask

app = Flask(__name__)
from post.controller import routes
