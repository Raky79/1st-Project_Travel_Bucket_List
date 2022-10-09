from db.run_sql import run_sql
from models.country import Country
from models.city import City

def save(city):
    sql = "INSERT INTO cities(city_name) VALUES (%) RETURNING id"
    values = [city.city_name]
    results = run_sql(sql, values)
    city.id = results[0]['id']

def select_all():
    cities = []
    
    sql = "SELECT * FROM cities"
    results = run_sql(sql)
    for row in results:
        city = City(row['city_name'], row['id'])
        cities.append(city)
    return cities

def select(id): 
    city = None
    sql = "SELECT * FROM cities WHERE id = %"
    values = [id]
    result = run_sql(sql,values)[0]
    
    if result is not None: 
        city = City(result['city_name'], result['id'])
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)