# send eamil to my husband
import yagmail
import settings
import requests

def send_mail(sender_mail, sender_password, sender_host, receiver_mail,
              subject, contents):
    """Send mail

    Parameters
    ----------
    sender_mail : string
        Email of sender
    sender_password : string
        Password of sender's mail
    sender_host : string
        Host of sender's mail provider
    receiver_mail : string
        Email of receiver
    subject : string
        Subject of mail
    contents : string
        Contents of mail
    """

    # Initializing the yagmail instance
    yag = yagmail.SMTP(user=sender_mail,
                       password=sender_password,
                       host=sender_host)
    # Sending the email
    yag.send(to=receiver_mail, subject=subject, contents=contents)


def generate_joke_from_api(token, random_joke_url, *disallowed_joke_types):
    """Generate jokes from "blagues API"

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


CONTENTS = generate_joke_from_api(settings.TOKEN, settings.RANDOM_JOKE_URL,
                                  *settings.DISALLOWED_JOKE_TYPES)
send_mail(settings.SENDER_MAIL, settings.SENDER_PASSWORD, settings.SENDER_HOST,
          settings.RECEIVER_MAIL, settings.SUBJECT, CONTENTS)
