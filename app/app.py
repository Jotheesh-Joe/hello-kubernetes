from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html', pod=os.environ['POD'], node=os.environ['NODE'], namespace=os.environ['NAMESPACE'], cluster=os.environ['ISTIO_META_CLUSTER_ID'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
