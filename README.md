### Managing R dependencies

The [renv](https://github.com/rstudio/renv) package is used to manage the R dependencies of this project. 

To add a new R package to this project, launch a local R session and run the following:
```r
renv::install("<pkg-name>")
renv::snapshot
```

This will download the package to the local cache, but more importantly, it will also update the `renv.lock` file after 
`renv::snapshot()` is called. Once the Docker image is rebuilt, the new container will now install any new dependencies within `renv.lock`.

**Note:** the version of the local R installation must match the version pinned within the Dockerfile (R-4.2.1) for the updated `renv.lock` file to be installed correctly when the new image is built. 

### Docker

```
docker build -t app .
docker run -p 8000:8000 app
```