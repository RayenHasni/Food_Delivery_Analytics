# Food Delivery Analytics Project 📦🚗

An end-to-end data analytics platform that collect food delivery data, orchestrates ingestion into Google BigQuery, transforms it using dbt, and enables business intelligence through dashboards.

## 🎯 Project Overview

This project demonstrates modern data stack best practices by building a scalable ELT pipeline :

![Preview](https://github.com/RayenHasni/Food_Delivery_Analytics/blob/main/docs/Architecture.gif)

```
Data Collection
    ↓
Apache Airflow (Pipeline Orchestration)
    ↓
BigQuery Ingestion (Raw Layer)
    ↓
dbt Transformation (Staging → Mart)
    ↓
Business Intelligence Dashboards
```

### ✨ Key Features

- **Data Collection**: 30K+ customers, 14K+ restaurants, 760K+ orders
- **Automated Orchestration**: Apache Airflow DAGs running every 5 minutes with failure handling
- **Cloud Data Warehouse**: Google BigQuery for scalable, cost-effective analytics
- **Complete ELT Pipeline**: dbt transformations with staging and analytics layers
- **Data Quality**: Built-in tests and documentation for data integrity
- **BI-Ready**: Dimensional and fact tables optimized for dashboards and analytics

## 📊 System Architecture

### Data Layers

```
Raw Layer (BigQuery: food_delivery_raw)
├── customers
├── restaurants
├── orders
└── deliveries

Staging Layer (dbt: food_delivery_staging)
├── stg_customers (cleaned, deduplicated)
├── stg_restaurants (validated)
├── stg_orders (enriched with timestamps)
└── stg_deliveries (standardized metrics)

Analytics Layer (dbt: food_delivery_analytics)
├── Fact Tables
│   └── fct_orders (grain: one row per order)
└── Dimension Tables
    ├── dim_customers (customer attributes)
    ├── dim_restaurants (restaurant profiles)
    └── dim_dates (time dimension)
```

### Pipeline Flow

1. **Ingestion** (Airflow + BigQuery): Runs every 5 minutes
   - Task 1: Generate and upload data to BigQuery raw layer
   - Task 2: Run dbt transformations (staging → analytics)
   - Automatic failure recovery and retry logic

2. **Transformation** (dbt): SQL-based transformations with tests
   - Staging models: data cleaning, standardization, deduplication
   - Mart models: business logic, KPIs, dimensional hierarchies
   - Data quality tests on primary keys, uniqueness, and referential integrity

3. **Analytics** (BI Tools): Clean, analytics-ready data for dashboards

## 🚀 Quick Start

### Prerequisites

- Python 3.12+
- Google Cloud Platform account with BigQuery enabled
- Service account JSON credentials for BigQuery access
- Power Bi (or any data visualisation tool)

### Setup Instructions

1. **Clone and navigate to project**
   ```bash
   git clone <your-repo-url>
   cd FoodDeliveryAnalytics
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up GCP credentials**
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account-key.json
   ```

5. **Configure Airflow**
   ```bash
   export AIRFLOW_HOME=./airflow
   airflow standalone  # Starts webserver on localhost:8080
   ```

## 🔧 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Data Collection** | Python | Upload data to Bigquery |
| **Orchestration** | Apache Airflow 2.9.3 | DAG scheduling, monitoring, error handling |
| **Cloud Data Warehouse** | Google BigQuery | Scalable data storage and SQL querying |
| **Data Transformation** | dbt (dbt-bigquery) | SQL-based ELT with testing and documentation |
| **Analytics** | Power BI | Data visualization and dashboards |

## 📈 Key Metrics & Analytics

The platform enables analysis of:

- **Customer Metrics**: Lifetime value, acquisition cost, Inactive customers rate
- **Order Analytics**: Average order value, completion rate, revenue trends
- **Delivery Performance**: Average delivery time, distance coverage, ratings
- **Restaurant Health**: Order volume, demand trends, cuisine popularity
- **Demand Patterns**: Peak hours analysis, zone-based demand, seasonality

## 📝 Data Models Reference

### Staging Models (`dbt/models/staging/`)
- `stg_customers.sql`: Cleaned customer data with demographics
- `stg_restaurants.sql`: Validated restaurant attributes
- `stg_orders.sql`: Orders with temporal features
- `stg_deliveries.sql`: Delivery metrics and performance data

### Analytics Models (`dbt/models/mart/`)
- `fct_orders.sql`: Fact table 
- `dim_customers.sql`: Customer dimension 
- `dim_restaurants.sql`: Restaurant dimension 
- `dim_dates.sql`: Date dimension for time series analysis

## 🔄 Pipeline Scheduling

The main DAG `food_delivery_pipeline` runs **every 5 minutes** with:
- Task 1: `generate_and_upload_data` - Creates synthetic data and uploads to BigQuery
- Task 2: `run_dbt_build` - Transforms raw data through staging to analytics layer
- Dependencies: Sequential execution (Task 1 → Task 2)


## 📚 Learning Resources

This project demonstrates key concepts from:

- [Apache Airflow Documentation](https://airflow.apache.org/) - Workflow orchestration
- [dbt Documentation](https://docs.getdbt.com/) - Data transformations and testing
- [BigQuery Documentation](https://cloud.google.com/bigquery/docs) - Data warehouse best practices
- [dbt BigQuery Adapter](https://docs.getdbt.com/reference/warehouse-setups/bigquery-setup) - Configuration

## 📊 BI & Analytics [(Link)](https://app.powerbi.com/view?r=eyJrIjoiN2Y2ZGFmZjYtODcxOS00YTFmLWFhMzgtMjUxMWI5YzU0ZWIyIiwidCI6ImRiZDY2NjRkLTRlYjktNDZlYi05OWQ4LTVjNDNiYTE1M2M2MSIsImMiOjl9)

Once the pipeline is running, connect your BI tool (Power BI, Looker, Tableau) to the `food_delivery_analytics` dataset in BigQuery to create dashboards. Key tables to visualize: 

![Dashboard Preview](https://github.com/RayenHasni/Food_Delivery_Analytics/blob/main/docs/Dashboard.png)

- `fct_orders` - Sales trends, order metrics, performance KPIs
- `dim_customers` + `fct_orders` - Customer segmentation and lifetime value
- `dim_restaurants` + `fct_orders` - Restaurant performance and rankings
- `dim_dates` + `fct_orders` - Time series analysis and seasonality

## 📄 License

This project is open source and available for learning and reference purposes.

## 🤝 Contributing

Contributions are welcome! Feel free to fork, improve, and submit pull requests.
