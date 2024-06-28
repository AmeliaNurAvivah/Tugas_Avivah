from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/keranjang-belanja')
def keranjang_belanja():
    return render_template('keranjang-belanja.html')

@app.route('/konfirmasi-pesanan')
def konfirmasi_pesanan():
    return render_template('konfirmasi-pesanan.html')

@app.route('/status-pesanan')
def status_pesanan():
    return render_template('status-pesanan.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
