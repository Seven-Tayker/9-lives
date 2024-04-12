from models.files import File

def get_all_files():
    return File.read()

def get_file_with_id(id):
    return File.read(id)

def save_file(party, path, id=None):
    if id != None:
        file = get_file_with_id(id)
        file.party, file.path = party, path

    else:
        file = File(
            party=party, path=path
        )

    file.save()

def delete_file(id):
    file = get_file_with_id(id)
    file.delete()