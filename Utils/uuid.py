from uuid import uuid4

def generate_uuid():
    return (str(uuid4()),)

def format_existing_uuid(uuid):
    return (str(uuid),)