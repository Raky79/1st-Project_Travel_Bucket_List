from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/countries_index.html", all_countries = countries)
