from app import db

class Project(db.Model):
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    demo_url = db.Column(db.String(200), nullable=False)
    github_url = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Project {self.title}>'

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_category(cls, category_id):
        return cls.query.filter_by(category_id=category_id).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)