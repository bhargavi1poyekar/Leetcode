# Write your MySQL query statement below

-- Select d.product_id, round((sum(price*units)+0.00)/(sum(units)+0.00),2) as average_price
-- from(
-- Select *
-- from prices p
-- natural join 
-- unitssold u
-- where u.purchase_date between p.start_date and p.end_date) d
-- group by d.product_id 

SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id
