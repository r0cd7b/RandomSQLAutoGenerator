import random


def create(count, city_type, borough_type, availability_type, phone):
    clinic_type = ["병원", "보건소"]
    city = []
    borough = []
    hospitalization = []
    address = []
    file = open("2_진료소.txt", 'w')
    for i in range(count):
        while True:
            city_index = random.randrange(len(city_type))
            selected_city = city_type[city_index]
            selected_borough = random.choice(borough_type[city_index])
            address_created = f"{selected_city} {selected_borough}"
            if address_created not in address:
                break
        while True:
            phone_created = f"0{random.randrange(100):02d}-{random.randrange(1000):03d}-{random.randrange(10000):04d}"
            if phone_created not in phone:
                break
        hospitalization_index = random.randrange(len(availability_type))
        selected_hospitalization = availability_type[hospitalization_index]
        file.write(
            f"INSERT INTO 코로나.진료소 VALUES ("
            f"\'{address_created}\', "
            f"\'{phone_created}\', "
            f"\'{selected_hospitalization}\', "
            f"\'{random.choice(availability_type)}\', "
            f"\'{selected_borough}{clinic_type[hospitalization_index]}\');\n")
        city.append(selected_city)
        borough.append(selected_borough)
        hospitalization.append(selected_hospitalization)
        address.append(address_created)
        phone.append(phone_created)
    file.close()
    return city, borough, hospitalization
