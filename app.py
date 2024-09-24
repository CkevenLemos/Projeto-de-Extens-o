from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os animais cadastrados
animais = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            especie = request.form['especie']
            data_chegada = request.form['data_chegada']
            data_saida = request.form['data_saida']
            cor_pelagem = request.form['cor_pelagem']
            condicao_saude = request.form['condicao_saude']
            
            animal = {
                'nome': nome,
                'especie': especie,
                'data_chegada': data_chegada,
                'data_saida': data_saida,
                'cor_pelagem': cor_pelagem,
                'condicao_saude': condicao_saude
            }
            
            animais.append(animal)
            return redirect(url_for('listar_animais'))
        
        except KeyError as e:
            # Handle the case where a key is missing
            return f"Missing form field: {e}", 400
    
    return render_template('cadastro.html')

@app.route('/animais', methods=['GET'])
def listar_animais():
    # Filtragem
    especie_filtro = request.args.get('especie')
    cor_filtro = request.args.get('cor_pelagem')
    condicao_filtro = request.args.get('condicao_saude')
    
    animais_filtrados = [animal for animal in animais if
                         (not especie_filtro or animal['especie'] == especie_filtro) and
                         (not cor_filtro or animal['cor_pelagem'] == cor_filtro) and
                         (not condicao_filtro or animal['condicao_saude'] == condicao_filtro)]
    
    return render_template('listar_animais.html', animais=animais_filtrados)

if __name__ == '__main__':
    app.run(debug=True)