Перечислены основные утилиты в части сети, ктороые могут понадобиться при работе.
	netstat -rn  аналог route
	netstat -at - все открытые порты TCP
	netstat -lt - по TCP прослушиваемые
	netstst -anp - самая используемая комбинация
	
	nmap -sT -O localhost - покажет порты что ждут соед. из вне
	lsof -i :<port> проц. работающий с портом
	ss -p;  ss -l
	ethtool eth0 - статистика

	host <name> - переводит в ip

	ifstat - общая статистика без ip
	iftop

time netstat -an|wc -l
time ss -ant|wc -l

Узнать mac
	ping <ip>
	arp -a

lsof -i:8081

Основные инструменты для мониторинга состояния Linux
atop, htop, iftop, iotop (и здесь же lsof)

Каждые 5с будет обновлять отображаемую информацию               
	iostat -d -t 5

Будет выводить в файл каждые 10с 60раз
	atop -w /tmp/atop.raw 10 60

Нужно разобраться что это (связано с  сеткой)
	echo 1 > /proc/sys/net/ipv4/tcp_tw_recycle

Дискрипторы
	Максимальное число дискрипторов открываемых файлов:
		cat /proc/sys/fs/file-max

	Для изменения "на лету"
		echo "104854" > /proc/sys/fs/file-max
	
	Отобразить текущее кол. открытых дискрипторов
	        cat /proc/sys/fs/file-nr
		lsof | wc -l

		lsof | grep <PID> отобразить кол. дискрипторов открытых конкретным приложением.
		ls -l /proc/<PID>/fd/


Мониторинг на базе FreeBSD
	https://habrahabr.ru/sandbox/31010/

Про настройки сети
	https://romantelychko.com/blog/1300/

Для мониторнга производительности на низком уровне для Linux
	bpf - perform a command on an extended BPF map or program