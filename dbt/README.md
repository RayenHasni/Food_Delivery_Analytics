Welcome dbt project!

## 🚀 Quick Start

Try running the following command:
- `dbt build` (or `dbt run` then `dbt test`)

Generate interactive dbt documentation locally:

- `dbt docs generate`
- `dbt docs serve`

---
## 🔀 Data Flow

![Preview](https://github.com/RayenHasni/Food_Delivery_Analytics/blob/main/docs/Data%20Flow.gif)


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

---

## 🛠️ Data Quality & Testing

Data quality is enforced through automated dbt tests integrated into the deployment workflow.

### Included Tests

- `not_null`
- `unique`
- `relationships`
- `accepted_values`

---

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
