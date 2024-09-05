from app import db

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(120), nullable=False)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<TodoItem {self.content}>'
