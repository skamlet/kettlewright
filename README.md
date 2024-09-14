# Kettlewright Setup

1. Create a directory for environment variables and the SQLite database:

       mkdir -p ~/docker/kettlewright/instance

2. Create a file in ~/docker/kettlewright/ called `.env` and populate it with the following:

       BASE_URL=http://127.0.0.1
       SECRET_KEY=[unique string]
       SQLALCHEMY_DATABASE_URI=sqlite:///db.sqlite
       MAIL_SERVER=[enter mail server details]
       MAIL_PORT=[Probably 587]
       MAIL_USE_TLS=[Probably 1]
       MAIL_USERNAME=[enter email address]
       MAIL_PASSWORD=[enter email password]
       REQUIRE_SIGNUP_CODE=[True_or_False]
       SIGNUP_CODE=[only needed if previous statement is True]

3. Pull the Docker image:

       docker pull yochaigal/kettlewright

4. Create the database:
       docker run -it --env-file .env -e UID=$(id -u) -e GID=$(id -g) -v $(pwd)/instance:/app/instance yochaigal/kettlewright /bin/sh -c "flask db upgrade"
   
5. Start Kettlewright

       docker run -d --env-file ~/docker/kettlewright/.env -e UID=$(id -u) -e GID=$(id -g) -v $(pwd)/instance:/app/instance -p 8000:8000 --restart always yochaigal/kettlewright

6. Open [http://127.0.0.1:8000](http://127.0.0.1:8000) to access Kettlewright.

## After Kettlewright Has Been Installed

To manage the Kettlewright image, first find the container id (typically the most recent container):

       docker ps -a

Then start or stop the container with:

       docker start/stop [container]

To see the logs, run:

       docker logs -f [container]

To remove old containers:

       docker rm [container]

## Updating Kettlewright

1. First, stop the container:

       docker stop [container]

2. Then remove it:

       docker rm [container]

3. Pull the latest image:

       docker pull yochaigal/kettlewright

4. Update the database:
       
       docker run -it --env-file .env -e UID=$(id -u) -e GID=$(id -g) -v $(pwd)/instance:/app/instance yochaigal/kettlewright /bin/sh -c "flask db upgrade"

5. Start a new container using the latest image:

       docker run -d --env-file ~/docker/kettlewright/.env -e UID=$(id -u) -e GID=$(id -g) -v $(pwd)/instance:/app/instance -p 8000:8000 --restart always yochaigal/kettlewright

## Automated Updates

1. To update the Docker image automatically, install Watchtower:

       git pull containerrr/watchtower

2. Then, run the following command:

       docker run -d --name watchtower --restart always -v /var/run/docker.sock:/var/run/docker.sock -e TZ=America/New_York containrrr/watchtower --cleanup --schedule "*/5 * * * *"
       
This command will run Watchtower every 5 minutes and automatically at boot. It will update all available Docker images unless explicitly stated, as well as clean up old images.

## Running the app without Docker

1. Clone the repository.

2. Copy `.env.template` to `.env` and insert the appropriate values.

3. Create the python environment:

       pipenv shell

4. Install packages:

       pipenv sync

5. Initialize database:

       flask db upgrade
       exit

6. Run the app:

       pipenv run dotenv run -- gunicorn -k eventlet -w 2 -b 0.0.0.0:8000 'app:application'
