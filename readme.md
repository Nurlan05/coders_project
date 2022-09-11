

Docker deployment start(real time projects)
####
daphne run olmasi ucun
    daphne -b 0.0.0.0 -p 8000 settings.asgi:application
###
1.Docker,docker-compose.yml,uwsgi.ini files import project

2. pip install uWSGI==2.0.18 to project

3.pip install Daphne (real time projects)

4.real time ucun lazim olan prosesleri edirik,fayl elaveleri ve s
#######
serverde
########

1.ssh root@server_ip
2.sudo apt-get update
3.sudo apt-get install git
4.adduser nurlan
5.sudo usermod -aG sudo nurlan
6.visudo (rootla bir user de add edirik,ctrl+O enter,ctrl x)
7.sudo su - nurlan
8.https://gist.github.com/msadig/
9.wget https://gist.githubusercontent.com/msadig/d63474bd71c93021b1844e8fd7e6c0b4/raw/03d6502802d9fcc374bf4bad99f24db9a770eb06/docker-install.sh
10.bash docker-install.sh
11.sudo su - nurlan
12.layiheni clone edirik ve proyekte icerisine giririk
13.docker network create nginx-proxy
14.docker-compose up --build -d (build etmek ucun)
    docker-compose logs -f (loglara baxmaq ucun)
    docker ps -a (containerlerin veziyyetine baxmaq ucundur)
15.docker exec -it django bash (docker exec -it container_name(postgress,redis,django) bash) containerlere qosulma ucundur
16.source /venv/bin/activate


backupdata____


###serverde postgres dump etmek
    
    pg_dumpall -c -U postgres > dump_data.sql

### file compress(tar.gz) etmek ucun

    tar -cvzf media.tar.gz media/


###localdan servere sql kocurmek ucun(sudo su - postgres (pwd ile yolu yoxlamaq))

    scp /home/nurlan/Documents/Projects_with_team/Team_Backend_projects/database_backup/nayora_last/dump_data.sql   roo@207.180.196.65:/home/nurlan/nayora
	scp /home/nurlan/Documents/Projects_with_team/Team_Backend_projects/database_backup/nayora/nayora_data.sql  chmod -R 777 /var/lib/postgresql

### serverden locala etmek ucun sadece yerlerin deyishmek lazimdi
    
    scp root@167.235.239.49:/var/lib/postgresql/dump_data.sql /home/nurlan/Documents/Projects_with_team/Team_Backend_projects/database_backup/nayora

###serverde postgrese sql yuklemek ucun
    
    cat dump_data.sql | psql -U postgres


###localdan servere file kocurmek ucun(pwd ile yolu yoxlamaq)

    scp /home/nurlan/Documents/Projects_with_team/Team_Backend_projects/database_backup/coders_project/dump_12-07-2022_13_16_34.sql  nurlan@167.235.239.49:/home/nurlan/coders_project

###serverden locala file kocurmek ucun(pwd ile yolu yoxlamaq)

    scp nurlan@167.235.239.49:/home/nurlan/coders_project/media.tar.gz  /home/nurlan/Documents/Projects_with_team/Team_Backend_projects/database_backup/coders

### tar.gz extract etmek ucun

    tar --extract --file media.tar.gz
    
#####################################################################################################################
docker sql backup

# Back up database
docker exec -t your-db-container pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

# Restore database from backup
cat your_dump.sql | docker exec -i your-db-container psql -U postgres 


##language makessages
 ./manage.py makemessages -l en -i venv