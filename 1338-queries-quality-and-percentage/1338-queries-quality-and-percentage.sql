# Write your MySQL query statement below
Select query_name, 
round(Avg(rating/position),2) as quality,
round(Avg(Case when rating < 3 then 1 else 0 end)*100,2) as poor_query_percentage
from Queries
where query_name is not null
Group By query_name; 

