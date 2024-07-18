--Знайти список курсів, які відвідує студент

SELECT students.name AS student_name, subjects.name AS subject_name
FROM grades
JOIN students ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
WHERE grades.student_id = 1;  -- Замініть на відповідний ID студента
