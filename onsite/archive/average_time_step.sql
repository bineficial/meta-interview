DROP table if EXISTS sessions;
create table sessions (
	session_id INT,
  	step INT,
  	ts TIMESTAMP
);

INSERT INTO sessions (session_id, step, ts)
VALUES
  (1,	1,	'2023-10-27 01:01:00'),
  (1,	2,	'2023-10-27 01:01:30'),
  (1,	3,	'2023-10-27 01:02:00'),
  (1,	3,	'2023-10-27 01:02:30'),
  (1,	4,	'2023-10-27 01:03:00')
 ;

with sessions as (
	select *, ROW_NUMBER() OVER(partition by session_id, step order by ts) as rn
	from sessions
)
, dedupe_sessions as (
  select *
  from sessions
  WHERE rn = 1
)

, step_seconds as (
  select s1.session_id, s1.step, sum(extract(epoch from s2.ts - s1.ts)) as total_sec
  from dedupe_sessions s1
  left join dedupe_sessions s2
      on s2.session_id = s1.session_id
      and s2.step - 1 = s1.step
  group by s1.session_id, s1.step
 )
 
 select step, sum(total_sec) / count(distinct session_id)
 from step_seconds
 group by step