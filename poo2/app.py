from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dados temporários (em produção, use um banco de dados)
consultas = []

@app.route('/')
def index():
    return render_template('pessoa1.html')

@app.route('/processar_consulta', methods=['POST'])
def processar_consulta():
    # Coletar todos os dados do formulário
    dados = {
        'animal': {
            'nome': request.form.get('animal_nome'),
            'sexo': request.form.get('animal_sexo'),
            'peso': request.form.get('animal_peso'),
            # ... outros campos do animal
        },
        'cliente': {
            'nome': request.form.get('cliente_nome'),
            'telefone': request.form.get('cliente_telefone'),
            # ... outros campos do cliente
        },
        # ... coletar dados de médico e funcionário
        'agendamento': {
            'data': request.form.get('data_agendamento'),
            'valor': request.form.get('valor_agendamento')
        },
        'action': request.form.get('action')
    }

    if dados['action'] == 'agendar':
        # Lógica para agendar consulta
        consultas.append(dados)
        return redirect(url_for('consulta_agendada'))
    elif dados['action'] == 'finalizar':
        # Lógica para finalizar consulta
        return redirect(url_for('consulta_finalizada', dados=dados))

@app.route('/consulta-agendada')
def consulta_agendada():
    return render_template('sucesso.html', mensagem="Consulta agendada com sucesso!")

@app.route('/consulta-finalizada')
def consulta_finalizada():
    dados = request.args.get('dados')
    return render_template('resumo.html', dados=dados)

if __name__ == '__main__':
    app.run(debug=True)