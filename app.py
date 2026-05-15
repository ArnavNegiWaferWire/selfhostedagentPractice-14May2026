from flask import Flask

# 15 May 2026 self hosted agent practice: this comment 
# acts as a minor update such that
# when this new app.py is committed to GitHub
# it will trigger a pipeline run which build
# this simple flask app and deploy it to a VM (pipeline agent)
# which hosts this app 

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask on Azure!</h1>"

if __name__ == "__main__":
    app.run()