import json

from flask import Flask
from flask import request


app = Flask(__name__)

login_page_str = '''
<html>
<head>
<title>Blum Mental Hash Challenge Login</title>
</head>

<body>

<h1>Blum Mental Hash Challenge Login</h1>

<table>
<form action="/authenticate" method="POST">
    <tr>
        <td style="text-align: right;">Login: </td>
        <td><input name="login" type="text"></td>
    </tr>
    <tr>
        <td style="text-align: right;">Password: </td>
        <td><input name="password" type="password"></td>
    </tr>
    <tr>
        <td></td>
        <td><input type="submit" value="Submit"></td>
    </tr>
</form>
</table>

<p>
Site code and directions can be found at GitHub.com at:<br />
<a href="https://github.com/lmandres/BlumMentalHashChallenge">https://github.com/lmandres/BlumMentalHashChallenge</a>
</p>

</body>
</html>
'''

authenticate_fail_page_str = '''
<html>
<head>
<title>Blum Mental Hash Challenge Login</title>
</head>

<body>

<h1>Unable to authenticate.</h1>

</body>
</html>
'''

authenticate_succeeded_page_str = '''
<html>
<head>
<title>Blum Mental Hash Challenge Login</title>
</head>

<body>

<h1>Authenticated!!!</h1>

</body>
</html>
'''

challenge_settings = {}
with open("challenge_settings.json", "r") as filein:
    challenge_settings = json.load(filein)

def blum_hash_word(input_word, alphanumeric, alphanumbmap, digits):

    def get_map_index(map_char):

        map_dec_values = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
        }
         
        map_index = alphanumeric.upper().index(map_char.upper())
        map_value = alphanumbmap[map_index]

        return map_dec_values[map_value]

    def get_map_digit(map_index):
        map_hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        return digits[(digits.lower().index(map_hex_digits[map_index].lower()) + 1) % 10]

    plaintext = input_word.upper()
    hashtext = ""

    for i in range(0, len(plaintext), 1):
        if i == 0:
            hashtext += get_map_digit((get_map_index(plaintext[0]) + get_map_index(plaintext[-1])) % 10)
        else:
            hashtext += get_map_digit((get_map_index(hashtext[i-1]) + get_map_index(plaintext[i])) % 10)
    
    return hashtext

@app.route("/")
def blum_redirect_default_page():
    return app.redirect("/login")

@app.route("/login")
def blum_login_page():
    return login_page_str

@app.route("/authenticate", methods=["POST"])
def blum_authenticate_page():

    return_page = authenticate_fail_page_str

    try:
        passwordhash = blum_hash_word(
            challenge_settings[request.form["login"].lower()]["password"],
            challenge_settings[request.form["login"].lower()]["alphanumeric"],
            challenge_settings[request.form["login"].lower()]["alphanumbmap"],
            challenge_settings[request.form["login"].lower()]["digits"]
        )
        if passwordhash == request.form["password"]:
            return_page = authenticate_succeeded_page_str
    except:
        pass

    return return_page

if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="localhost", port=8080, debug=True)