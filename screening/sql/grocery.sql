/* 
sales (
    product_id
    store_id
    customer_id
    promotion_id
    store_sales
    store_cost
    units_sold
    transaction_date
)

products (
    product_id
    product_class_id
    brand_name
    product_name
    is_low_fat_flg
    is_recyclable_flg
    gross_weight
    net_weight
)

promotions (
    promotion_id
    promotion_name
    media_type
    cost
    start_date
    end_date
)

product_classes (
    product_class_id
    product_subcategory
    product_category
    product_department
    product_family
) 
 */

-- What percent of all products in the grocery chain's catalog are both low fat and recyclable?
select 
    count(case when is_low_fat_flg = 'Y' and is_recyclable_flg ='Y' then product_id end) * 100
        / count(product_id) as perc
from products

-- What are the top five (ranked in decreasing order) single-channel media types that correspond to the 
-- most money the grocery chain had spent on its promotional campaigns?
select media_type
from promotions
where media_type not like '%,%'
group by media_type
order by sum(cost) desc
limit 5

SELECT media_type, SUM(cost) FROM (
    SELECT DISTINCT media_type, s.promotion_id, cost
    FROM promotions p
    JOIN sales s
    ON p.promotion_id = s.promotion_id
    JOIN products pd
    ON pd.product_id = s.product_id
    JOIN product_classes pc
    ON pc.product_class_id = pd.product_class_id
    WHERE s.promotion_id > 0
    AND media_type NOT LIKE "%,%"
    AND product_department = "grocery"
) t
GROUP BY media_type
ORDER BY SUM(cost) DESC
LIMIT 5;

-- Find top 5 sales products having promotions
select product_id
from sales s 
where promotion_id is not null
group by product_id
order by sum(store_cost * units_sold) desc
limit 5

-- What percentage of sales happened on first and last day of the promotion?
select s.product_id,
    sum(case when s.transaction_date = p.start_date then (store_cost * units_sold) end) * 100 / sum((store_cost * units_sold)) as first_perc,
    sum(case when s.transaction_date = p.end_date then (store_cost * units_sold) end) * 100 / sum((store_cost * units_sold)) as last_perc
from sales s
join promotion p on p.promotion_id = s.promotion_id
group by product_id

-- Percent of sales that had a valid promotion, the VP of marketing
-- wants to know what percent of transactions occur on either
-- the very first day or the very last day of a promotion campaign.
select count(case when s.promotion_id > 0 then store_sales end) * 100 / (select count(s.store_sales) FROM sales)
from sales s
join promotion p on p.promotion_id = s.promotion_id
where s.transaction_date = p.start_date and s.transaction_date = p.end_date

select sum(case when s.transaction_date in (p.start_date, p.end_date) then 1 else 0 end) * 100 / count(*)
from sales s
join promotion p on p.promotion_id = s.promotion_id

-- What brands have an average price above $3 and contain at least 2 different products?
select p.brand_name
from products p 
join sales s on s.product_id = p.product_id
group by p.brand_name
having count(distinct product_id) >= 2
-- avg price per transaction
and avg(store_cost) > 3
-- avg price for each units sold
and sum(store_cost * units_sold) / sum(units_sold) >= 3

-- To improve sales, the marketing department runs various types of promotions.
-- The marketing manager would like to analyze the effectiveness of these promotion campaigns.
-- In particular, what percent of our sales transactions had a valid promotion applied?
select sum(case when promotion_id is not null then 1 end) * 100 / count(*)
from sales

-- We want to run a new promotion for our most successful category of products
-- (we call these categories “product classes”).
-- Can you find out what are the top 3 selling product classes by total sales?
select pc.product_class_id
from sales s 
join product p on p.product_id = s.product_id
join product_classes pc on pc.product_class_id = p.product_class_id
group by pc.product_class_id
order by sum(store_sales) desc
limit 3

-- We are considering running a promo across brands. We want to target
-- customers who have bought products from two specific brands.
-- Can you find out which customers have bought products from both the
-- “Fort West" and the "Golden" brands?
select customer_id
from sales s
from product p on p.product_id = s.product_id
where p.brand_name in ('Fort West', 'Golden')
group by customer_id
having count(distinct brand_name) = 2

-- Which product had the highest sales with promotions and sales?
select product_name, sum(store_sales) as sales
from sales s
join products p
on s.product_id = p.product_id
where promotion_id is not null
group by product_id
order by sales desc
LIMIT 1

-- Manager want to analyze the how the promotions on certain products are performing.
-- Find the percent of promoted sales?
select product_id,
    sum(case when promotion_id is not null then 1 else 0 end) * 100 / count(*)
from sales
group by product_id

-- Get the top 3 product_class_id by the total sales.
select product_class_id
from sales s 
join products p on p.product_id = s.product_id
group by p.product_class_id
order by sum(store_sales) desc
limit 3

-- Percentage increase in revenue compared to promoted and non-promoted products.
select product_id,
    sum(case when promotion_id is not null then store_cost * units_sold end) * 100 /
    sum(case when promotion_id is null then store_cost * units_sold end)
from sales
group by product_id

-- Product classes that has the highest transactions
select product_class_id
from sales s 
join products p on p.product_id = s.product_id
group by p.product_class_id
order by count(*) desc

-- Write a query that returns product_family, total units_sold and percentage of promoted.
select pc.product_family, sum(s.units_sold),
    sum(case when pc.promotion_id > 1 then 1 else 0 end) * 100.0 /
    sum(case when pc.promotion_id = 0 then 1 else 0 end)
from sales s 
join products p on p.product_id = s.product_id
join product_class pc on pc.product_class_id = p.product_class_id
group by pc.product_family

-- Write a query that returns percentage of unsold product categories.
with unsold_product_category as (
    select a.product_class_id, a.product_category
    from product_classes pc
    join products p on p.product_class_id = pc.product_class_id
    where p.product_id not in (select distinct product_id from sales)
)
select ((select count(distinct product_class_id) from unsold_product_category) / count(product_class_id)) *100
from product_classes 


with sold_product_category as (
    select distinct product_category
    from sales s
    join products p on p.product_id = s.product_id
    join product_classes pc on pc.product_class_id = p.product_class_id
)
select 
    count(case when product_category not in (select product_category from sold_product_category)
        then product_category) * 1.0
    / count(product_class_id)
from product_classes 

select count(distinct case when s.product_id is null then pc.product_category) / count(distinct product_category)
from product_classes pc
join products p on p.product_class_id = pc.product_class_id
left join sales s on s.product_id = p.product_id