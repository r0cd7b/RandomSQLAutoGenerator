import random


def create(count, registration, company):
    week = ["None", "월화수목금"]
    rating = ["None", "KF80", "KF94", "KF99"]
    price = [1000, 1500, 2000, 2500]
    file = open("5_마스크공급.txt", 'w')
    mask = random.randrange(len(rating))
    for i in range(count):
        selected_week = random.choice(week)
        if selected_week == week[0]:
            mask = random.randrange(len(rating))
            selected_rating = rating[mask]
            selected_price = price[mask]
        else:
            selected_week = random.choice(week[1])
            selected_rating = rating[1]
            selected_price = price[1]
        file.write(
            f"INSERT INTO 코로나.마스크공급 VALUES ("
            f"\'{random.choice(registration)}\', "
            f"\'{random.choice(company)}\', "
            f"\'2020-{random.randrange(1, 6):02d}-{random.randrange(1, 30):02d}\', "
            f"{i + 1}, "
            f"\'{selected_rating}\', "
            f"{selected_price}, "
            f"\'{selected_week}\');\n"
        )
    file.close()
