from flask import Flask

app = Flask(__name__)

@app.route('/mypage/me')
def My_page():
    my_name = "Bartłomiej"
    my_surname = "Szostak"
    return f'My_page, {my_name} , {my_surname}'