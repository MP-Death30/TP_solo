-- init-haproxy.sql
CREATE USER IF NOT EXISTS 'haproxy_check'@'%' IDENTIFIED BY '';
GRANT USAGE ON *.* TO 'haproxy_check'@'%';
