import faker
from random import randint

NUMBER_USERS = 5
NUMBER_TASK = 20
NUMBER_STATUS = 3


def generate_fake_data(number_users=1, number_task=1, number_status=1) -> tuple():
    fake_users = []
    fake_tasks = []
    status = [("new",), ("in progress",), ("completed",)]

    fake_data = faker.Faker()

    for _ in range(number_users):
        fake_users.append((fake_data.name(), fake_data.email()))

    for _ in range(number_task):
        fake_tasks.append(
            (
                fake_data.sentence(nb_words=6),
                fake_data.paragraph(nb_sentences=3),
                randint(1, number_status),
                randint(1, number_users),
            )
        )

    return status, fake_users, fake_tasks


if __name__ == "__main__":
    status, user, task = generate_fake_data(NUMBER_USERS, NUMBER_TASK, NUMBER_STATUS)
    print(status, user, task, sep="\n")
