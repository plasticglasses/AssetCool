# Task Instructions

## Task 1

Design a cloud-based system block architecture
(using available services, packages and components from AWS or GCP, plus any custom code you may require)
for access to an SQL (or similar) database
through an externally-facing gRPC API.
Provide a block diagram of how these services and components connect together.
You do not have to go into detail of the individual RPCs or specify the external API.

## Acceptance Criteria

• Prepare a ~30 mins presentation detailing your solution for discussion at the
interview.
• Please submit all code in a zipped folder the evening before the interview.

## Options

- Use Databricks API and Spark Connect to provide gRPC output required.
- Use Spark db and gRPC
    - https://grpc.io/docs/languages/python/quickstart/
    API Gateway (gRPC)	Cloud Endpoints + ESPv2
    ECS/Fargate	Cloud Run / GKE / Compute Engine
    Amazon RDS	Cloud SQL
    VPC/Security Groups	VPC firewall rules


# Things to consider
- Network security -- having a layer that everyone must go through before they can access anything
- Access Control - AD groups / IAM controls
- Language the gRPC is built in? GO?

I'm not sure what this means????

- should we include user management IAM/AD groups?
- how much code is expected?
- how many requests will be occuring - should I consider load balancing options 

if there's lots of requests then load balancing will need to be considered.


AWS ECS to host gRPC


![alt text](image.png)


# Useful Links
https://dev.to/aws-builders/getting-started-with-grpc-net-6-and-amazon-ec2-498b

# EKS Cluster
https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer.html


ECS (Elastic Container Service) is AWS's proprietary, simpler container orchestration service, ideal for tight AWS integration and less complex workloads. EKS (Elastic Kubernetes Service) is AWS's fully managed Kubernetes service, offering more power, flexibility, and a vast open-source ecosystem, but with increased complexity and costs


# Why AWS over Google cloud??


# For hosting my gRPC api
# ECS vs Lambda

# Deploy a gRPC-based application on an amazon EKS cluster and access it within an application 
https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer.html




# Externally accessible eks api endpoint 
 First you can change the network setting and make it only available within the VPC.

If you leave it public/private then the API is exposed in the internet but there’s 2 layer of authentication. First you need a valid IAM user with keys then either allow that user access via IAM role or groups a added in the EKS auth config file. There’s also OIDC setup.

Personally I’m running a development cluster so I just add Devs user acct access on auth config with access group.

https://www.reddit.com/r/kubernetes/comments/zq5wko/aws_eks_api_endpoint_publicly_accessible_but_not/


# how to make a gRPC api
- Java with Spring Boot Framework
- Go
- ASP.NET microservice
- 



# Google cloud equivalent
- Amazon Elastic Kubernetes Service (EKS) Google Cloud offers the Google Kubernetes Engine (GKE)




# architecture diagram for ecs to database via grpc
# https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-grpc-based-application-on-an-amazon-eks-cluster-and-access-it-with-an-application-load-balancer.html 
# does databricks api use grpc
# how to link a grpc server pod inside aws eks with a database
databricks on aws ec2 instance
https://dev.to/aws-builders/getting-started-with-grpc-net-6-and-amazon-ec2-498b
https://aws.amazon.com/blogs/modernizing-with-aws/deploy-sql-server-container-clusters-using-amazon-eks-and-amazon-fsx-for-windows/
https://docs.aws.amazon.com/eks/latest/userguide/cluster-endpoint.html
https://docs.aws.amazon.com/eks/latest/userguide/eks-architecture.html
https://www.google.com/search?client=firefox-b-d&sca_esv=a95b1a567a7f3cbf&udm=2&fbs=AIIjpHxU7SXXniUZfeShr2fp4giZ1Y6MJ25_tmWITc7uy4KIeoJTKjrFjVxydQWqI2NcOha3O1YqG67F0QIhAOFN_ob1yXos5K_Qo9Tq-0cVPzex8akBC0YDCZ6Kdb3tXvKc6RFFaJZ5G23Reu3aSyxvn2qD41n-47oj-b-f0NcRPP5lz0IcnVzj2DIj_DMpoDz5XbfZAMcEl5-58jjbkgCC_7e4L5AEDQ&q=architecture+diagram+of+a+database+inside+an+eks+instance&sa=X&ved=2ahUKEwjdtIHl55KQAxVuXEEAHbH9IFsQtKgLegQIHhAB&biw=3440&bih=1307&dpr=1#vhid=CUNGMxBSBmBYQM&vssid=mosaic
https://www.reddit.com/r/kubernetes/comments/zq5wko/aws_eks_api_endpoint_publicly_accessible_but_not/
how to make a gRPC api
eks equivalent in gcp
https://groups.google.com/g/grpc-io/c/DoX0qUZrH4s
https://cloud.google.com/apis/docs/overview#supporting_http_and_grpc
https://cloud.google.com/apis/design
https://daily.dev/blog/api-gateway-for-grpc-microservices





