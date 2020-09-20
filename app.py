from flask import Flask, session, url_for, redirect, render_template

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from src.models import Link, db
from src.forms import RegistrationForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        link = Link(link=form.link.data)
        link.set_token()
        db.session.add(link)
        db.session.commit()
        token = Link(link=form.link.data).token
        return render_template("index.html", title="Home", token=token)
    if "token" in session:
        data = True
        return render_template("index.html", title="Home", data=data)
    return render_template("index.html", title="Home", form=form)


@app.route("/<token>")
def authentication(token):
    user = User.query.filter_by(token=token).first()
    if user:
        user.add_visits()
        db.session.add(user)
        db.session.commit()
        session["token"] = token

    return redirect(url_for("index"))
if __name__ == '__main__':
    app.run()
