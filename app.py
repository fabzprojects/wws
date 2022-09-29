from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api=Api(app)




import webbrowser







   


contents = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
<head>
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>Python Webbrowser</title>
</head>
<body>
<table>
fgh
</table>
</body>
</html>
'''

filename = 'web.html'

def main(contents, filename):
    output = open(filename,"w")
    output.write(contents)
    output.close()

main(contents, filename)    
webbrowser.open(filename)






if __name__ == "__main__":
    app.run(debug=True)