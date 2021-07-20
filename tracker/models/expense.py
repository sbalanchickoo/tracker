from models import db


class Expense(db.Model):
    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    payee = db.Column(db.String(512), unique=False, nullable=False)

    def __repr__(self):
        return 'Payee: {}'.format(self.payee)
