import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Spain", True)
country_repository.save(country1)

country2 = Country("Finland", False)
country_repository.save(country2)

country3 = Country("Norway", False)
country_repository.save(country3)

city1 = City("Tenerife", country1, True)
city_repository.save(city1)

city2 = City("Helsinki", country2, False)
city_repository.save(city2)

city3 = City("Oslo", country3, False)
city_repository.save(city3)

all_countries = country_repository.select_all()
all_cities = city_repository.select_all()

for country in all_countries:
    print(country.__dict__)

for city in all_cities:
    print(city.__dict__)

city2.mark_visited()
city_repository.update(city2)
city2_test = city_repository.select(city2.id)

city_repository.delete(city2.id)
city2_test = city_repository.select(city2.id)



country2.mark_visited()
country_repository.update(country2)
country2_test = country_repository.select(country2.id)

country_repository.delete(country2.id)            
country2_test = country_repository.select(country2.id)

country2_cities = country_repository.cities(country2)



pdb.set_trace()
