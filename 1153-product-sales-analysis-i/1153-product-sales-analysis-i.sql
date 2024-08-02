# Write your MySQL query statement below
SELECT p.product_name as  product_name, s.year as year, s.price as price
from Sales s JOIN Product p on s.product_id=p.product_id; 