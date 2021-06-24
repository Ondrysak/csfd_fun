# csfd_fun
top300 movies

# Quickstart

## Start the stack 

This starts PostgreSQL database and a Django app

```
docker-compose up
```

## Apply migrations

This can be done using a one off container 

```
docker-compose run web python3 csfd/manage.py migrate
```


## Download data

This command accepts one `int` parameter, which specifies delay between scraping each movie in seconds. To wait one second we specify `1` below.


```
docker-compose run web python3 csfd/manage.py scrape 1
```


## Load data from fixture

```
docker-compose run web python3 csfd/manage.py loaddata csfd/fixture.json
```