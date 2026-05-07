with dates as (

    select
        date
    from unnest(generate_date_array('2024-01-01', '2030-12-31')) as date

)

select
    date,
    extract(year from date) as year,
    extract(month from date) as month,
    format_date('%B', date) as month_name,
    extract(day from date) as day,
    extract(dayofweek from date) as day_of_week,
    extract(week from date) as week_of_year,
    extract(quarter from date) as quarter
from dates