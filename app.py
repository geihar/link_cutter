from flask import Flask, url_for, redirect, render_template

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from src.models import Link, db
from src.forms import RegistrationForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Heroku config
        if Link.query.filter_by(link=form.link.data).count() == 5000:
            db.session.query(Link).delete()
            db.session.commit()
        if not Link.query.filter_by(link=form.link.data).first():
            link = Link(link=form.link.data)
            link.set_shortcut()
            db.session.add(link)
            db.session.commit()
        t = Link.query.filter_by(link=form.link.data).first()
        form.link.data = url_for("redirector", token=t.token, _external=True)
        return render_template("index.html", title="Cutter", form=form, shortcut=True)
    return render_template("index.html", title="Cutter", form=form)


@app.route("/<token>")
def redirector(token):
    link = Link.query.filter_by(token=token).first()
    if link:
        link.add_visits()
        db.session.add(link)
        db.session.commit()
        return redirect(link.link)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
