--Знайти середній бал, який поставив певний викладач зі своїх предметів:

SELECT teachers.name AS teacher_name, AVG(grades.grade) AS avg_grade
FROM grades
JOIN subjects ON grades.subject_id = subjects.id
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE subjects.teacher_id = 4; -- змініть на відповідний ID викладача