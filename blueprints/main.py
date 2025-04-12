from flask import Blueprint, render_template, request
from .logic import executar_buscas

main_bp = Blueprint('main', __name__)

capitais = ('Aracaju', 'Belém', 'Belo Horizonte', 'Boa Vista', 'Brasília','Campo Grande', 'Cuiabá', 'Curitiba', 'Florianópolis', 'Fortaleza', 'Goiânia', 'João Pessoa', 'Macapá', 'Maceió', 'Manaus','Natal', 'Palmas', 'Porto Alegre', 'Porto Velho', 'Recife', 'Rio Branco', 'Rio de Janeiro', 'Salvador', 'São Luís', 'São Paulo','Teresina', 'Vitória')


@main_bp.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        origem = request.form.get('origem')
        destino = request.form.get('destino')
        resultados = executar_buscas(origem, destino)

        return render_template('index.html', capitais=capitais, resultados=resultados, origem=origem, destino=destino)
        

    return render_template('index.html', capitais=capitais)
