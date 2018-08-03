# Image processing using amazon service

**Use Case**<br/>

![Workflow](../images/image_processing_aws.jpg)


1) User can upload an image via flask web application.
2) Images push into amazon s3 bucket.
3) Once image arrives in s3 bucket, lambda invokes.
4) Lambda instance will process these images to call amazon rekonition service to analyze the deatils.
5) Once amazon rekonition identifies and collect metadat about image, information stored into dynamodb.
6) At the same time it creates an thumbnail image and stores to s3 bucket.
7) User can view all the uploaded images metadata and their thumbnails. 

Amazon services used in this application,
1) Elastic Beanstalk - flask application
2) S3
3) Lambda
4) Rekognition
5) Dynamodb
