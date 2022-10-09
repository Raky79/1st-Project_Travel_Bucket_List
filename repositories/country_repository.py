from db.run_sql import run_sql
from models.country import Country
from models.city import City

def save(country):
    sql = "INSERT INTO countries(country_name) VALUES (%) RETURNING id"
    values = [country.country_name]
    results = run_sql(sql, values)
    country.id = results[0]['id']

def select_all():
    countries = []
    
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for row in results:
        country = Country(row['country_name'], row['id'])
        countries.append(country)
    return countries

def select(id): 
    city = None
    sql = "SELECT * FROM countries WHERE id = %"
    values = [id]
    result = run_sql(sql,values)[0]
    
    if result is not None: 
        country = Country(result['country_name'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)


