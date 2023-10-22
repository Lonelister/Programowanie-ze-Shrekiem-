from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='Templates')

app.static_folder = 'static'
app.static_url_path = '/static'
app.add_url_rule('/static/<filename>', 'static', build_only=True)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('Logowanie.html')

@app.route('/messages')
def inbox():
    return render_template('Inbox.html')

@app.route('/tags')
def multimedia():
    return render_template('tags.html')

@app.route('/tags/images')
def styles():
    return render_template('t-mgs.html')

@app.route('/tags/text')
def text():
    return render_template('t-txt.html')

@app.route('/front-end-vs-back-end')
def front_end_vs_back_end():
    return render_template('fe-vs-be.html')

@app.route('/tags/css')
def settings():
    return render_template('t-css.html')

@app.route('/tags/media')
def source():
    return render_template('t-media.html')

@app.route('/github')
def github():
    return redirect("https://github.com/Programowanie-ze-Shrekiem", code=302)

if __name__ == '__main__':
    app.run()