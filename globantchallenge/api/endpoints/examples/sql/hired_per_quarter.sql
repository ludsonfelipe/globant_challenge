SELECT 
    d.department AS department,
    j.job AS job,
    SUM(CASE WHEN EXTRACT(quarter FROM e.datetime) = 1 THEN 1 ELSE 0 END) AS Q1,
    SUM(CASE WHEN EXTRACT(quarter FROM e.datetime) = 2 THEN 1 ELSE 0 END) AS Q2,
    SUM(CASE WHEN EXTRACT(quarter FROM e.datetime) = 3 THEN 1 ELSE 0 END) AS Q3,
    SUM(CASE WHEN EXTRACT(quarter FROM e.datetime) = 4 THEN 1 ELSE 0 END) AS Q4
FROM
    hired_employees e
LEFT JOIN
    departments d ON e.department_id = d.id
LEFT JOIN
    jobs j ON e.job_id = j.id
WHERE
    EXTRACT(year FROM e.datetime) = 2021 /* year to filter the hired employees by */    
GROUP BY
    d.department, j.job
ORDER BY
    d.department, j.job;
