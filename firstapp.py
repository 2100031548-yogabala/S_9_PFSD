# import Flask
from flask import Flask
#create an app instance
app=Flask(__name__)
#renderring(route)
@app.route("/")

def sample():
    return "welcome to flask"
if __name__=="__main__":
    app.run(debug=True)