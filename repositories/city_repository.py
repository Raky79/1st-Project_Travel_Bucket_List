from db.run_sql import run_sql
from models.country import Country
from models.city import City
from repositories import country_repository

def save(city):
    sql = "INSERT INTO cities(city_name, country_id, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [city.city_name, city.country.id, city.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    city.id = id
    return city

def select_all():
    cities = []
    
    sql = "SELECT * FROM cities"
    results = run_sql(sql)

    for row in results:
        country = country_repository.select(row['country_id'])
        city = City(row['city_name'], country, row['visited'], row['id'])
        cities.append(city)
    return cities

def select(id): 
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)

    if results:
        result = result[0]
        country = country_repository.select(result["country_id"])
        city = City(result['city_name'], country, result['visited'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)