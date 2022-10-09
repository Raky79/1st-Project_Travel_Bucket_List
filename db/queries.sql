SELECT countries.name, cities.name FROM countries
INNER JOIN cities
ON cities.country_id = countries.id
