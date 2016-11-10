import html
from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/')
def myform():
    return render_template("myform.html")

@app.route('/', methods=['POST', 'GET'])
def myform_post():
    title = request.form['title']
    headline = request.form['headline']
    intro_paragraph = request.form['intro_paragraph']
    return render_template("output.html", title = title, headline=headline, intro_paragraph=intro_paragraph)

# def generate_header(title):
#     g = open('template.html','r')
#     count = 0
#     while (count < 8):
#         message = g.readline()
#         f.write(message)
#         count+=1
#     f.write("""		<title>"""+title+""" | The Daily Texan</title>"""+"\n")
#     g.readline()
#     count+=1
#     while (count < 145):
#         message = g.readline()
#         f.write(message)
#         count +=1
#     f.write("""          <h1 id="headline">"""+title+"""</h1>"""+"\n")
#     g.readline()
#     count+=1
#     while (count < 192):
#         message = g.readline()
#         f.write(message)
#         count +=1
#     f.close()


if __name__ == '__main__':
    app.run()