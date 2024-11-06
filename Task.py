class Task:
    
    def __init__(self, title, description, complated=False):
        self.title = title
        self.description = description
        self.complated = complated

    def to_dict(self):
        return{
            'title': self.title,
            'description': self.description,
            'complated': self.complated
        }

    @classmethod    
    def from_dict(cls,data):
        return cls(data['title'], data['description'], data.get('complated', False))
    