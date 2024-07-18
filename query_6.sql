--Знайти список студентів у певній групі:


SELECT students.name AS student_name, groups.name AS group_name
FROM students
JOIN groups ON students.group_id = groups.id
WHERE students.group_id = 3; -- змініть на відповідний ID групи
