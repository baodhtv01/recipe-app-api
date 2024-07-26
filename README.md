# Recipe API Project

## Build project

**Step 1:**
```
docker build .
```

**Step 2:**
```
docker-compose build
```

**Step 3:**
```
docker-compose run --rm app sh -c "flake8"
```

**Step 4:**
```
docker-compose run --rm app sh -c "django-admin startproject app ."
```


**Step 4:**
```
docker-compose up -d
```