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
    id
    product_class_id
    brand_name
    product_name
    is_low_fat_flg
    is_recyclable_flg
    gross_weight
    net_weight
)

promotions (
    id
    promotion_name
    media_type
    cost
    start_date
    end_date
)

product_classes (
    id
    product_class_name
    product_subcategory
    product_category
    product_department
    product_family
) 
 */

-- What percent of all products in the grocery chain's catalog are both low fat and recyclable?
select sum(case when is_low_fat_flg and is_recyclable_flg then 1 else 0 end) / count(product_id)
from products

-- What are the top five (ranked in decreasing order) single-channel media types that correspond to the 
-- most money the grocery chain had spent on its promotional campaigns?
select media_type
from promotions
where media_type not like '%,%'
group by media_type
order by sum(cost) desc
limit 5


-- Find top 5 sales products having promotions
select product_id
from sales
join promotions
    on promotions.promotion_id = sales.promotion_id
order by sum(store_sales * units_sold) desc
limit 5

-- What percentage of sales happened on first and last day of the promotion?
select
    sum(case when transaction_date = promotions.start_date or transaction_date = promotions.end_date then store_sales else 0 end) / sum(store_sales)
from sales
join promotions
    on promotions.promotion_id = sales.promotion_id



-- Percent of sales that had a valid promotion, the VP of marketing
-- wants to know what percent of transactions occur on either
-- the very first day or the very last day of a promotion campaign.
select sum(case when sales.transaction_date = promotions.start_date or sales.transaction_date = end_date then 1 else 0 end) / count(*)
from sales
join promotions
    on promotions.promotion_id = sales.promotion_id





-- What brands have an average price above $3 and contain at least 2 different products?
select
from sales
join products
    on products.product_id = sales.product_id
group by brand_name
having sum(store_cost) / sum(units_sold) > 3
and count(distinct product_id) >= 2






-- To improve sales, the marketing department runs various types of promotions.
-- The marketing manager would like to analyze the effectiveness of these promotion campaigns.
-- In particular, what percent of our sales transactions had a valid promotion applied?
select sum(case when promotion_id is not null then 1 else 0 end) / count(*)
from sales






-- We want to run a new promotion for our most successful category of products
-- (we call these categories “product classes”).
-- Can you find out what are the top 3 selling product classes by total sales?
select product_class_name
from sales
join products
    on products.id = sales.product_id
join product_class
    on product_class.id = products.product_class_id
group by product_class_name
order by sum(units_sold) desc
limit 3





-- We are considering running a promo across brands. We want to target
-- customers who have bought products from two specific brands.
-- Can you find out which customers have bought products from both the
-- “Fort West" and the "Golden" brands?
select customer_id
from sales
join products
    on products.id = sales.product_id
where brand_name in ('Fort West', 'Golden')
group by customer_id
having count(distinct brand_name) == 2



-- Which product had the highest sales with promotions and sales?
select product_id
from sales
where promotion_id is not null
order by sum(store_cost * units_sold) desc


-- Manager want to analyze the how the promotions on certain products are performing.
-- Find the percent of promoted sales?
select sum(case when promotion_id is not null then 1 else 0 end) / count(*)
from sales



-- Get the top 3 product_class_id by the total sales.
select product_class_id
from sales
join product
    on product.id = sales.product_id
join product_class
    on product_class.id = product.product_class_id
group by product_class_id
order by sum(units_sold * store_sales) desc





-- Percentage increase in revenue compared to promoted and non-promoted products.
select
    product_id,
    sum(case when promotion_id is not null then units_sold * store_sales else 0 end) / sum(case when promotion_id is null then units_sold * store_sales else 0 end)
from sales
group by product_id




-- Product classes that has the highest transactions
select product_class_id
from sales
join products
    on products.id = sales.product_id
join product_class
    on product_class.id = product.product_class_id
group by product_class_id
order by count(*) desc



-- Write a query that returns product_family, total units_sold and percentage of promoted.
select
    product_family,
    sum(units_sold),
    sum(case when promotion_id is not null then 1 else 0 end) / count(*)
from sales
join product
    on product.id = sales.product_id
join product_class
    on product_class.id = product.product_class_id
group by product_family





-- Write a query that returns percentage of unsold product categories.
select
    count(distinct select case when sale.product_id is null then product_category end) / count(distinct product_category)
from product
join product_class
    on product_class.id = product.product_class_id
left join sales
    on sales.product_id = product.id


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