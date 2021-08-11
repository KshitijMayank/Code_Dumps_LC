# Write your MySQL query statement below

Select Email From
(
Select Count(*) As Counted,
    Email From Person Group By Email )A 
    
    Where A.Counted > 1
