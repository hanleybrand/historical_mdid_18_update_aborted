cd /var/local/mdid/rooibos/solr
sudo nohup java -server -Djava.headless=True -DSTOP.PORT=8079 -DSTOP.KEY=stopkey -jar /var/local/mdid/rooibos/solr/start.jar > /var/local/mdid-storage/mdid-scratch/logs/solr.log  &
cd -
