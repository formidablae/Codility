-- write your code in PostgreSQL 9.4
-- Given a table events with the following structure:

--   create table events (
--       event_type integer not null,
--       value integer not null,
--       time timestamp not null,
--       unique(event_type, time)
--   );
-- write an SQL query that, for each event_type that has been registered more than once, returns the difference between the latest (i.e. the most recent in terms of time) and the second latest value. The table should be ordered by event_type (in ascending order).

-- For example, given the following data:

--    event_type | value      | time
--   ------------+------------+--------------------
--    2          | 5          | 2015-05-09 12:42:00
--    4          | -42        | 2015-05-09 13:19:57
--    2          | 2          | 2015-05-09 14:48:30
--    2          | 7          | 2015-05-09 12:54:39
--    3          | 16         | 2015-05-09 13:19:57
--    3          | 20         | 2015-05-09 15:01:09
-- your query should return the following rowset:

--    event_type | value
--   ------------+-----------
--    2          | -5
--    3          | 4
-- For the event_type 2, the latest value is 2 and the second latest value is 7, so the difference between them is −5.

-- The names of the columns in the rowset don't matter, but their order does.

-- SELECT latest of each event
