#!/bin/bash


echo "На вход принимает PID Java процесса."
echo "В лог выводит RAM память и Heap память."
echo "Пример запуска heap_mem.sh <pid>"

[ "${#@}" = "0" ] && { echo "Не указн PID JAVA процесса"; exit 0; }

file="/tmp/heap.log"
JMAP="/opt/jdk8/bin/jmap"

rm -f ${file}

echo "jmap -heap" >> ${file}

while true
    do
        cat >> ${file} << EOF



>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
EOF
	date >> ${file}
	free -m >> ${file}
	echo ""
	$JMAP -heap "$1" >> ${file}
	sleep 10
    done
