from types import TracebackType
from models.mail_content import JokeFactory, WeatherFactory
from models.mail import Mail


def main():
    joke = JokeFactory().create_content().generate_content()
    weather = WeatherFactory().create_content().generate_content()
    Mail().send_mail(contents=[joke, weather])


if __name__ == "__main__":
    main()