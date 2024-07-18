--Знайти оцінки студентів у окремій групі з певного предмета:


SELECT students.name AS student_name, groups.name AS group_name, subjects.name AS subject_name, grades.grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN groups ON students.group_id = groups.id
JOIN subjects ON grades.subject_id = subjects.id
WHERE students.group_id = 1 -- змініть на відповідний ID групи
AND grades.subject_id = 2;  -- змініть на відповідний ID предмета
