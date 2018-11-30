from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/users',methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    loc_from_form = request.form['loc']
    lang_from_form = request.form['lang']
    message_from_form = request.form['message']
    return render_template("show.html", name_on_template=name_from_form, loc_on_template=loc_from_form, lang_on_template=lang_from_form, message_on_template=message_from_form)
if __name__ == "__main__":
    app.run(debug=True)
