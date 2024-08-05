# Write your MySQL query statement below
Select x,y,z, 
case
when x+y > z and x+z > y and y+z > x then "Yes"
when x=y and y=z then "Yes"
else "No" 
end as triangle
from Triangle;