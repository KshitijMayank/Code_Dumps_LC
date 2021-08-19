CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
      select Salary as getNthHighestSalary  from 
      
      ( select * , DENSE_RANK() OVER (Order by Salary DESC) drank from Employee
      ) A 
      where drank = N limit 1
  );
END