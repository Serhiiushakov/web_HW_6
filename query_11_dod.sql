--Середній бал, який певний викладач поставить певному студентові.

SELECT
    students.name AS student_name,
    teachers.name AS teacher_name,
    subjects.name AS subject_name,
    AVG(grades.grade) AS avg_grade
FROM
    grades
JOIN
    students ON grades.student_id = students.id
JOIN
    subjects ON grades.subject_id = subjects.id
JOIN
    teachers ON subjects.teacher_id = teachers.id
WHERE
    students.id = 4 -- змініть на відповідний ID студента
    AND teachers.id = 1 -- змініть на відповідний ID викладача
GROUP BY
    students.name, teachers.name, subjects.name;
