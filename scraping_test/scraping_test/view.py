from flask import Flask
from flask import Flask, render_template, request
import subprocess
import sys
import scraper_with_scrapy

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template("layout.html", title = "Scraping App")

@app.route('/run_scraper_with_scrapy', methods=['GET', 'POST'])
def run_scraper():
    if request.method == 'POST':
        try:
            book_data = scraper_with_scrapy.run()
            return render_template("result.html", title="Scraping Result", books=book_data)
        except Exception as e:
            return str(e), 500
    return render_template("layout.html", title="Scraping App")



if __name__ =="__main__":
    app.run(debug=True,)