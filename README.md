# DEChallenge

1. crear imagen container:
```
$ docker build -t prediction:v1 .

```
2. run container

```
$ docker run -dit --rm -p 5000:5000 --name prediction prediction:v1

```

3. url API


```
http://localhost:5000/prediction

```
