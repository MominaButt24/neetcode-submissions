-- Write your query below
select name 
from customers
where id not in
(
    select customer_id
    from orders
)

-- SELECT c.name
-- FROM customers c
-- LEFT JOIN orders o ON c.id = o.customer_id
-- WHERE o.customer_id IS NULL;
