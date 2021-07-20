from models import db


class Grouping(db.Model):
    __tablename__ = 'grouping'

    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(512), unique=False, nullable=False)
    subcategory = db.Column(db.String(512), unique=False, nullable=False)

    def __repr__(self):
        return 'Category: {}; Subcategory: {}'.format(self.category, self.subcategory)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'category': self.category,
            'subcategory': self.subcategory
        }

    @staticmethod
    def get_grouping_by_subcategory():
        """
        Get list of countries filtered by currency code

        Parameters
        ----------
        subcategory
            Country's currency code

        Returns
        -------
        countries
            List of countries with specified currency code

        """
        grouping = Grouping.query.filter_by(subcategory="Mortgage")
        grouping.run()
        return grouping

    @staticmethod
    def add_grouping(new_grouping):
        db.session.add(new_grouping)
        db.session.commit()
        return 'pass'

    @staticmethod
    def delete_grouping(grouping):
        db.session.delete(grouping)
        db.session.commit()
        return 'pass'
