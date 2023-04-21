from sqlalchemy import ForeignKey
from helpers.database import db
from sqlalchemy.types import String
from flask_restful import fields
from model.EnderecoUsuario import endereco_fields

usuario_fields = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'email': fields.String(attribute='email'),
    'senha': fields.String(attribute='senha'),
    'endereco': fields.Nested(endereco_fields),
    'telefone': fields.String(attribute='telefone'),
    'observacoes': fields.String(attribute='observacoes')
}

class Usuario(db.Model):

    __tablename__ = "tb_usuario"

    id = db.Column('id', db.Integer, primary_key=True)
    nome = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True)
    senha = db.Column(db.String(30), unique=True, nullable=False)
    telefone = db.Column(db.String(11), nullable=False)
    observacoes = db.Column(db.String(700))

    EnderecoUsuario_id = db.Column(db.Integer, ForeignKey('tb_enderecoUsuario.id'))
    EnderecoUsuario = db.relationship("EnderecoUsuario", uselist=False)

    # Herança: Superclasse
    #tipo_usuario = db.Column('tipo_usuario', String(50))
    #_mapper_args_ = {'polymorphic_on': tipo_usuario}

    def __init__(self, nome, email, senha, endereco: EnderecoUsuario, telefone,  observacoes):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.telefone = telefone
        self.observacoes = observacoes

    def __repr__(self):
        return '<Nome: {}\n Email: {}\n Endereço: {}\n Telefone: {}\n Observacoes: {}>'.format(self.nome, self.email, self.endereco, self.telefone, self.observacoes)