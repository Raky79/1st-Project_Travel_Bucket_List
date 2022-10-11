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
                           country_cities = country_repository.cities(country))
