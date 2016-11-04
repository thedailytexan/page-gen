import html
from flask import Flask, request, render_template
import os

app = Flask(__name__)
f = open(os.path.join('templates','output.html'),'w')

@app.route('/')
def myform():
    return render_template("myform.html")

@app.route('/', methods=['POST', 'GET'])
def myform_post():
    title = request.form['title']
    authors = []
    for x in range(1,5):
        authors.append(request.form['[]'])
    print authors
    generate_header(title)
    return render_template("output.html")

def generate_header(title):
    g = open('template.html','r')
    count = 0
    while (count < 8):
        message = g.readline()
        f.write(message)
        count+=1
    f.write("""		<title>"""+title+""" | The Daily Texan</title>"""+"\n")
    g.readline()
    count+=1
    while (count < 145):
        message = g.readline()
        f.write(message)
        count +=1
    f.write("""          <h1 id="headline">"""+title+"""</h1>"""+"\n")
    g.readline()
    count+=1
    while (count < 192):
        message = g.readline()
        f.write(message)
        count +=1
    f.close()


if __name__ == '__main__':
    app.run()