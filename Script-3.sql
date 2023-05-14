SELECT em.id, em.name, jt.job 
FROM employee AS em
JOIN job_title jt 
ON em.job_title_id = jt.id;