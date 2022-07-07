# DevGrid

To run the project you just need to:
    1 - clone the repository
    2 - run "docker compose build"
    3 - run "docker compose run -d"

To test:
    1 - run "docker compose exec -it weather-api sh"
    2 - run inside the container "cd app/tests/"
    3 - run inside the container "pytest"
