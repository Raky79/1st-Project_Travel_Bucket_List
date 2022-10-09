from db.run_sql import run_sql
from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries(country_name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.country_name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


def select_all():
    countries = []
    
    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['country_name'], row['visited'], row['id'])
        countries.append(country)
    return countries

def select(id): 
    city = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql,values)[0]
    
    if result is not None: 
        country = Country(result['country_name'], result['visited'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country): 
    sql = "UPDATE countries SET (country_name, visited) = (%s, %s) WHERE id = %s"
    values = [country.country_name, country.visited, country.id]
    run_sql(sql, values)


