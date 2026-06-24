-- Write your query below

-- it works t dont handl the same high score exams for one student
-- select student_id, exam_id, score
-- from exam_results
-- where (student_id , score) in
-- (select student_id, max(score)
-- from exam_results
-- group by student_id)
-- order by student_id

select distinct on (student_id)
student_id, exam_id, score
from exam_results
order by student_id asc, score desc, exam_id asc
