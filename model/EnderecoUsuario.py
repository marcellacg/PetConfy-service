from helpers.database import db
from flask_restful import fields


endereco_fields = {
    'id': fields.Integer(attribute='id'),
    'logradouro': fields.String(attribute='logradouro'),
    'numero': fields.String(attribute='numero'),
    'cidade': fields.String(attribute='cidade'),
    'estado': fields.String(attribute='estado')
}


class EnderecoUsuario(db.Model):

    __tablename__ = "tb_enderecoUsuario"

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String, nullable=False)
    numero = db.Column(db.String(9), nullable=False)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(2), nullable=False)

    #usuario_id = db.Column(db.Integer, db.ForeignKey("tb_usuario.id"))

    def __init__(self, logradouro, numero, cidade, estado):
        self.logradouro = logradouro
        self.numero = numero
        self.cidade = cidade
        self.estado = estado

    def __repr__(self):
        return '<Logradouro: {}\n Numero: {}\n Cidade: {}\n Estado: {}>'.format(self.logradouro, self.numero, self.cidade, self.estado)