import requests


def generate_fr_joke_from_api(token, random_joke_url, *disallowed_joke_types):
    """Generate jokes from "blagues API" (french jokes api)

    Parameters
    ----------
    token : string
        Token generated from "Blagues API"
    random_joke_url : string
        Url for fetching random joke without parameters
    disallowed_joke_types:  string
        Types(global, dev, dark, limit, beauf, blondes) want to be disallowed

    Returns
    -------
    string
        The random joke generated
    """

    # Generate api url with disallowed joke types
    url_with_params = None
    if disallowed_joke_types:
        url_with_params = random_joke_url + "?"
        for disallowed_type in disallowed_joke_types:
            url_with_params += "disallow=" + disallowed_type + "&"
        url_with_params = url_with_params.strip("&")
    else:
        url_with_params = random_joke_url

    # Get random joke
    response = requests.get(url_with_params,
                            headers={'Authorization': 'Bearer ' + token})
    data = response.json()
    return data["joke"] + " " + data["answer"]


def generate_current_weather(current_weather_url, location, api_secret_key):
    """Generate current weather from OpenWeather API

    Parameters
    ----------
    current_weather_url : string
        URL for current weather request
    location : string
        Location desired
    api_secret_key : string
        Secret personal API token

    Returns
    -------
    string
        Current weather in HTML format
    """
    current_weather = requests.get(
        f"{current_weather_url}?q={location}&appid={api_secret_key}&mode=html")

    return current_weather.text
