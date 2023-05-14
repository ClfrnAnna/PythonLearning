SELECT em.name, jt.job, jt.salary 
FROM employee AS em
JOIN job_title jt ON em.job_title_id = jt.id
JOIN vacation vac ON em.id = vac.employee_id
WHERE em.child = true 
OR em.retiree = true
AND CURRENT_DATE 
BETWEEN vac.data_from and data_to;

SELECT em.id, em.name, jt.job 
FROM employee AS em
JOIN job_title jt ON em.job_title_id = jt.id;

SELECT em.id, em.name, fj.* FROM employee as em
LEFT JOIN former_job fj on em.id = fj.employee_id;