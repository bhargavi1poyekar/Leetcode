# Write your MySQL query statement below
# Ferbruary -  2020-02-01 -  2020-02-28

Select product_name, sum(unit) as unit from Orders o
LEFT JOIN Products p on o.product_id = p.product_id
Where month(order_date)=2 and year(order_date) = 2020 
Group By product_name
having sum(unit) >= 100;


-- Select sum(unit) from Orders
-- Group by order_date, prodcut);
