import html
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def input():
    return render_template("input.html")

@app.route('/', methods=['POST', 'GET'])
def input_post():
    title = request.form['title']
    headline = request.form['headline']
    authcount = int(request.form['member'])
    tauthors = []
    tauthorlinks = []
    for x in range (1,authcount):
        authors.append(request.form['author'+i])
        authorlinks.append("")
    
    intro_paragraph = request.form['intro_paragraph']
    content = request.form['content']
    return render_template("output.html", title = title, headline=headline, intro_paragraph=intro_paragraph, content=content)

if __name__ == '__main__':
    app.run()