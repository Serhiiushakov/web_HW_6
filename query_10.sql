--Список курсів, які певному студенту читає певний викладач:

SELECT students.name AS student_name, subjects.name AS subject_name, teachers.name AS teacher_name
FROM grades
JOIN students ON students.id = grades.student_id
JOIN subjects ON subjects.id = grades.subject_id
JOIN teachers ON teachers.id = subjects.teacher_id
WHERE grades.student_id = 2  -- Замініть на відповідний ID студента
AND subjects.teacher_id = 1;  -- Замініть на відповідний ID викладача
