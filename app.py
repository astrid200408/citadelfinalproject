from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
@app.route("/index")
def index():

    apikey = ""
    #response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
    response = requests.get("https://pokeapi.co/api/v2/pokemon/ditto" + "?apikey="+apikey)
    data = response.json()
    image = data["sprites"]["front_default"]
    name = data["forms"][0]["name"]
    return render_template("index.html", poke_src=image, poke_nm = name)


if __name__ == "__main__":
    app.run()