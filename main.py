from models.mail_content import JokeFactory
from models.mail import Mail


def main():
    joke = JokeFactory().create_content().generate_content()
    Mail().send_mail(content=joke)


if __name__ == "__main__":
    main()