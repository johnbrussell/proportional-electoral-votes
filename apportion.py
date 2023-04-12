from data.apportionment_data import populations_2010, populations_2020
from utils.apportionment_utils import apportion


apportionment_2020_573_seats = apportion(populations_2020, 573)
print("2020 with 573 seats:", apportionment_2020_573_seats)

apportionment_2020_653_seats = apportion(populations_2020, 653)
print("2020 with 653 seats:", apportionment_2020_573_seats)

apportionment_2010_573_seats = apportion(populations_2010, 573)
print("2010 with 573 seats:", apportionment_2010_573_seats)
