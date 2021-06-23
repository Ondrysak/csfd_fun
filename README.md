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


```
docker-compose run web python3 csfd/manage.py scrape 1
```