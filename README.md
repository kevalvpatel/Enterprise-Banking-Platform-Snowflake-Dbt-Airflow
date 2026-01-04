# Enterprise Big Data Platform 🏦
### Domain: Banking

[![Snowflake](https://img.shields.io/badge/Warehouse-Snowflake-29B5E8?logo=snowflake)](https://www.snowflake.com/)
[![dbt](https://img.shields.io/badge/Modeling-dbt-FF694B?logo=dbt)](https://www.getdbt.com/)
[![Apache-Airflow](https://img.shields.io/badge/Orchestration-Airflow-017CEE?logo=apache-airflow)](https://airflow.apache.org/)
[![Apache-Spark](https://img.shields.io/badge/Processing-Spark-E25A1C?logo=apachespark)](https://spark.apache.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=ffd343)](requirements.txt)
[![AWS-S3](https://img.shields.io/badge/Storage-S3-569A31?logo=amazons3)](https://aws.amazon.com/s3/)
[![AWS-EKS](https://img.shields.io/badge/Compute-EKS-FF9900?logo=amazoneks)](https://aws.amazon.com/eks/)
[![Terraform](https://img.shields.io/badge/Infrastructure-Terraform-623CE4?logo=terraform)](https://www.terraform.io/)
[![Kubernetes](https://img.shields.io/badge/Compute-Kubernetes-326CE5?logo=kubernetes)](https://kubernetes.io/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)](https://www.docker.com/)


<!-- ---------------  Scope  --------------- -->
## Project Overview
A fully-encrypted, audit-ready analytics platform that ingests **millions of banking events per hour**, lands them in S3 (Bronze), cleans & conforms in Snowflake (Silver), and exposes business-ready Data-Vault marts (Gold) to downstream BI, AML, and regulatory teams. This project demonstrates a scalable, enterprise-grade banking data platform using modern Data Engineering and DevOps best practices. It ingests, processes, models, and serves banking data at scale using **AWS, Snowflake, Spark, Airflow, dbt, Docker, Terraform, and Kubernetes (K8s).**


<!-- ---------------  ARCHITECTURE DIAGRAM  --------------- -->
## Architecture
![Architecture](img/Architecture.png)


## Key Features

- **Cloud-Native**: AWS S3, Snowflake, K8s-managed Spark and Airflow.
- **Orchestrated Pipelines**: Airflow DAGs for batch and streaming ingestion.
- **Modular dbt Models**: Hub, Link, Satellite layers for clean data modeling.
- **Big Data Processing**: Spark handles large transaction and payment datasets efficiently.
- **Security & Governance**: Snowflake role-based access, audit logs, encrypted data at rest.
- **Infrastructure as Code (IaC)**: Terraform scripts for reproducible environments.
- **Containerized Deployment**: Docker + K8s for scalable, portable workloads.
