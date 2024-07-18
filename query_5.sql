
--Знайти які курси читає певний викладач:


SELECT teachers.name AS teacher_name, subjects.name AS course_name
FROM subjects
JOIN teachers ON subjects.teacher_id = teachers.id
WHERE subjects.teacher_id = 4; -- змініть на відповідний ID викладача
