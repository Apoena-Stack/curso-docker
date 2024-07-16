

docker-compose up -d
docker cp -L job.py spark-local_spark-master_1:/opt/bitnami/spark/job.py
docker logs spark-local_spark-master_1
docker exec spark-local_spark-master_1 spark-submit --master spark://8dcc4582c434:7077 test_job.py
