JMETER_HOME=/root/loadtesting/jmeter-node-6
SCRIPT_FILE=$WORKSPACE/appointment/appointment.jmx
RESULT_FILE=$WORKSPACE/result.xml
SCRIPT_PARAMETERS="-Jthreads=$THREADS -JrampUpPeriod=$RAMPUPPERIOD -JworkCycles=$WORKCYCLES -JrepeatPerThread=$REPEATPERTHREAD -JrepeatPerThreadDuration=$REPEATPERTHREADDURATION -Jprotocol=$PROTOCOL -Jhost=$HOST -Jport=$PORT -Jusername=$USERNAME -Juserpassword=$USERPASSWORD -JcasUrlPrefix=$CASURLPREFIX -JcasHost=$CASHOST -JpatientId=$PATIENTID"
SCRIPT_PARAMETERS_FILE=$WORKSPACE/appointment/$PARAMETERS.txt

rm -f $RESULT_FILE
rm -f $WORKSPACE/*.png
sh $JMETER_HOME/bin/jmeter.sh -n $SCRIPT_PARAMETERS -q $SCRIPT_PARAMETERS_FILE -t $SCRIPT_FILE -l $RESULT_FILE

sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ThreadsStateOverTime.png --input-jtl $RESULT_FILE --plugin-type ThreadsStateOverTime --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/BytesThroughputOverTime.png --input-jtl $RESULT_FILE --plugin-type BytesThroughputOverTime --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/HitsPerSecond.png --input-jtl $RESULT_FILE --plugin-type HitsPerSecond --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/LatenciesOverTime.png --input-jtl $RESULT_FILE --plugin-type LatenciesOverTime --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ResponseCodesPerSecond.png --input-jtl $RESULT_FILE --plugin-type ResponseCodesPerSecond --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ResponseTimesDistribution.png --input-jtl $RESULT_FILE --plugin-type ResponseTimesDistribution --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ResponseTimesOverTime.png --input-jtl $RESULT_FILE --plugin-type ResponseTimesOverTime --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ResponseTimesPercentiles.png --input-jtl $RESULT_FILE --plugin-type ResponseTimesPercentiles --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/ThroughputVsThreads.png --input-jtl $RESULT_FILE --plugin-type ThroughputVsThreads --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/TimesVsThreads.png --input-jtl $RESULT_FILE --plugin-type TimesVsThreads  --width 1600 --height 900
sh $JMETER_HOME/lib/ext/JMeterPluginsCMD.sh --generate-png $WORKSPACE/TransactionsPerSecond.png --input-jtl $RESULT_FILE --plugin-type TransactionsPerSecond  --width 1600 --height 900





-verbose:gc -Xloggc:gc.log -XX:+PrintGCDetails -XX:+PrintGCTimeStamps -XX:+UseGCLogFileRotation -XX:NumberOfGCLogFiles=5 -XX:GCLogFileSize=1048576