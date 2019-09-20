#!/bin/bash
#################################

echo "检查CarClassifyService是否启动"
for i in {1..3}
    do
	USER_CHECK=`ps aux | grep CarClassifyService | grep python`
	    if [ -n "$USER_CHECK" ] ;then
            echo "CarClassifyService已经启动"
            break
        else
            echo "尝试第 $i 启动CarClassifyService"
			cd /data/appRun/CarClassifyService/code
            nohup ./start.sh > /data/appRun/CarClassifyService/code/nohup.out &
            echo "sleep 15s"
            sleep 15s
        fi
    done

echo "sleep 5s"
sleep 5s