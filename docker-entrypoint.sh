#!/bin/bash
set -e

if [ ! -e '/var/www/html/index.php' ]; then
	tar cf - --one-file-system -C /usr/src/tastyigniter . | tar xf -
        chown -R www-data:www-data /var/www/html
	if [ -n "${DB_CONNECTION}" ]; then
		sed -i -e "s/127.0.0.1/$DB_HOSTNAME/g" /var/www/html/config/database.php
                sed -i -e "s/'database' => 'database'/'database' => '$DB_DATABASE'/g" /var/www/html/config/database.php
		sed -i -e "s/'username' => 'username'/'username' => '$DB_USERNAME'/g" /var/www/html/config/database.php
		sed -i -e "s/'password' => 'password'/'password' => '$DB_PASSWORD'/g" /var/www/html/config/database.php
		sleep 60
		php artisan igniter:install -n --env
	        sed -i "/defaultTheme/a \    'urlPolicy' => 'secure'," /var/www/html/config/system.php
	fi


fi

exec "$@"
