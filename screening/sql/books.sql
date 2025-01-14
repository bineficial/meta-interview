-- Identify authors who have published at least 5 books. 
select author
from author
join book on book.author_id = author.id
group by author.id
having count(book.id) >= 5

-- Calculate the percentage of total sales completed on the same day the customer registered: (Same day sales * 100.0) / Total sales. 
select
    sum(case when sales.date = customer.registeration_date then sale else 0) / sum(sale)
from sales
join customer
    on customer.id = sales.customer_id

-- Find customers who purchased 3 or more books on both the first and last day of sales, excluding those with only one transaction.
select customer_id
from sales
join promotions
  on promotions.id = sales.promotion_id
where
  sales.date = promotions.start_date or sales.date = promotions.end_date
group by customer_id
having sum(books_sold) >= 3 and count(id) != 1

-- Find the IDs of the top 5 customers, ordered by average payment per book made by the people they invited.
select customer.id
from sales
join customer.id = sales.invited_by_id
group by customer.id
order by sum(sale) / sum(books_sold) desc
top 5

-- Find the total number of authors registered with the bookstore. What percentage of them have a website URL that contains ".com", and what percentage never made a sale?
select sum(case when website like '%.com' then 1 else 0 end) / count(website)
from registery

select count(distinct case when sales.id is null then author.id else null end) / (count(distinct author.id) * 1.0)
from author
left join sales
  on sales.author_id = author.id
where sales.id is null


-- What was the total value of sales and the number of unique paying customers, grouped and sorted in descending order by payment type?
select
  payment_type,
  sum(sales),
  count(distinct customer_id)
from sales
group by payment_type
order by payment_type desc

-- Having a transaction table find the sum of total orders and the count of unique customers
select
  sum(sales),
  count(distinct customer_id)
from sales

-- Given 3 dimensional tables, (user, item, references), get the avg number of referrals per user who purchased item x.