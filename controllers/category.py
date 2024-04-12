from models.category import Category

def get_all_categories():
    categories = Category.read()

    return [ category.toJSON() for category in categories ]

def get_category_with_id(id):
    return Category.read(id).toJSON()

def save_category(name, id=None):
    if id != None:
        
        category = get_category_with_id(id)
        category.name = name

    else:
        category = Category(name=name)
    
    category.save()

    return category.toJSON()

def delete_category(id):
    category = get_category_with_id(id)
    category.delete()

    return subject.toJSON()
