from flask import Blueprint, request

from controllers.paeties import *

parties_view = Blueprint('parties', __name__, url_prefix='/parties')

@exams_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_parties()
    else:
        submitted_data = request.POST
        files = request.files.getlist("files")

        category, session, duration, questions = (
            submitted_data['category'], submitted_data['session'], 
            submitted_data['duration'], submitted_data['questions']
        )

        return save_party(category, questions, session, duration, uploaded_files=files)
    
@exams_view.route('/<id>', methods=['GET', 'POST'])
def get_or_update_instance(id):
    if request.method == 'GET':
        return get_exam_with_id(id)
    pass