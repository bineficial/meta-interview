-- date, user_id, first_active_date, last_active_date, previous_active_date
select
    count(case when datediff(dd, last_active_date, previous_active_date) = 1 and date = last_active_date then user_id end) as active_users
    , count(case when date = first_active_date then user_id end) as new_users
    , count(case when date = last_active_date and datediff(dd, last_active_date, previous_active_date) > 1 then user_id end) as returning_users
    , count(case when datediff(dd, date, last_active_date) >= 30) churned_users
from cumulative
where date = current_date()


select
    daily.date
    , coalesce(cumulative.user_id, daily.user_id) as user_id
    , coalesce(cumulative.first_active_date, daily.date) as first_active_date
    , coalesce(daily.date, cumulative.last_active_date) as last_active_date
    , case when daily.user_id is not null then cumulative.last_active_date else cumulative.previous_active_date end as previous_active_date
from cumulative
full outer join daily
    on daily.user_id = cumulative.user_id
    and daily.date = cumulative.date + interval '1 day'