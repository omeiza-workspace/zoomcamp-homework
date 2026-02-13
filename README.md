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
- **BigQuery**: Cloud data warehouse for analytics
- **dbt (data build tool)**: Analytics engineering and data transformations

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

### 📚 Module 3: Data Warehouse

Module 3 covers modern **Data Warehousing** concepts using Google BigQuery:

#### 🏢 Data Warehouse Fundamentals
- Understanding OLTP vs OLAP systems and their use cases
- Exploring BigQuery architecture and serverless data warehouse capabilities
- Working with BigQuery's columnar storage and distributed processing
- Understanding data warehouse design patterns and best practices

#### 🗂️ Partitioning and Clustering
- Implementing table partitioning for cost-effective querying (time-unit, integer range, ingestion time)
- Configuring clustering to optimize data access patterns and improve query performance
- Understanding the trade-offs between partitioning and clustering strategies
- Best practices for optimizing BigQuery costs through intelligent data organization

#### 📊 SQL for Analytics
- Writing analytical SQL queries for business intelligence
- Working with window functions for time-series analysis and running totals
- Understanding data types and schema design for analytical workloads
- Leveraging BigQuery's advanced SQL capabilities (ML functions, GIS, etc.)

#### ☁️ BigQuery Architecture
- Creating external tables from GCS parquet files
- Understanding materialized vs external tables
- Exploring BigQuery's columnar storage format and query optimization
- Cost estimation and query performance analysis

#### 🎯 Assignment Details

**Module 3 Homework** includes:

1. **BigQuery Architecture** - Understanding the internal workings of BigQuery's distributed system
2. **Partitioning Strategies** - Implementing and optimizing table partitioning for the NYC taxi dataset
3. **Cost Optimization** - Writing efficient queries that minimize data processing costs
4. **Advanced SQL Analytics** - Answering complex business questions using window functions and aggregations
5. **Performance Tuning** - Optimizing query performance through proper data organization

The assignment demonstrates practical skills in:
- Cloud data warehouse architecture and design
- BigQuery optimization techniques
- Cost-efficient data querying strategies
- Advanced analytical SQL patterns

### 📚 Module 4: Analytics Engineering

Module 4 introduces **Analytics Engineering** using dbt (data build tool) for transforming data in the warehouse:

#### 🔄 dbt Fundamentals
- Understanding the analytics engineering workflow and the T in ELT
- Setting up and configuring dbt projects with BigQuery integration
- Working with dbt's version control and collaborative development features
- Understanding the dbt DAG (Directed Acyclic Graph) for data lineage

#### 🏗️ Data Modeling
- Building staging models for raw data ingestion and initial transformations
- Creating core/marts models for business logic and analytics-ready tables
- Designing dimensional models with fact and dimension tables
- Implementing star schema design patterns for the NYC taxi data

#### ✅ Testing and Documentation
- Writing data tests to ensure data quality and integrity
- Creating custom tests for business-specific validation rules
- Generating and maintaining data documentation with dbt docs
- Understanding testing strategies for data warehouses

#### 🧮 Advanced SQL Analytics
- Computing quarterly revenue growth and Year-over-Year (YoY) comparisons
- Working with continuous percentiles for fare analysis
- Building complex analytical models with window functions
- Handling time-series data and travel time calculations

#### 📦 dbt Project Structure
The `taxi_rides_ny` dbt project includes:
- **Staging Models**: `stg_green_tripdata.sql`, `stg_yellow_tripdata.sql` - Clean and prepare raw data
- **Core Models**:
  - `fact_trips.sql` - Central fact table combining green and yellow taxi trips
  - `dim_zones.sql` - Dimension table for taxi zones and boroughs
  - `dim_monthly_zone_revenue.sql` - Aggregated revenue metrics by zone and month
- **Seeds**: `taxi_zone_lookup.csv` - Static reference data for location mapping
- **Macros**: Custom SQL functions for reusable transformations like `get_payment_type_description`

#### 🎯 Assignment Details

**Module 4 Homework** includes:

1. **dbt Project Setup** - Configuring dbt with BigQuery and understanding project structure
2. **Model Development** - Building staging and core models following best practices
3. **Data Transformations** - Implementing business logic for trip metrics and revenue calculations
4. **Testing Implementation** - Adding tests for data quality and schema validation
5. **Documentation** - Creating comprehensive documentation for models and their relationships
6. **Advanced Analytics** - Building quarterly revenue analysis and percentile calculations

The assignment demonstrates practical skills in:
- Analytics engineering workflow with dbt
- Data modeling for analytics and BI
- Data quality testing and validation
- Collaborative data transformation practices
- Advanced SQL for business analytics

### 📊 Dataset

The assignments work with real-world **NYC Taxi and Limousine Commission** data:
- **Module 1**: Green taxi trip records for November 2025
- **Module 2**: Yellow and green taxi trip records for 2020-2021
- **Module 3**: Yellow taxi data (January-June 2024) loaded into BigQuery for partitioning and clustering analysis
- **Module 4**: Green, yellow, and FHV taxi data (2019-2020) for dbt transformations and analytics
- Taxi zone lookup data for location analysis
- Parquet, CSV, and BigQuery table formats representing common data engineering scenarios

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

To explore the Module 3 solution:
1. Navigate to the `03-data-warehouse/` directory
2. Review the homework questions and answers in `homework.md`
3. Examine the SQL queries and BigQuery optimization techniques
4. Study the partitioning and clustering strategies for cost efficiency

To explore the Module 4 solution:
1. Navigate to the `04-analytics-engineering/taxi_rides_ny/` directory
2. Review the homework questions and answers in `homework.md`
3. Examine the dbt project structure, models, and configurations
4. Review the staging models in `models/staging/` and core models in `models/core/`
5. Study the tests, macros, and documentation setup in the dbt project

This repository demonstrates practical implementation of data engineering concepts and serves as a learning resource for aspiring data engineers.
