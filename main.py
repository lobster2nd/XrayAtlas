from flask import Flask, render_template, request, send_file

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/head')
def head():
    return render_template('/head.html')


@app.route('/pdf')
def pdf():
    filename = 'files/2.pdf'  # страницу файла прописывать здесь - решёткаНомерСтраницы без пробелов
    return '''<html><body><script>window.open(\'/open-pdf?file=''' + filename + '''\', \'_blank\');</script></body></html>'''


@app.route('/open-pdf')
def open_pdf():
    filename = request.args.get('file')
    return send_file(filename, mimetype='application/pdf')


if __name__ == "__main__":
    app.run()