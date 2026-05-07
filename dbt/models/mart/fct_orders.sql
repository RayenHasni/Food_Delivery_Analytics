with orders as (

    select *
    from {{ ref('stg_orders') }}

),

deliveries as (

    select *
    from {{ ref('stg_deliveries') }}

)

select
    o.order_id,
    o.customer_id,
    o.restaurant_id,
    d.delivery_id,
    d.driver_id,
    o.order_date,
    o.order_hour,
    d.delivery_time_min,
    d.distance_km,
    o.rating as order_rating,
    d.rating as delivery_rating,
    o.order_value,
    o.discount,
    o.final_value,
    o.payment_method,
    o.status

from orders o
left join deliveries d
    on o.order_id = d.order_id