import json
from flask import Blueprint, jsonify, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            flash('Note added!', category='success')
            db.session.add(new_note)
            db.session.commit()
  
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    # take in data from a POST request and load as a python dict named note
    note = json.loads(request.data)
    # access note's id attribute
    noteId = note['noteId']
    # search in database for note
    note = Note.query.get(noteId)
    # validate that note was posted by current user then delete it
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})
