## Data Engineering Zoomcamp 2026 Cohort

This repository contains the homework assignments and solutions for the **Data Engineering Zoomcamp 2026** cohort - a comprehensive free course covering modern data engineering fundamentals and best practices.

### 🎯 Course Overview

The Data Engineering Zoomcamp is an intensive, hands-on program that teaches the essential skills needed to become a data engineer. The course covers:

- **Containerization** with Docker and orchestration with Docker Compose
- **Workflow Orchestration** using tools like Prefect and Mage
- **Data Warehousing** with SQL and cloud-based solutions
- **Analytics Engineering** with dbt and transformation best practices
- **Batch Processing** for large-scale data pipelines
- **Streaming** real-time data processing with Kafka and similar technologies

### 📚 Module 1: Docker & Terraform

This repository contains the complete solution for **Module 1**, which focuses on foundational data engineering infrastructure skills:

#### 🐳 Docker Fundamentals
- Understanding Docker images and containers
- Working with Docker Compose for multi-container applications
- Setting up PostgreSQL databases in containerized environments
- Building data ingestion pipelines with Python

#### 🗄️ SQL & Data Processing
- Writing complex SQL queries for data analysis
- Processing NYC taxi trip data (Parquet and CSV formats)
- Performing aggregations, joins, and window functions
- Data type handling and optimization

#### ☁️ Infrastructure as Code
- Introduction to Terraform for cloud resource management
- Creating and managing Google Cloud Platform (GCP) resources
- Setting up storage buckets and BigQuery datasets
- Understanding the Terraform workflow (init, plan, apply, destroy)

### 🚀 Assignment Details

**Module 1 Homework** includes:

1. **Docker Image Analysis** - Understanding container internals and package management
2. **Container Networking** - Configuring service communication in Docker Compose
3. **Data Ingestion Pipeline** - Building ETL processes for NYC taxi data
4. **SQL Analytics** - Answering business questions through data analysis
5. **Cloud Infrastructure** - Provisioning data infrastructure with Terraform

The assignment demonstrates practical skills in:
- Container-based application deployment
- Database administration and querying
- Data pipeline development
- Cloud infrastructure automation

### 💡 Learning Outcomes

After completing Module 1, students gain hands-on experience with:

- **Modern Development Practices**: Using containers for reproducible environments
- **Database Management**: Setting up and querying PostgreSQL databases
- **Data Engineering Fundamentals**: Building scalable data ingestion pipelines
- **Cloud Infrastructure**: Managing cloud resources programmatically
- **Problem-Solving**: Translating business requirements into technical solutions

### 🛠️ Technical Stack

- **Docker & Docker Compose**: Containerization and orchestration
- **PostgreSQL**: Relational database for structured data
- **Python**: Data processing with pandas and SQLAlchemy
- **SQL**: Data analysis and manipulation
- **Terraform**: Infrastructure as Code
- **Kestra**: Workflow orchestration and automation
- **Google Cloud Platform**: Cloud infrastructure provider

### 📚 Module 2: Workflow Orchestration

Module 2 focuses on **Kestra**, a modern workflow orchestration platform for building data pipelines:

#### 🔄 Workflow Orchestration Fundamentals
- Understanding workflow orchestration and its importance in data engineering
- Learning Kestra's architecture and core concepts (flows, tasks, triggers)
- Creating and managing data pipelines with declarative YAML configurations
- Working with variables and templates for dynamic pipeline execution

#### 🗂️ Data Processing at Scale
- Ingesting and processing NYC taxi data (yellow and green) across multiple years
- Implementing backfill functionality for historical data
- Handling large datasets with efficient processing strategies
- Working with both scheduled and manual execution modes

#### 🐳 Container Integration
- Running workflows in containerized environments
- Integrating Docker with Kestra for task execution
- Managing dependencies and runtime environments
- Building reproducible data pipelines

#### ☁️ Cloud Integration
- Working with Google Cloud Platform (GCP) and BigQuery
- Setting up data storage in cloud buckets
- Loading processed data into data warehouses
- Understanding cloud-native data engineering patterns

#### 🎯 Assignment Details

**Module 2 Homework** includes:

1. **Flow Extension** - Extending existing workflows to process 2021 data
2. **Backfill Implementation** - Leveraging Kestra's backfill functionality for historical data
3. **Manual vs Scheduled Execution** - Understanding different execution modes
4. **Data Validation** - Verifying data integrity and row counts across datasets
5. **Configuration Mastery** - Working with triggers, timezones, and variables

The assignment demonstrates practical skills in:
- Workflow orchestration with Kestra
- Large-scale data pipeline management
- Cloud-native data engineering
- Automation and scheduling best practices

### 📊 Dataset

The assignments work with real-world **NYC Taxi and Limousine Commission** data:
- **Module 1**: Green taxi trip records for November 2025
- **Module 2**: Yellow and green taxi trip records for 2020-2021
- Taxi zone lookup data for location analysis
- Parquet and CSV file formats representing common data engineering scenarios

### 🎓 About Data Engineering Zoomcamp

This free course is offered by [DataTalksClub](https://github.com/DataTalksClub) and provides:
- Comprehensive curriculum covering the full data engineering lifecycle
- Hands-on assignments with real datasets
- Community support and collaborative learning
- Preparation for entry-level data engineering roles

**Course Repository**: https://github.com/DataTalksClub/data-engineering-zoomcamp/

### 🚀 Getting Started

To explore the Module 1 solution:
1. Navigate to the `01-docker-terraform/` directory
2. Review the homework questions and answers in `homework.md`
3. Examine the Docker setup and Python ingestion scripts
4. Try running the SQL queries to understand the data analysis

To explore the Module 2 solution:
1. Navigate to the `02-workflow-orchestration/` directory
2. Review the homework questions and answers in `homework.md`
3. Examine the Kestra flow definitions and configurations
4. Study the workflow patterns for data ingestion and backfill

This repository demonstrates practical implementation of data engineering concepts and serves as a learning resource for aspiring data engineers.
