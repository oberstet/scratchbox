# Prune everything

```
docker system prune --volumes --force
```

See [here](https://docs.docker.com/config/pruning/).

# Remove all images

```
docker rmi --force $(docker images -a -q)
```

https://www.digitalocean.com/community/tutorials/how-to-remove-docker-images-containers-and-volumes
