from faker import Faker
import secrets
import string

fake = Faker()

random_email = fake.email()
random_name = fake.first_name()
random_password = ''.join(secrets.choice(string.ascii_letters + string.digits)
                          for _ in range(12))