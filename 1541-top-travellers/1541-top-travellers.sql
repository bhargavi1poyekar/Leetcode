# Write your MySQL query statement below
Select name, IFNULL(sum(distance),0) as travelled_distance from Users u
LEFT Join Rides r on u.id = r.user_id
GROUP by u.id
Order by sum(distance) Desc, Name;