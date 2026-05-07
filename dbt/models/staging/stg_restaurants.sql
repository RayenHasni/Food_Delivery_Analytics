select
    restaurant_id,
    name,
    cuisine,
    zone,
    latitude,
    longitude,
    avg_rating,
    avg_delivery_time_min,
    is_open
from {{ source('raw', 'restaurants') }}