from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__)


@app.route("/assests/<path:filename>")
def assests(filename):
    return send_from_directory("assests", filename)

# LOGIN PAGE
@app.route("/", methods=["GET","POST"])
def login():

    if request.method == "POST":
        return render_template("details.html")

    return render_template("login.html")


# DETAILS PAGE (BHK + LOCATION + USER DETAILS)
@app.route("/recommendation", methods=["POST"])
def recommendation():

    bhk = request.form.get("bhk")
    city = request.form.get("city")
    living = request.form.get("living")
    house_type = request.form.get("house_type")

    # logic for houses
    if living == "Bachelors":
        houses = 5
    else:
        houses = 12

    # logic for rent
    if house_type == "Luxury":
        rent = 45000
    else:
        rent = 15000

    return render_template(
        "recommendation.html",
        bhk=bhk,
        city=city,
        houses=houses,
        rent=rent
    )


if __name__ == "__main__":
    app.run(debug=True)
