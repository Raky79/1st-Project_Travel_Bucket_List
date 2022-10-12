from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    return render_template("countries/countries_index.html",
                           all_countries = country_repository.select_all())

#SHOW
@countries_blueprint.route("/countries/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/countries_show.html',
                           country = country, 
                           country_cities = country_repository.cities(country), 
                           all_countries = country_repository.select_all())

@countries_blueprint.route('/countries', methods=['POST'])
def create_country():
    print(request.form)
    name = request.form['name'] 
    visited = True if 'visited' in request.form else False
    newcountry = Country(name=name, visited=visited)
    country_repository.save(newcountry)
    return redirect('/countries')

@countries_blueprint.route('/countries/<id>/edit', methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country=country)

#UPDATE

@countries_blueprint.route('/countries/<id>', methods=['POST'])
def update_country(id):
    name = request.form['name']
    visited = request.form['visited']
    country = Country(name, visited, id)
    country_repository.update(country)
    return redirect('/countries')

#DELETE

@countries_blueprint.route("/countries/<id>/delete", methods=['GET'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')    

