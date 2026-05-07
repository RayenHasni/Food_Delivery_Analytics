select
    customer_id,
    zone,
    latitude,
    longitude,
    tier,
    signup_date,
    is_active
from {{ source('raw', 'customers') }}