# Twinning

## Introduction

Scrapy project to obtain England's town twinnings listed on wikipedia.

## Installation

Python 3.10.6

```
$ python -m venv ./env
$ source ./env/bin/activate
$ pip install -r requirements.txt
```

## Usage

```
$ scrapy crawl twinning -o twinning.csv
```

## Notes

Spider is based on page revision: https://en.wikipedia.org/w/index.php?title=List_of_twin_towns_and_sister_cities_in_England&oldid=1113990879

robots.txt forbids direct access.
