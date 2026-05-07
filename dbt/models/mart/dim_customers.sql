select
    customer_id,
    zone,
    tier,
    is_active,
    signup_date,
    latitude,
    longitude
from {{ ref('stg_customers') }}