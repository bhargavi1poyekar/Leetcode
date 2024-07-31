# Write your MySQL query statement below
Select e.name as name, b.bonus as bonus
from Employee e 
left join Bonus B
on e.empId=b.empId
where b.bonus<1000 or b.bonus is NULL; 