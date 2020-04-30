@app.route("/profile")
def profile():
    return render_template("public/profile.html")