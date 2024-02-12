from flask import Flask, redirect, url_for, render_template, request, session, flash

app = Flask(__name__, static_url_path='/static')
app.secret_key = "ochio"

#Home page
@app.route("/", methods= ["GET", "POST"])
def home():
    if request.method == "POST":
        return redirect(url_for("results"))
    else:
        return render_template("home.html")

#Login page
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Logged in successfully!", "info")
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in", "info")
            return redirect(url_for("user"))
        return render_template("login.html")
    
#Logout page
@app.route("/logout/")
def logout():
    session.pop("user", None)
    flash("Logged out successfully", "info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)