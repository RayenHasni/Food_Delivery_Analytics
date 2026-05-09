Welcome dbt project!

### Using the starter project

Try running the following commands:
- dbt run
- dbt test

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

### Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices
