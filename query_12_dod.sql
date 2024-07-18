WITH LastGradeDate AS (
    SELECT
        s.group_id,
        g.subject_id,
        MAX(g.date) AS last_date
    FROM
        grades g
    JOIN
        students s ON g.student_id = s.id
    WHERE
        s.group_id = 1 -- Змініть на відповідний ID групи
        AND g.subject_id = 1 -- Змініть на відповідний ID предмета
    GROUP BY
        s.group_id, g.subject_id
)

SELECT
    grp.name AS group_name,              -- Назва групи
    subj.name AS subject_name,          -- Назва предмета
    lg.last_date AS last_grade_date,    -- Остання дата оцінки
    s.name AS student_name,             -- Ім'я студента
    g.grade AS grade                    -- Оцінка на цю дату
FROM
    LastGradeDate lg
JOIN
    grades g ON lg.last_date = g.date
JOIN
    students s ON g.student_id = s.id
JOIN
    groups grp ON s.group_id = grp.id
JOIN
    subjects subj ON g.subject_id = subj.id
WHERE
    g.subject_id = 3 -- Змініть на відповідний ID предмета
    AND grp.id = 2 -- Змініть на відповідний ID групи
    AND g.date = lg.last_date
ORDER BY
    grp.name, subj.name, s.name;
