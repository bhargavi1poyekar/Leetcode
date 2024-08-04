# Write your MySQL query statement below

Select s.name from Salesperson s where s.name not in 
(Select s.name from SalesPerson 
Left Join Orders o on s.sales_id = o.sales_id
Left Join Company c on c.com_id = o.com_id
where c.name = "RED");



