CREATE OR REPLACE VIEW links_violation AS (
       SELECT fid
       FROM cf
       WHERE sid = 1
);
