#git init
#git pull https://github.com/negintavakkoli/Maglet
#####SOLR#####

##install SOLR
#sudo wget https://archive.apache.org/dist/lucene/solr/8.5.2/solr-8.5.2.tgz
#tar xzf solr-8.5.2.tgz solr-8.5.2/bin/install_solr_service.sh --strip-components=2
#sudo bash ./install_solr_service.sh solr-8.5.2.tgz
# sudo systemctl status solr

###Create collection
#cd path/to/solr/directory
# bin/solr create -c maglet --> create new collection of solr
#java -classpath C:\solr-7.3.1\dist\solr-core-7.3.1.jar  -Dauto=yes -Dc=2juil -Ddata=files -Drecursive=no org.apache.solr.util.SimplePostTool /home/negin/ls
# bin/post -c Maglet Maglet/Maglet_1.0.0/Journals\ to\ Crawl/Journals_XML/XML_Solr/* --> insert data to solr





