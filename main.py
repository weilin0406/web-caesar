from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head>
    
<<<<<<< HEAD
        <style>t
=======
        <style>
>>>>>>> e1daf7ca6c31f22af00697318a50e50b8127acd0
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
           
        </style>
    </head>
    <body>
        <form action="/new" method="post">
            <label>Rotate by:</label>
            <input type="text" id="rot" name="rot" value="0" />
            <textarea name="text">{0}</textarea>
            <input type="submit" />
        </form>
    </body>
</html>
"""
@app.route("/new", methods=['POST'])
def encrypt():
    rot = int(request.form["rot"])
    text = request.form["text"]
    cat = rotate_string(text, rot)


    return form.format(cat)



@app.route("/")
def index():
    return form.format("")

app.run()