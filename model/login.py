from datetime import datetime
from helpers.database import db
from model.usuario import Usuario, usuario_fields
from flask_restful import fields

login_fields = {
    'id': fields.Integer(attribute='id'),
    'usuario': fields.Nested(usuario_fields),
    'datahora': fields.String(attribute='datahora'),
    'key': fields.String(attribute='key')
}


class Login(db.Model):

    _tablename_ = 'tb_login'

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("tb_usuario.id"))
    datahora = db.Column(db.DateTime, default=datetime.now)
    key = db.Column(db.String(40))

    # Relacionamento com Usuario
    usuario = db.relationship("Usuario", uselist=False)

    def _init_(self, usuario: Usuario, datahora, key):
        self.datahora = datahora
        self.usuario = usuario
        self.key = key

    def _repr_(self):
        return '<Login data: {}>'.format(self.datahora)