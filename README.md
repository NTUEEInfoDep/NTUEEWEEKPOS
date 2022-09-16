# TastyIgniter Docker

clone the repo

    git clone https://github.com/NTUEEInfoDep/NTUEEWEEKPOS.git

Required to prepare .env file for installation!

Run with docker compose for automatic database configuration

    cd NTUEEWEEKPOS
    docker-compose up -d

# Modify Components configuration

go to the directory

    cd /home/ntuee/production/NTUEEWEEKPOS

go into container

    docker exec -it ntueeweekpos_weekpos_1  bash

in container

    php artisan igniter:install --no-interaction
    php artisan igniter:passwd admin

## Credits

TastyIgniter(docker): https://github.com/ThisIsQasim/TastyIgniter

TastyIgniter: https://github.com/tastyigniter/TastyIgniter
