from flask import Flask, jsonify
app = Flask(__name__)

@app.get("/")
def hello():
    return jsonify(
        message="✨ Welcome to Cloud with VarJosh ✨",
        tip="Built with Flask, shipped by Jenkins, running in Docker.",
        UI="THis is from feature/ui branch",
        NOTE="This is new   pr",
        BRANCH="feaute branch is deleted WTF WTF WTF WTF WTF......."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
