import json

from app.Tools.Hash import Hash

class User:
    encrypted_fields = ['password']

    def __init__(self, attributes: dict, db_handler):
        self.set_name(attributes.name or 'John DOE')
        self.set_email(attributes.email or 'email@example.com')
        self.set_password(attributes or 'password')
        self.set_db_handler(db_handler)

    def set_name(self, name):
        self.name = name
        return self

    def set_email(self, email):
        self.email = email
        return self
    
    def set_password(self, password):
        self.password = password
        return self
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_db_handler(self):
        return self.db_handler

    def set_db_handler(self, db_handler):
        self.db_handler = db_handler
        return self
    
    def save(self):
        if(self.name is not '' and self.email is not '' and self.password is not ''):
            return self.save_model()
        return False
    
    def save_model(self):
        self.db_handler.insert_one(self.to_json())

    def to_json(self):
        return json.dumps({
            'name': self.ensure_protected_field('name', self.name),
            'email': self.ensure_protected_field('email', self.email),
            'password': self.ensure_protected_field('password', self.password)
        })

    def ensure_protected_field(self, attribute, value):
        if(attribute in self.encrypted_fields):
            return Hash.make(value)
        return value

    def find(email):
        # Recherche d'un utilisateur avec email
        # retourner une instance User
        return User({'name': 'Mhmoud', 'email': 'zba@zba.com', 'password': 'sjdfhjdhgkjdghkfjdkgsdkfjhg'}, db_handler=)