import random


def create(count, city_type, borough_type):
    person_type = ["김이박정최조강윤장임", "민서예지도시주하채수", "준연우현원은호후유훈"]
    gender_type = ["남", "여"]
    number = []
    city = []
    file = open("1_국내거주자.txt", 'w')
    for i in range(count):
        while True:
            year = random.randrange(1920, 2020)
            number_created = f"{year % 100:02d}{random.randint(1, 12):02d}" \
                             f"{random.randint(1, 28):02d}-{random.randrange(10000000):07d}"
            if number_created not in number:
                break
        city_index = random.randrange(len(city_type))
        selected_city = city_type[city_index]
        file.write(
            f"INSERT INTO 코로나.국내거주자 VALUES ("
            f"\'{number_created}\', "
            f"\'{selected_city} {random.choice(borough_type[city_index])}\', "
            f"\'{random.choice(person_type[0])}{random.choice(person_type[1])}{random.choice(person_type[2])}\', "
            f"\'010-{random.randrange(10000):04d}-{random.randrange(10000):04d}\', "
            f"\'{random.choice(gender_type)}\', "
            f"{2020 - year});\n")
        number.append(number_created)
        city.append(selected_city)
    file.close()
    return number, city
