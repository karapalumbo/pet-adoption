from flask import Flask, render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///adopt"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config["SECRET_KEY"] = "seeecret"

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()


@app.route('/')
def list_of_pets():
    """Shows list of pets."""

    pets = Pet.query.all()
    return render_template('list_pets.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Form to add a new pet."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        p = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(p)
        db.session.commit()
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def display_edit_form(pet_id):
    """ For to edit pet info."""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        return redirect('/')

    else:
        return render_template("edit_pet_form.html", form=form, pet=pet)


