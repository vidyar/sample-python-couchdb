from couchdbkit import Server

class Couch():
    def __init__(self):
        self.server = Server()
        self.server.delete_db('test')
        self.db = self.server.get_or_create_db('test')

    def populate(self):
        things = [
            {"name": "Vishnu"},
            {"name": "Lakshmi"},
            {"name": "Ganesha"},
            {"name": "Krishna"},
            {"name": "Murugan"}
        ]
        self.db.save_docs(things)

    def count(self):
        return self.db.all_docs().count()

if __name__ == "__main__":
    couch = Couch()
    couch.populate()
    print(couch.count())
