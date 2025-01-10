DROP table if EXISTS cumulative;
create table cumulative (
	date DATE,
  	user_id INT,
  	first_active_date DATE,
    last_active_date DATE,
    previous_active_date DATE
);

INSERT INTO cumulative (date, user_id, first_active_date, last_active_date, previous_active_date)
VALUES
  ('2020-01-01',	1,	'2019-01-01',	'2020-01-01',	'2019-12-31'),
  ('2020-01-01',	2,	'2020-01-01',	'2020-01-01', NULL),
  ('2020-01-01',	3,	'2019-01-01',	'2020-01-01',	'2019-11-01'),
  ('2020-01-01',	4,	'2019-01-01',	'2019-06-01',	'2019-05-30'),
  ('2020-01-01',	5,	'2020-01-01',	'2019-05-01',	NULL)
 ;
 
DROP table if EXISTS daily;
create table daily (
	date DATE,
  	user_id INT
);

INSERT INTO daily (date, user_id)
VALUES
  ('2020-01-02',	1),
  ('2020-01-02',	2),
  ('2020-01-02',	3),
  ('2020-01-02',	6),
  ('2020-01-02',	7)
 ;
 
 
select
	count(case when last_active_date - previous_active_date = 1 and date = last_active_date then user_id end) as active_users
	, count(case when date = first_active_date then user_id end) as new_users
    , count(case when date = last_active_date and last_active_date - previous_active_date > 1 then user_id end) as returning_users
    , count(case when date - last_active_date >= 30 THEN user_id END) churned_users
from cumulative
;


select *
    daily.date
    , coalesce(cumulative.user_id, daily.user_id) as user_id
    , coalesce(cumulative.first_active_date, daily.date) as first_active_date
    , coalesce(daily.date, cumulative.last_active_date) as last_active_date
    , case when daily.user_id is not null then cumulative.last_active_date else cumulative.previous_active_date end as previous_active_date
from cumulative
full outer join daily
    on daily.user_id = cumulative.user_id
    and daily.date = cumulative.date + interval '1 day'