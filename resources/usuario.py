from model.EnderecoUsuario import EnderecoUsuario
from model.error import Error, error_campos
from model.usuario import usuario_fields
from helpers.database import db
from sqlalchemy import exc
from flask_restful import Resource, marshal_with, reqparse, current_app, marshal


parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, help="Nome é campo obrigatório.")
parser.add_argument('email', required=True, help="Email é campo obrigatório.")
parser.add_argument('senha', required=True, help="Senha é campo obrigatório.")
parser.add_argument('endereco', type=dict, required=True)
parser.add_argument('telefone', required=True, help="Telefone é campo obrigatório.")



class Usuario(Resource):
    @marshal_with(usuario_fields)
    def get(self):
        current_app.logger.info("Get - Usuarios ")
        usuario = Usuario.query\
            .order_by(Usuario.email)\
            .all()
        return usuario, 200

    def post(self):
        current_app.logger.info("Post - Usuários")

        try:
            # JSON
            args = parser.parse_args()
            nome = args['nome']
            email = args['email']
            senha = args['senha']
            endereco = args['endereco']
            telefone = args['telefone']

            logradouro = endereco['logradouro']
            numero = endereco['numero']
            cidade = endereco['cidade']
            estado = endereco['estado']

            endereco_usr = EnderecoUsuario(logradouro, numero, cidade, estado)

            # Usuario
            usuario = Usuario(nome, email, senha, endereco_usr, telefone)
            # Criação do Usuario.
            db.session.add(usuario)
            db.session.commit()

        except exc.SQLAlchemyError as err:
            current_app.logger.error(err)
            erro = Error(1, "Erro ao adicionar no banco de dados, consulte o adminstrador",
                         err.__cause__())
            return marshal(erro, error_campos), 500

        return 200
    
    def put(self, usuario_id):
        current_app.logger.info("Put - Usuarios")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Usuario: %s:" % args)
            # Evento
            nome = args['nome']
            email = args['email']
            senha = args['senha']
            endereco = args['endereco']
            telefone = args['telefone']

            Usuario.query \
                .filter_by(id=usuario_id) \
                .update(dict(nome=nome, email=email, senha=senha, endereco=endereco, telefone=telefone))
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 200
    
    def delete(self, usuario_id):
        current_app.logger.info("Delete - Usuarios: %s:" % usuario_id)
        try:
            Usuario.query.filter_by(id=usuario_id).delete()
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return 200