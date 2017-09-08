#!/usr/bin/env python3

from flask import Flask, render_template

from newsdb import get_articles, get_populr_authors, request_errors

from collections import OrderedDict

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    # fetching the values from the sql queries and sending to html
    ar1dict = OrderedDict()
    au1dict = OrderedDict()
    req1dict = OrderedDict()
    for title, gets in get_articles():
        ar1dict[title] = gets
    for name, total in get_populr_authors():
        au1dict[name] = total
    for date, percentage in request_errors():
        req1dict[date] = percentage
    return render_template('report.html', ardict=ar1dict,
                           audict=au1dict, reqdict=req1dict)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=8000)
