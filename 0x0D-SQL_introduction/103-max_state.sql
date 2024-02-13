-- Script that displays the maximum temp
-- of each state, ordered by state name.
SELECT `state`, MAX(`value`) AS `max_tmp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;
