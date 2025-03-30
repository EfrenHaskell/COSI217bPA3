#!usr/bin/env Python
"""
notes file for Notebook implementation
"""

__author__ = "Efren Haskell"
__email__ = "efrenhask@gmail.com"

from notebook import db
from notebook.model import Note, Comment
from datetime import datetime


def add(name: str, content: str):
    """
    Add new note
     - A note is composed of a name and content
    :param name:
    :param content:
    :return:
    """
    new_note = Note(name=name, content=content)
    db.session.add(new_note)
    db.session.commit()


def add_comment(name: str, comment: str):
    """
    Create new comment entity
    """
    new_comment = Comment(timestamp=datetime.now(), note=name, comment=comment)
    db.session.add(new_comment)
    db.session.commit()


def delete_note(name: str):
    """
    Delete note and all comments attributed with it
    """
    db.session.delete(Note.query.filter_by(name=name).first())
    for comment in Comment.query.filter_by(note=name):
        db.session.delete(comment)
    db.session.commit()


def find(query_term: str) -> list[str]:
    """
    find note that has query_term in its contents
    :param query_term:
    :return:
    """
    all_notes = Note.query.all()
    return [note.name for note in all_notes if query_term in note.content]


def get_comments(name: str):
    """
    Returns all comments in sqlite db for specified note name
    """
    return Comment.query.filter_by(note=name)


def get_note(name: str):
    """
    Return note contents by name
    :param name:
    :return:
    """
    note = Note.query.filter_by(name=name).first()
    if not note:
        return ""
    return note.content


def notes() -> list[str]:
    """"
    Return a list of all note names
    """
    all_notes = Note.query.all()
    return [note.name for note in all_notes]
