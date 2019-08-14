import os
from flask import Flask, render_template, request, flash
import json

app = Flask(__name__)
app.secret_key = "its_secret"

@app.route('/')
def index():
    with open("data/data.json", "r") as file :
        content_of_file = json.load(file)
        return render_template("index.html", bg_img="/static/img/home-bg.jpg", title="Clean Blog", sub_title="A Blog Theme by Start Bootstrap", content_list = content_of_file)

@app.route('/about')
def about():
    return render_template("about.html",bg_img="/static/img/about-bg.jpg", title="About", sub_title="This is what I do")

@app.route('/post')
def post():
    return render_template("post.html" ,bg_img="/static/img/post-bg.jpg", title="Man must explore, and this is exploration at its greatest", sub_title="Problems look mighty small from 150 miles up", posted_by="Posted by Start Bootstrap on August 24, 2019")
    
@app.route('/contact', methods=["GET","POST"])
def contact():
    if request.method == "POST":
        file = open("user_info.txt", "a")
        file.write("name:{}, email:{}, phone:{}, message:{}\n".format
                    (request.form['name'], request.form['email'], 
                    request.form['phone'], request.form['message']))
        file.close()
        flash("Hey {}, Your for has been successfully submited".format(request.form['name']))
    return render_template("contact.html", bg_img="/static/img/contact-bg.jpg" , title="Contact", sub_title="Have questions? I have answers.")

@app.route('/about/<actor_name>')
def about_actor(actor_name):
    with open("data/data.json", "r") as file :
        content_of_file = json.load(file)
        single_actor = {}
        for actor in content_of_file:
            if actor['url'] == actor_name:
                single_actor = actor
                banner_title = single_actor['name']
    if single_actor == {}:
        single_actor = {"message":"No Data Available"}
        banner_title = "Error"
    return render_template("about_actor.html", bg_img="/static/img/home-bg.jpg" , title = banner_title, sub_title="", content = single_actor)



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)