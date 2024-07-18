
--Знайти середній бал на потоці (за всіма таблицями оцінок):
--SELECT AVG(grade) AS avg_grade
--FROM grades;

SELECT printf('Current average score: %.2f', AVG(grade)) AS avg_grade
FROM grades;