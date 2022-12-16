import re
from app import app
from flask import render_template, request
from urllib import request as UrlRequest


@app.route('/')
def form():
    return render_template("index.html")


@app.route("/result", methods=["POST"])
def result():
    print(request.form)
    link = request.form.get("url") # getting url value from the form using flask request lib
    response = UrlRequest.urlopen(link) # upload page by link from the form
    string = response.read().decode('utf-8') # decode uploaded page to utf-8
    pattern = r'<p>[\w+\s+-]+<b>[\w+\s+]+@[\w+\.]+<\/b>[\n?]+<\/p>' # define reg exp to find necessary contacts
    result = re.findall(pattern, string)
    return render_template("result.html", result=result)

