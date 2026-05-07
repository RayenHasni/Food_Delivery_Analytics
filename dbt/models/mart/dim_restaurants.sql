select
    restaurant_id,
    name,
    cuisine,
    zone,
    is_open,
    avg_rating,
    avg_delivery_time_min

from {{ ref('stg_restaurants') }}