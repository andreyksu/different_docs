graphite postgresql - ??? ??????????? ?? ??.  (http://eax.me/graphite-statsd-collectd/)
BMC TrueSight - ??? ???? ????????
Zabbix - ? ????????????? ?? ?????????



?????????? ??? ????????(?????????? ???????? ? ????? ?? ??????????)
	select queryid,query from pg_stat_statements where queryid in (4248211384,3054902337);
	
????? ????? ????? ??????? ??????????? ? ?????? ??????, ????? ??????? ?? ????????? ? ??????? ?????? ??? ????????. ? PostgreSQL ???? ???????? ????????? ???????? pg_stat_activity.
		select now() - query_start, pid, waiting, query from pg_stat_activity where state != 'idle' order by 1 desc;
		select now() - query_start, procpid, waiting, current_query from pg_stat_activity where current_query != '<IDLE>' order by 1 desc; (??? Postgresql-9.1)
	??????: ??????? ????? ??????? ? ?????? ?????? ??????????? ? ???? ??????.
	????????: pg_stat_activity ?????????? ??????? ??????? ?? ?????????(????????).
	???????: gdb.
		????????, ? ???? ??????? ???? ??????? ?????, ?? ?? ??? ?? ?????. ????? PID ?? ??????? ???? ? ???????????? ? ????
			gdb [path_to_postgres] [pid]
		? ????? ???? ??? ???????????? ? ???????? ?????????
			printf "%s\n", debug_query_string	
	
??????: ?????????? ????????? ???????
????????: ??????? ??????? ??? ?? ?????? ???? ??????
???????: log_min_duration_statement
	????????? log_min_duration_statement ???????? ? ?????????????, ? ???????? ??? ??????? ? ????, ??????? ??????????? ?????? ????????? ????????.	
	??????? ???????? ?????? PostgreSQL vim /var/lib/pgsql/9.4/data/posgresql.conf ? ???????? ? ??? 3 ??????? ??? ????????? ????????
		log_min_duration_statement = 3000 
	????? ????????? ???????? ? ???? ?? ??????????? ????????????? ????, ?????????? ????????? ??????? ?? psql, pgadmin ??? ??????? ?????????? ? ????
		SELECT pg_reload_conf();
	??? ????????? ?? ????????? ??????
		su - postgres
		/usr/bin/pg_ctl reload
	????? ???????, ??? ????????? ????????? ? ???????????????? ????? ??????? ? ???? ?????? ????? ??????????? ???? ??????.
	? ????? ????? ????? ?????????? ? ??? PostgreSQL, ??????? ? ??? ????????? ?? ?????? ???? /var/lib/pgsql/9.4/data/pg_log/postgresql-2015-07-07.log ? ????? ?????, ??? ???? ?????? ??????? ??????????? ????? 6 ??????.
		2015-07-07 09:39:30 UTC 192.168.100.82(45276) LOG:  duration: 5944.540 ms  statement: SELECT * FROM application_devices WHERE applicationid='1234' AND hwid='95ea842e368f6a64' LIMIT 1
	??? ??????? ? ??????????, ????? ?????????? ???-???? ????? ??????? ?????? logstash+elasticsearch+kibana ? ????? ????? ????? zabbix ??????????? ? ????????? ????????? ????????, ???? ??? ???????? ????????? ??? ???????.
	
??????: ??????, ??? ?????? ???????(??? ?????? ????? ??????? ???? ? ????)
????????: ??????? ?????? ????????? ??? ?????????????.
???????: strace
	??? ????? ?????????? ????? pid ???????? ??????? ????? ? ???????? ????? -T. ? ????? ????? strace ????? ???? ???????? ?????
		strace -p 27345 -s 1024 -T 2> out
	gettimeofday({1437846841, 447186}, NULL) = 0 <0.000004>
	sendto(8, "Q\0\0\0005SELECT * FROM accounts WHERE uid='25143' LIMIT 1\0", 54, MSG_NOSIGNAL, NULL, 0) = 54 <0.000013>
	poll([{fd=8, events=POLLIN|POLLERR}], 1, -1) = 1 ([{fd=8, revents=POLLIN}]) <0.000890>

	
	
????? ??? ??????? ?????????????, ?? ???? ?????????? ?? ???????? ?? ?? ??????? ???????, ? ?? ?????? ?????????? ? ????? ?????? pg ????????.
-? ?????? ????? ??????, ??? ??????? ???????????? ?? ????????? ????? ??????????. ??????? ?????? ??, ??? ??????? ? ?????? ??????????? ?????????? ? IN ???????????? ????????, ???? ?? ? ??? ?????? ???? ??????????.
-? ???? ?????, ??? ?? ????? ???? ??????? ??? ?? "????????" ?????? ??????? ????? ??????????????? ???????. ??????? ? 9.4 ?? ????????? ? ??????? queryid.
-?? ???????? ??? ?????????? ????????????? ??????????????? ? ???????????? ??????? ??? ? ??????. ????????, ?????? ?????????? ?????????? ? IN ?? ?????????? ? ???? ??????????? "(?)". ??? ?????????, ??????? ????????? ? pg ????????????? ? ?????? ?? ???? ???????? ?? ????????????. ?????? ??????????? ??? ? ???, ??? ????? ??????? ????? ???? ?? ??????.
-?? 9.4 ????? ??????? ?????????? ?? track_activity_query_size, c 9.4 ????? ??????? ???????? ??? ??????????? ?????? ? ??????????? ??????, ?? ?? ? ????? ?????? ???????? ?????? ?? 8??, ??? ??? ???? ? query ????? ????? ????????? ??????, ??????? ?? ?????? ??????? ????????? ????????.

??? ???????? ?????? ? ??????? ?????? ??? ? ?????? ?????? ????????? (pg_stat_statements_reset).
	query ? ????? ???????
	calls ? ?????????? ??????? ???????
	total_time ? ????? ?????? ?????????? ??????? ? ?????????????
	rows ? ?????????? ????? ???????????? (select) ??? ???????????????? ? ???? ??????? (update)
	shared_blks_hit ? ?????????? ?????? ??????????? ??????, ?????????? ?? ????
	shared_blks_read ? ?????????? ?????? ??????????? ??????, ??????????? ?? ?? ????
		? ???????????? ?? ????????, ??? ????????? ?????????? ??????????? ?????? ??? ?????? ??, ??? ?? ??????? ? ????, ????????? ?? ????
	shared_blks_dirtied ? ?????????? ?????? ??????????? ??????, ???????????????? ??? "???????" ? ???? ??????? (?????? ??????? ???? ?? ???? ?????? ? ????? ? ?????? ???? ?????????? ???????? ?? ????, ??? ?????? ??? checkpointer ??? bgwriter)
	shared_blks_written ? ?????????? ?????? ??????????? ?????? ?????????? ?? ???? ????????? ? ???????? ????????? ???????. ???????? ???????? ????????? ???????? ????, ???? ?? ??? ???????? "???????".
	local_blks ? ??????????? ???????? ??? ????????? ? ????? ?????? backend ??????, ???????????? ??? ????????? ??????
	temp_blks_read ? ?????????? ?????? ????????? ?????? ????????? ? ?????.
	????????? ????? ???????????? ??? ????????? ??????? ????? ?? ??????? ??????, ???????????? ?????????? work_mem
	temp_blks_written ? ?????????? ?????? ????????? ?????? ?????????? ?? ????
	blk_read_time ? ????? ??????? ???????? ?????? ?????? ?????????????
	blk_write_time ? ????? ??????? ???????? ?????? ?????? ?? ???? ? ????????????? (??????????? ?????? ?????????? ??????, ????? ??????????? checkpointer/bgwriter ????? ?? ???????????)
		blk_read_time ? blk_write_time ?????????? ?????? ??? ?????????? ????????? track_io_timing.
		

		
http://evtuhovich.ru/blog/2013/06/28/pg-stat-statements/


?????????? ???????? ? pg_stat_statements

?????? ??? ???????????? ??????? ????????? ??????, ????? ??????? ? ?? ??????????? ?????? ????? ??? ?????????? ?????????? ?????????? ??????? ??? ????????.

?? ?????? 9.2 ???????? ????? ?? ???? ?????? ????? ???? ???????? ? ??????? ??????? pgBadger. ???? ?????????? ????? ?????????? ??????? ????????? ??? ?????????, ????????? ? ????????????, ?? ? ?????????? ????? ???????? ?????????? ????????
?????. ? ?????????, ???? ?????? ????? ?????????? ????? ?????? ??????. ??-??????, ????? ???????? ?????? ???????, ?????????? ?????? ???? ???? ???????? ? ??, ??????? ??? ???????????? ???????? ???????? ???????? ?????????? ????????? ????????????, ? ????? ?????????????????? ???????? ??????????. ??-??????, ? ????? ??????? ?????????? ?????? ????????? ????? ?????????? ???? ???????? ? ?? ??????????. ??? ???????? ??????????, ?? ???????? ?? ????? ????? ???? ???.

?????? ?? ?????????? ????? ???????? ? ??????? ????? ?????????? ?? ??????? ???????, ????????, ??? ??? ??????? ? newrelic.

?????? pg_stat_statements ???????? ? PostgreSQL ??? ?????????? ?????, ?? ?????? ? 9.2 ?? ???????? ??????????????? ???????, ????????? ???????, ??????? ?????????? ?????? ???????????, ? ????.

????? ??????????????? ???? ???????, ?????????? ???????? ????????? ??????? ? postgresql.conf.

shared_preload_libraries = 'pg_stat_statements'         # (change requires restart)

????? ???? ?????????? ????????????? ?????? ??. ????? ????? ? ??, ????????? ????????? ???????:

CREATE EXTENSION pg_stat_statements

????? ????? ? ??, ??? ?? ????????? ??? ???????, ???????? ????????????? (view) pg_stat_statements.

$ psql dbname
dbname=# \x
??????????? ????? ???????.

doman=# select * from pg_stat_statements;

userid              | 10
dbid                | 16388
query               | SELECT  "words".* FROM "words"  WHERE "words"."id" = ? LIMIT ?
calls               | 27
total_time          | 0.277
rows                | 27
shared_blks_hit     | 76
shared_blks_read    | 6
shared_blks_dirtied | 0
shared_blks_written | 0
local_blks_hit      | 0
local_blks_read     | 0
local_blks_dirtied  | 0
local_blks_written  | 0
temp_blks_read      | 0
temp_blks_written   | 0
blk_read_time       | 0.051
blk_write_time      | 0

??? ????, ????? ???????????? ????????? ??? ???????, ?????????? ???????? trackiotiming, ??? ???? ???? ???????? ? postgresql.conf ????????? ???????.

track_io_timing = on

??????? ???????????? ????????? ?? ????? ????? ???????. userid ? ??? id ????????????, ??????? ???????? ??????, dbid ? id ???? ??????, ? ??????? ?????????? ???? ??????. ?????? ??? ?????, ???????? select oid, * from pg_database. ????? ??????? ??????????????? ?????? (query), ?????????? ??????? (calls), ????? ????? ?????????? ???? ??????? (total_time).

??? ??? ????? ???? ?????? ? ?? pgBadger, ? ??? ?????? ?????????? ?????????:

    rows ? ????????? ?????????? ???????????? ?????;
    shared_blks_hit ? ?????????? ???????, ??????? ???? ? ???? ??;
    shared_blks_read ? ?????????? ???????, ??????? ???? ????????? ? ?????, ????? ????????? ??????? ?????? ????;
    shared_blks_dirtied ? ?????????? ???????, ??????? ???? ????????;
    shared_blks_written ? ?????????? ???????, ??????? ???? ???????? ?? ????;
    local_blks_hit, local_blks_read, local_blks_dirtied, local_blks_written ? ?? ?? ?????, ??? ?????????? 4, ?????? ??? ????????? ?????? ? ????????;
    temp_blks_read ? ??????? ??????? ????????? ?????? ???? ?????????;
    temp_blks_written ? ??????? ??????? ????????? ?????? ???? ???????? (???????????? ??? ?????????? ?? ?????, ??????? ? ?????? ????????? ?????????);
    blk_read_time ? ??????? ??????? ???????? ?????? ?????? ? ?????;
    blk_write_time ? ??????? ??????? ???????? ?????? ?????? ?? ????.

???????????? ????? ??????????? ? ????? ????? ????????????? ???????, ????? ??????????? ????????? ?????????????????? ????? ??.

???????, ????? ??????? ????????? ?? ?????????, pg_stat_statements ??????? ?????????????? ???????? ?? ??. ???????? ?????? ???? ???????? ???? ? ????? ???? ???????? ??????.
