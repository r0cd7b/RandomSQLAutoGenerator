import random


def create(count, city_type, borough_type, phone):
    name_type = ["푸주지금삼지현리가", "른민영호성대안야"]
    number = []
    file = open("4_판매처.txt", 'w')
    for i in range(count):
        while True:
            number_created = f"{random.randrange(1000):03d}-{random.randrange(100):02d}-{random.randrange(100000):05d}"
            if number_created not in number:
                break
        while True:
            phone_created = f"0{random.randrange(100):02d}-{random.randrange(1000):03d}-{random.randrange(10000):04d}"
            if phone_created not in phone:
                break
        city_index = random.randrange(len(city_type))
        file.write(
            f"INSERT INTO 코로나.판매처 VALUES ("
            f"\'{number_created}\', "
            f"\'{random.choice(name_type[0])}{random.choice(name_type[1])}약국\', "
            f"\'{city_type[city_index]} {random.choice(borough_type[city_index])}\', "
            f"\'{phone_created}\');\n"
        )
        number.append(number_created)
    file.close()
    return number
