from notebook import db

"""
Model for sql relations Note and Comment.
 - Note has attributes name and content
 - Comment has attributes timestamp, note and comment
"""


class Note(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    content = db.Column(db.String(255), nullable=False)


class Comment(db.Model):
    timestamp = db.Column(db.DateTime, primary_key=True)
    note = db.Column(db.String(120), db.ForeignKey('note.name'))
    comment = db.Column(db.String(255))
