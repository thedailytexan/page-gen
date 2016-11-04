f = open('kevin.html','w')

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



def generate_header1(title):
    g = open('template.html','r')
    lines_after_17 = g.readlines()[0:8]
    print(lines_after_17)
    f.close()

generate_header("Trump wins election!")
