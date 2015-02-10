from sqlalchemy_declarative import Person, Base, Address
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sqlalchemy_example.db')
Base.metadata.bind = engine
from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker()
DBSession.bind = engine
session = DBSession()
print ("""===============================================

""")
print("We now have a database session")
print("""try the following commands:
 """)
print(""">>> session.query(Person).all()
>>> person = session.query(Person).first()
>>> person.name
>>> address = session.query(Address).filter(Address.person == person).one()
>>> address.post_code

You can create a new person as follows:
>>> new_person = Person(name='john brown')
>>> session.add(new_person)
>>> session.commit()

=============================================="""
)
import pdb;pdb.set_trace()
