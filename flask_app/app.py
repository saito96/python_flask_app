from flask import Flask, render_template
import os

# template_dir = os.path.dirname(os.path.abspath(__file__))
# template_dir = os.path.join(template_dir, 'frontend')
# template_dir = os.path.join(template_dir, 'templates')
app = Flask(__name__)


@app.route("/")
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
