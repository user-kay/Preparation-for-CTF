from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/<username>')
def hello(username):
    return render_template_string('Hello %s' % username)

if __name__ == '__main__':
    # app.run(host='114.55.65.251')
    app.run(port=48080)

