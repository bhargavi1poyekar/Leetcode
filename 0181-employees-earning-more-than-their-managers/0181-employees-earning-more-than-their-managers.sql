# Write your MySQL query statement below
Select e.name as Employee from Employee E, Employee M
where E.managerId = M.id 
AND E.salary > M.salary; 
