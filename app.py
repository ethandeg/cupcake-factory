from flask import Flask, request, render_template, redirect, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcake_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = 'CodyIsTheBestDoggy92384721'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


connect_db(app)
db.create_all()


@app.route('/')
def show_home_page():
    form = AddCupcakeForm()
    return render_template('home.html', form=form)


@app.route('/api/cupcakes')
def show_cupcakes():
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    return jsonify(cupcakes=all_cupcakes)


@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
    form = AddCupcakeForm()
    # import pdb
    # pdb.set_trace()
    if form.validate_on_submit():
        flavor = request.json['flavor']
        size = request.json['size']
        rating = request.json['rating']
        if request.json['image']:
            image = request.json['image']
        else:
            image = None
        new_cupcake = Cupcake(flavor=flavor, size=size,
                              rating=rating, image=image)
        print(new_cupcake)
        db.session.add(new_cupcake)
        db.session.commit()
        response_json = jsonify(cupcake=new_cupcake.serialize())
        return (response_json, 201)
    else:
        return render_template('home.html')


@app.route('/api/cupcakes/<int:id>', methods=['PATCH'])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize())


@app.route('/api/cupcakes/<int:id>', methods=['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message='deleted')
