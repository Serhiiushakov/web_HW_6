-- Знайти середній бал у групах з певного предмета:
SELECT groups.name AS group_name, subjects.name AS subject_name, AVG(grades.grade) AS avg_grade
FROM groups
JOIN students ON groups.id = students.group_id
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.subject_id = 3 -- змініть на відповідний ID предмета
GROUP BY groups.id, subjects.name;

