from app import db
from models import Pet

db.drop_all()
db.create_all()

dog_photo = "https://images.unsplash.com/photo-1587044022954-c3ecc844dedc?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxleHBsb3JlLWZlZWR8NjN8fHxlbnwwfHx8&auto=format&fit=crop&w=800&q=60"
cat_photo = "https://images.pexels.com/photos/615369/pexels-photo-615369.jpeg?auto=compress&cs=tinysrgb&dpr=2&w=500"
porcupine_photo = "https://images.unsplash.com/photo-1574671652898-fc04f34c7517?ixid=MXwxMjA3fDB8MHxzZWFyY2h8MzN8fHBvcmN1cGluZXxlbnwwfHwwfA%3D%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=800&q=60"


buster = Pet(name="Buster", species="dog", photo_url=dog_photo, age=2)
tammy = Pet(name="Tammy", species="cat", photo_url=cat_photo, age=3)
poke = Pet(name="Poke", species="porcupine", photo_url=porcupine_photo, age=7)


db.session.add_all([buster, tammy, poke])
db.session.commit()



