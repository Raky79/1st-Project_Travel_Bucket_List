import pdb
from models.city import City
from models.country import Country

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

country_repository.delete_all()
city_repository.delete_all()

country1 = Country("Spain", True)
country_repository.save(country1)
country2 = Country("Finland", False)
country_repository.save(country2)
country3 = Country("Norway", False)
country_repository.save(country3)

country_repository.select_all()

city = City("Barcelona", country1, True)
city_repository.save(city)

pdb.set_trace()