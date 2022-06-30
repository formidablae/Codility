-- write your code in PostgreSQL 9.4
-- Given a table elements with the following structure:

--   create table elements (
--       v integer not null
--   );
-- write an SQL query that returns the sum of the numbers in column v.

-- For example, given:

--   v
--   ---
--   2
--   10
--   20
--   10
-- your query should return 42.

SELECT sum(v) FROM elements;
