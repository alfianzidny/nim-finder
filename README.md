# NIM Finder

NIM Finder for ITB. Using python for crawling NIM and name each student.
http://ddery.com/nim-finder/

## How to scrape
1. Open terminal
```sh
cd spider
scrapy runspider nim_spider.py -o ../data/nim_nama_draft.json
```
2. Don't forget to use VPN if you're not under ITB network

## How to insert json to mysql localhost
1. Edit database connect configuration on converter/json_to_mysql.py
2. Open terminal
```sh
$ cd converter
$ python json_to_mysql.py
```

## How to export mysql to json
1. Open terminal
```sh
$ cd converter
$ python mysql_to_json.py >> ../data/nim_nama_final.json
```

## Structure
```sh
converter
-- json_to_mysql.py
-- mysql_to_json.py
css
-- style.css
data
-- nim_nama_final.py
-- nim_nama_draft.py
spider
-- nim_spider.py
index.html
```