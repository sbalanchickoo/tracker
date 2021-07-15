from tracker import db


class Expense(db.Model):
    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(512), unique=False, nullable=False)
    def __repr__(self):
        return 'Item: {}'.format(self.item)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'item': self.item
        }

