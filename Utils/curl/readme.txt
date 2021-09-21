Регистрация сервера организации (СО) на центральном сервере (ЦС):
CERTIFICATE_PATH=/etc/app-server-certificates/identity.cer
HOSTNAME=
SERVER_IP_ADDRESS=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
CENTRAL_SERVER=
UPDATE= # update or ""
       curl \
           -F "uuid=$GEN_UUID" \
           -F "file=@$CERTIFICATE_PATH" \
           -F "ip=$SERVER_IP_ADDRESS" \
           -F "description=$HOSTNAME" \
           -F "active=on" \
           --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/msa-configuration/$UPDATE 

Отправка АК СО на ЦС:
CENTRAL_SERVER=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
        curl -H 'Content-type: application/xml' -d @addres.xml --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/akws/send   
При этом addres.xml должен находиться в месте запуска скрипта.

Для того чтобы использовать прокси при работе с curl, требуется в команде указать --proxy <SERVER_IP>. Т.е. команда может выглядить примерно так:
CENTRAL_SERVER=
CENTRAL_SERVER_USER=
CENTRAL_SERVER_USER_PWD=
        curl --proxy 127.0.0.1:8090 -H 'Content-type: application/xml' -d @addres.xml --user $CENTRAL_SERVER_USER:$CENTRAL_SERVER_USER_PWD http://$CENTRAL_SERVER:8081/akws/send  