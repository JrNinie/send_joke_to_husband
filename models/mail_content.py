from abc import ABCMeta, abstractmethod
import settings
from tools.mail_content import generate_fr_joke_from_api

class MailContent(metaclass=ABCMeta):
    @abstractmethod
    def generate_content(self):
        pass

class Joke(MailContent):
    def __init__(self, language="french"):
        self.language = language

    def generate_content(self):
        if self.language in ("fr","french"):
            return generate_fr_joke_from_api(settings.TOKEN, settings.RANDOM_JOKE_URL,
                                  *settings.DISALLOWED_JOKE_TYPES)
        elif self.language in ("en", "english"):
            pass


class Weather(MailContent):
    def generate_content(self):
        pass

class MailContentFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_content(self):
        pass

class JokeFactory(MailContentFactory):
    def create_content(self):
        return Joke(language="french")

class WeatherFactory(MailContentFactory):
    def create_content(self):
        return Weather()