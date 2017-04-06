#coding:utf-8

from minio import Minio
from minio.error import ResponseError

minioClient = Minio('localhost:9001',
                  access_key='LD8CVUS73FZ5G8IYSQHL',
                  secret_key='G1bFWJBu4PKgFI+4iaA43LjhrhHGngfqHQu8iXgLL',
                  secure=True)

# Make a bucket with the make_bucket API call.
# try:
#        minioClient.make_bucket("maylogs")
# except ResponseError as err:
#        print(err)
# else:
#         # Put an object 'pumaserver_debug.log' with contents from 'pumaserver_debug.log'.
#         try:
#                minioClient.fput_object('maylogs', 'pumaserver_debug.log', '/tmp/pumaserver_debug.log')
#         except ResponseError as error:
#                print(error)

print(minioClient)
buckets = minioClient.list_buckets()
print(buckets)
# for bucket in buckets:
#     print(bucket.name, bucket.creation_date)
