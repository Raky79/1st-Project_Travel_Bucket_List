import pdb
from models.city import City
from models.country import Country

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

country_repository.delete_all()
city_repository.delete_all()

country1 = Country("Spain", True)
country_repository.save(country1)

country2 = Country("Finland", False)
country_repository.save(country2)

country3 = Country("Norway", False)
country_repository.save(country3)

city1 = City("Barcelona", country1, True)
city_repository.save(city1)

city2 = City("Helsinki", country2, False)
city_repository.save(city2)

city3 = City("Oslo", country3, False)
city_repository.save(city3)

country_repository.select_all()

pdb.set_trace()

breakpoint()