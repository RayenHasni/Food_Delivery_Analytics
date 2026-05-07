with source as (

    select * from {{ source('raw', 'orders') }}

),

cleaned as (

    select
        order_id,
        customer_id,
        restaurant_id,
        order_datetime,
        date(order_datetime) as order_date,
        EXTRACT(HOUR FROM order_datetime) AS order_hour,
        order_value,
        discount,
        final_value,
        payment_method,
        status,
        rating

    from source

)

select * from cleaned