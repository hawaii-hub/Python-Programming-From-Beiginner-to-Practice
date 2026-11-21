class Restaurant:
    """餐馆"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性restaurant_name和cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 100

    def describe_restaurant(self):
        """打印前两项信息"""
        print(f"restaurant_name: {self.restaurant_name}")
        print(f"cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """指出餐馆营业状态"""
        print("The restaurant now is opening")

    def set_number_served(self, mileage):
        """设置用餐人数"""
        self.number_served = mileage

    def increment_number_served(self, miles):
        """用来让人数递增"""
        self.number_served += miles


class IceCreamStand(Restaurant):
    """冰淇凌店的特殊之处"""

    def __init__(self, restaurant_name, cuisine_type, *flavors):
        """
        先初始化父类的属性,再初始化冰淇凌店特有的属性
        """

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def describe_flavors(self):
        """打印各种冰淇凌的口味"""
        print("There are have some defyrent flavors:")
        for f in self.flavors:
            print(f" -{f}")


my_restaurant = IceCreamStand('long cangaun', 'china', 'a', 's', 'd')

print(my_restaurant.restaurant_name)
print(my_restaurant.cuisine_type)        

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.describe_flavors()  #如果加入print