# Write your MySQL query statement below
Select user_id, 
Concat(Upper(substring(name,1,1)), Lower(substring(name, 2,Length(name)))) as name 
from users
order by user_id;