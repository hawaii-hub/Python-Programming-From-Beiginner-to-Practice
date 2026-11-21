from restaurant import Restaurant

my_restaurant = Restaurant('long cangaun', 'china')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()


# 9.4就餐人数
print(f"number: {my_restaurant.number_served}")

my_restaurant.set_number_served(400)
print(f"number:{my_restaurant.number_served}")

my_restaurant.increment_number_served(50)
print(f"new_number:{my_restaurant.number_served}")


# 9.2三家餐馆·
print('')
# 9.2.1
xinjiang_restaurant = Restaurant('big plate chicken', 'jiang')
xinjiang_restaurant.describe_restaurant()

# 9.2.2
beijing_restaurant = Restaurant('beijing duck', 'jing')
beijing_restaurant.describe_restaurant()

# 9.2.3
hunan_restaurant = Restaurant('hunan spicy', 'xiang')
hunan_restaurant.describe_restaurant()