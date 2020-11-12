import random


def create(count, registration, city, borough):
    file = open("6_외래진료.txt", 'w')
    for i in range(count):
        city_index = random.randrange(len(city))
        file.write(
            f"INSERT INTO 코로나.외래진료 VALUES ("
            f"\'{random.choice(registration)}\', "
            f"\'{city[city_index]} {borough[city_index]}\', "
            f"{i + 1}, "
            f"\'2020-{random.randrange(1, 6):02d}-{random.randrange(1, 30):02d}\');\n"
        )
    file.close()
