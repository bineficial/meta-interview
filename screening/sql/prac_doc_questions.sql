/* 
Salesperson (
    id
    name
    age
    salary
)

Customer (
    id
    name
    city
    industry_type
)

Orders (
    number
    order_date
    cust_id
    salesperson_id
    amount
)
 */

-- The names of all salespeople that have an order with Samsonic.
select sp.name
from salesperson sp
join orders o on o.salesperson_id = sp.id
join customer c on c.id = o.cust_id
where c.name = 'Samsonic'

-- The names of all salespeople that do not have any order with Samsonic.
select name
from salesperson
where id not in (
    select distinct salesperson_id
    from orders o 
    join customer c on c.id = o.cust_id
    where c.name = 'Samsonic'
)

-- The names of salespeople that have 2 or more orders.
select sp.name
from salesperson sp 
join orders o on o.salesperson_id = sp.id
group by sp.id
having count(*) >= 2

-- The names and ages of all salespersons must having a salary of 100,000 or greater.
select sp.name, sp.ages
from salesperson sp
where salary >= 100000

-- What sales people have sold more than 1400 total units?
select sp.name
from orders o 
join salesperson sp on sp.id = o.salesperson_id
group by o.salesperson_id
having sum(amount) > 1400

-- When was the earliest and latest order made to Samony?
select min(order_date) as earliest_order, max(order_date) as latest_order
from orders o 
join customer c on c.id = o.cust_id 
where c.name = 'Samony'

-- Count of Customers who bought 2 items type (A,B)
select count(name) AS count
from customer
where id in (
    select cust_id
    from orders
    where product_name in ('A','B')
    group by cust_id
    having count(distinct product_name) = 2
);