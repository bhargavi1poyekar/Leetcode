# Write your MySQL query statement below

Select * from Cinema
where Mod(id, 2) !=0  and description != "boring"
Order by rating DESC;
