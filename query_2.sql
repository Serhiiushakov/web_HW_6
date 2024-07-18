-- Знайти студента з найвищим середнім балом з певного предмета:
SELECT students.name, subjects.name AS subject_name, AVG(grades.grade) AS avg_grade
FROM students
JOIN grades ON students.id = grades.student_id
JOIN subjects ON grades.subject_id = subjects.id
WHERE grades.subject_id = 4 -- змініть на відповідний ID предмета
GROUP BY students.id, subjects.name
ORDER BY avg_grade DESC
LIMIT 1;

