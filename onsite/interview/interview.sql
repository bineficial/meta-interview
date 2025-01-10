-- calculate based on snapshot table based on today
-- (ds user_id first_dt last_dt prev_dt)
-- active user
-- new user
-- return user
-- churn user

select
    count(case when coalesce(datediff(last_dt, prev_dt), 0) = 1 then user_id end) as active_user,
    count(case when prev_dt is null then user_id end) as new_user,
    count(case when coalesce(datediff(last_dt, prev_dt), 0) > 1 then user_id end) as return_user,
    count(case when last_dt <> today() then user_id end) as churned_user
from cumulative
where ds = today()

-- load snapshot table based on transaction table
-- ds user_id first_dt last_dt prev_dt
select 
    d.ds,
    d.user_id,
    coalesce(c.first_dt, d.ds) as first_dt,
    d.ds as last_dt,
    c.last_dt as prev_dt
from daily d
left join cumulative c 
    on c.user_id = d.user_id
        and  datediff(d.ds, c.ds) = 1


-- uber
-- calculate average waiting time
select sum(pick_up_ts - request_ts) / count(*)
from fact_ride

-- how to calcualte how many drivers have spent more than total four hours with passengers
select count(distinct rider_id)
from (
    select rider_id
    from fact_ride
    group by driver_id
    having sum(drop_off_ts - pick_up_ts) > 4
) a

-- how many driver used the airport
select count(distinct rider_id)
from fact_ride r
join dim_location pu on pu.id = r.pick_up_id
join dim_location dof on dof.id = r.drop_off_id
where pu.type = 'Airport' or dof.type = 'Airport'

-- count riders who have only used uber to go to and from airport
select count(rider)
from (
    select distinct rider_id
    from fact_ride r
    join dim_location pu on pu.id = r.pick_up_id
    join dim_location dof on dof.id = r.drop_off_id
    where pu.type = 'Airport' or dof.type = 'Airport'
    group by rider_id
    having distinct(count pu.type) <= 2 and distinct(count do.type) <= 2
)

-- step model
-- step can duplicated
-- (session_id, step, timestamp)
select step, sum(total_sec) / count(distinct session_id)
from (
    select session_id, step, min(s2.timestamp) - min(s1.timestamp) as total_sec
    from session s1
    left join session s2 
        on s2.session_id = s1.session_id
            and s2.step - 1 = s1.step
    group by session_id, step
)
group by step