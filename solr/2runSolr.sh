sudo nohup java -server -Djava.headless=True -DSTOP.PORT=8079 -DSTOP.KEY=stopkey -jar start.jar > /var/local/mdid-storage/mdid-scratch/logs/solr.log  &
