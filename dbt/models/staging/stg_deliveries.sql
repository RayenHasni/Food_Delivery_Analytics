select
    delivery_id,
    order_id,
    driver_id,
    delivery_time_min,
    distance_km,
    rating
from {{ source('raw', 'deliveries') }}