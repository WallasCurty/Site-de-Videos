from flask import Flask, render_template,redirect

app = Flask(__name__, template_folder='template')


@app.route('/')
def index():
    return render_template('index.html', title= 'Pagina Inicial')

@app.route('/jogo')
def jogo():
    return render_template('jogo.html', title= 'Jogos')
    
    

@app.route('/filme')
def filme():
    return render_template('filme.html', title= 'Filmes')

@app.route('/humor')
def humor():
    return render_template('humor.html', title= 'Humor')

if __name__ == '__main__':
    app.run(debug=True)
