# Write your MySQL query statement below
Select Email from
(Select Email, count(email) 
from person group by Email having count(email)>1) a