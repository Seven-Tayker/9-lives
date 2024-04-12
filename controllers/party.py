import os

from models.party import Party
from .files import save_file

from werkzeug.utils import secure_filename

from constants import UPLOAD_FOLDER

def get_all_parties():
    return Party.read()

def get_party_with_id(id):
    return Party.read(id)

def save_party(category, questions, session, duration, id=None, uploaded_files=None):
    if id != None:
        party = get_party_with_id(id)
        party.category, party.questions, party.session, party.duration = (
            category, questions, session, duration
        )
    else:
        party = Party(
            category=category,questions=questions, 
            session=session, duration=duration
        )

    party.save()

    for file in uploaded_files:
        file_name = secure_filename(file.filename)

        save_file(party=party.id, path=file_name)

        file.save(
            os.path.join(UPLOAD_FOLDER, file_name)
        )

    return party
    
def delete_party(id):
    party = get_party_with_id(id)
    party.delete()