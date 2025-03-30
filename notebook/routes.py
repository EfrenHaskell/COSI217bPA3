from flask import render_template, request, redirect, jsonify, url_for
from notebook import app, notes


@app.get("/")
def home_page():
    """
    Renders main page for adding new notes, searching by query and viewing all note names
    :return:
    """
    return render_template("index.html")


@app.route("/get_notes", methods=["GET"])
def get_notes():
    """
    Return Json object listing all note names
    :return:
    """
    return jsonify(notes.notes())


@app.route("/note", methods=["GET", "DELETE", "POST"])
def note_page():
    """
    Render page based on route "name", displays note name and contents
    :return:
    """
    name = request.args.get("name", type=str)
    if request.method == "DELETE":
        # delete request for removing note
        notes.delete_note(name)
        return "success"
    elif request.method == "POST":
        # post request for adding comment
        comment_content = request.form['content']
        notes.add_comment(name, comment_content)
    contents = notes.get_note(name)
    comments = notes.get_comments(name)
    return render_template("note.html", note_name=name, note_contents=contents, comments=comments)


@app.route("/add_note", methods=["POST"])
def add_note():
    """
    Post method for adding new note
    :return:
    """
    new_element = request.get_json()
    notes.add(new_element["name"], new_element["content"])
    return redirect("/")


@app.route("/search")
def search():
    """
    Search functionality, returns Json object for find output
    :return:
    """
    query_term = request.args.get('term', type=str)
    search_results = notes.find(query_term)
    return jsonify(search_results)
