DATE=`date +"%Y-%m-%d"`
#HOUR_RUN_ETF=14
HOUR_RUN_ETF=06
MINUTE_RUN_ETF=00
HOUR_RUN_OIL=06
MINUTE_RUN_OIL=01
HOUR_COMMIT=08
MINUTE_COMMIT=30
#echo $DATE

while [ 1 ]
do
    HOUR=`date +"%H"`
    MINUTE=`date +"%M"`
    DAY_OF_WEEK=`date +"%u"`
    echo "HOUR is $HOUR"
    echo "MINUTE is $MINUTE"
    #echo "Now time is $HOUR:$MINUTE $DAY_OF_WEEK"
    #echo "Alert time is $HOUR_RUN:$MINUTE_RUN "

    #if [ "$DAY_OF_WEEK" == "1" ] || [ "$DAY_OF_WEEK" == "2" ] || [ "$DAY_OF_WEEK" == "3" ] || [ "$DAY_OF_WEEK" == "4" ] || [ "$DAY_OF_WEEK" == "5" ] ; then
        if [ "$HOUR" == "$HOUR_RUN_ETF" ] && [ "$MINUTE" == "$MINUTE_RUN_ETF" ]; then
            etf_value=`python get_etf.py`
            echo $etf_value
            #for golden
            etf_golden_value=`python get_etf_golden.py`
            echo $etf_golden_value
        fi
        if [ "$HOUR" == "$HOUR_RUN_OIL" ] && [ "$MINUTE" == "$MINUTE_RUN_OIL" ]; then
            oil_value=`python get_oil.py`
            echo $oil_value
            sed '2i '"${etf_value}  ${oil_value}" -i data.txt
            #for golden
            sed '2i '"${etf_golden_value}" -i data_golden.txt
            commit_log="Update golden information - 日期 淨值 市值: ${etf_golden_value} "
            git commit data_golden.txt -m "${commit_log}"
        fi
        if [ "$HOUR" == "$HOUR_COMMIT" ] && [ "$MINUTE" == "$MINUTE_COMMIT" ]; then
            echo "Run git commit and git push"
            commit_log="Update oil information - 日期 淨值 市值 原油價格: ${etf_value} ${oil_value}"
            git commit data.txt -m "${commit_log}"
            git push
        fi
    #fi
    sleep 60
done
