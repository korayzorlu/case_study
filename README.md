# Analytica House Case Study
## Report
[Prepared Report](https://docs.google.com/spreadsheets/d/1QCjQzRVgPFkR9UeA75eC08r6V4w0696o0bp4HIcRe4A/edit#gid=0)

## Libraries
Some libraries and modules used in the project;

* [Requests](https://github.com/psf/requests)
* [Pandas](https://github.com/pandas-dev/pandas)
* [Operator](https://github.com/python/cpython/blob/3.10/Lib/operator.py)
* [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [GoogleApiClient](https://github.com/googleapis/google-api-python-client/)

## Description
The difficult part for me in this project; some product codes combined with description text. It was not possible to pull that codes. But I believe they can be resolved with a similar approach to the get_close_matches(string from list) feature in difflib. I just didn't go too far.

## What i learned?
In this project, I learned how to use and share the google sheets api along with web scraping. Frankly, it seems easier and more logical than saving excel and csv files on the computer.

## Q&A
If I’d have 10.000 urls that I should visit, then it takes hours to finish. What can we make to fasten this process?
* We can to prepare a multi process script for multiple requests.

What can we make or use to automate this process to run once a day?
* We can easily automate it using the [Schedule](https://github.com/dbader/schedule) library.

Please briefly explain what an API is and how it works.
* API is a structure that allows two applications to communicate with each other and exchange data. Basic working structure of api; an application sends a request to a web server, and that web server sends a response to the request.