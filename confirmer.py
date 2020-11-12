import random


def create(count, registration, resident_city, clinic_city, borough, hospitalization, availability_type):
    traffic_type = ["음식점", "편의점", "카페", "문화마을", "시장", "해수욕장", "자택", "숙소", "버스", "PC방", "의료기관", "약국", "도보"]
    confirmation = []
    confirmed_registration = []
    file = open("3_확진자.txt", 'w')
    for i in range(count):
        while True:
            resident_index = random.randrange(len(registration))
            selected_registration = registration[resident_index]
            if registration[resident_index] not in confirmed_registration:
                break
        selected_resident_city = resident_city[resident_index]
        number = i + 1
        confirmation_created = f"{selected_resident_city}-{number}"

        while True:
            clinic_index = random.randrange(len(hospitalization))
            selected_clinic_city = clinic_city[clinic_index]
            if hospitalization[clinic_index] == availability_type[0] and selected_clinic_city == selected_resident_city:
                break

        date = f"2020-{random.randrange(1, 6):02d}-{random.randrange(1, 30):02d}"
        traffic_list = random.sample(traffic_type, 4)
        traffic = traffic_list[0]
        for j in range(1, len(traffic_list)):
            traffic += f"-{traffic_list[j]}"
        file.write(
            f"INSERT INTO 코로나.확진자 VALUES ("
            f"\'{confirmation_created}\', "
            f"\'{selected_registration}\', "
            f"\'{random.choice(availability_type)}\', "
            f"\'{date}\', "
            f"\'{traffic}\', "
            f"\'{selected_clinic_city} {borough[clinic_index]}\', "
            f"\'{selected_resident_city}\', "
            f"\'{random.choice(availability_type)}\', "
            f"{number}, "
            f"\'{date}\');\n"
        )
        confirmation.append(confirmation_created)
    file.close()
    return confirmation
