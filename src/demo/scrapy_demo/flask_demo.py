from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello World!"

@app.route("/user/<name>")
def show_user_profile(name):
    print("name: %s" %name)
    return "name: %s" %name

@app.route('/post/<int:id>')
def show_post(id):
    return "post %d" %id

if __name__ == "__main__":
    app.debug = True
    app.run()