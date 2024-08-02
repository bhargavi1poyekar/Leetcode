# Write your MySQL query statement below

Select project_id, round(Avg(experience_years), 2) as average_years from Project p
Left Join Employee e on p.employee_id = e.employee_id
Group by project_id;

