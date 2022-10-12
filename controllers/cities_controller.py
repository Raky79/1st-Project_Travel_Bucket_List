from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.city import City
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

cities_blueprint = Blueprint("cities", __name__)

#index 

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    return render_template("cities/cities_index.html", all_cities = city_repository.select_all())

#show
@cities_blueprint.route("/cities/<id>", methods=['GET'])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/cities_show.html',
                            city = city)

@cities_blueprint.route('/cities/<id>/edit', methods=['GET'])
def edit_city(id):
    city = city_repository.select(id)
    return render_template('cities/edit.html', city=city)

@cities_blueprint.route('/cities/<id>', methods=['POST'])
def update_city(id):
    name = request.form['name']
    visited = request.form['visited']
    city = City(name, visited, id)
    city_repository.update(city)
    return redirect('/cities')

# @cities_blueprint.route("/countries/<id>", methods = ['POST'])
# def create_city():
#     name = request.form['name']
#     country = country_repository.select(request.form['country_id'])
#     city = City(name, country)
#     city_repository.save(city)
#     return redirect('/cities')
