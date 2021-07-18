from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Expense(db.Model):
    __tablename__ = 'expense'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(512), unique=False, nullable=False)
    subcategory = db.Column(db.String(512), unique=False, nullable=False)

    def __repr__(self):
        return 'Category: {}; Subcategory: {}'.format(self.category, self.subcategory)
