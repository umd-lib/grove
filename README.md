# grove

Grove RDF Ontology and Vocabulary Editor is a [Django]-based web
application for creating, editing, and publishing controlled vocabularies
in RDF.

## Additional Documentation

Additional documentation for this application is in the "docs/" subdirectory,
including:

* [Load Predicates](docs/load_predicate.md)
* [Vocabulary Model Timestamps](docs/VocabularyModelTimestamps.md)

## Test Plan

A basic test plan for verifying application functionality is provided in
[docs/TestPlan.md](docs/TestPlan.md).

## Development Environment Setup

* [VS Code Dev Container Setup](docs/DevelopmentEnvironmentVsCode.md)
* [Local Development Environment Setup](docs/DevelopmentEnvironmentLocal.md)

## Building the Docker Image for local testing

To build and run locally

```zsh
# Build
docker build -t docker.lib.umd.edu/grove:latest .

# Run
docker run -it \
-e DATABASE_URL=sqlite:///db.sqlite3 \
-e DEBUG=True \
-e SECRET_KEY=$(uuidgen | shasum -a 256 | cut -c-64) \
-e SERVER_PORT=5000 \
-p 5000:5000 \
docker.lib.umd.edu/grove:latest
```

## Building the Docker Image for K8s Deployment

The following procedure uses the Docker "buildx" functionality and the
Kubernetes "build" namespace to build the Docker image. This procedure should
work on both "arm64" and "amd64" MacBooks.

The image will be automatically pushed to the Nexus.

### Local Machine Setup

See <https://github.com/umd-lib/k8s/blob/main/docs/DockerBuilds.md> in
GitHub for information about setting up a MacBook to use the Kubernetes
"build" namespace.

### Creating the Docker image

1. Switch to the Kubernetes "build" namespace:

    ```bash
    kubectl config use-context build
    ```

2. Create the "docker.lib.umd.edu/grove" Docker image,
   using the git tag uploaded to Github:

    ```bash
    TAG=<GIT_TAG> && \
    docker buildx build \
        --build-arg BUILDKIT_CONTEXT_KEEP_GIT_DIR=1 --no-cache --platform linux/amd64 --push --builder=kube \
        -t docker.lib.umd.edu/grove:$TAG https://github.com/umd-lib/grove.git#$TAG
    ```

   The Docker image will be automatically pushed to the Nexus.

[Django]: https://www.djangoproject.com/
