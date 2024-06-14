import faker
from random import randint


def generate_fake_data(
    number_users: int = 1, number_task: int = 1, number_status: int = 1
) -> tuple:
    """
    This function generates fake user data and task data.

    Parameters:
    number_users (int): The number of fake users to generate. Default is 1.
    number_task (int): The number of fake tasks to generate. Default is 1.
    number_status (int): The number of fake statuses to generate. Default is 1.

    Returns:
    tuple: A tuple containing two lists. The first list contains tuples of fake user data (name, email).
           The second list contains tuples of fake task data (task_title, task_description, status, user_id).

    Example:
    >>> user, task = generate_fake_data(5, 20, 3)
    >>> print(user, task, sep="\n")
    """
    fake_users = []
    fake_tasks = []

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

    return fake_users, fake_tasks


if __name__ == "__main__":
    NUMBER_USERS = 5
    NUMBER_TASK = 20
    NUMBER_STATUS = 3
    user, task = generate_fake_data(NUMBER_USERS, NUMBER_TASK, NUMBER_STATUS)
    print(user, task, sep="\n")
