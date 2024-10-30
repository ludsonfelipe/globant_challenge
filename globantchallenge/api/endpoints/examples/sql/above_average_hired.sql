WITH average_hired_employees AS (
    SELECT 
       CAST(COUNT(e.id) AS FLOAT)/
        (SELECT COUNT(DISTINCT id) FROM departments) as avg_employees
    FROM
        hired_employees e
    WHERE 
        EXTRACT(year FROM e.datetime) = 2021
)

SELECT 
    d.id,
    d.department AS department,
    COUNT(e.id) AS hired
FROM
    hired_employees e
LEFT JOIN
    departments d ON e.department_id = d.id
GROUP BY
    d.id,d.department
HAVING
    COUNT(e.id) > (SELECT avgh.avg_employees FROM average_hired_employees avgh)
ORDER BY 
    hired DESC;