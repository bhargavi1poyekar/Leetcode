# Write your MySQL query statement below

Select c.name as Customers from Customers c
Left Join Orders o on c.id = o.customerId
Where o.id is null;

-- Select Customers.name as Customers from Customers left join Orders ON
-- Customers.id=Orders.customerId where Orders.id is null