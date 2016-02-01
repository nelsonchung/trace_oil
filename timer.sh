DATE=`date +"%Y-%m-%d"`
HOUR_RUN_EFT=14
MINUTE_RUN_EFT=00
HOUR_RUN_OIL=09
MINUTE_RUN_OIL=00
#echo $DATE

while [ 1 ]
do
    HOUR=`date +"%H"`
    MINUTE=`date +"%M"`
    DAY_OF_WEEK=`date +"%u"`
    #echo "Now time is $HOUR:$MINUTE $DAY_OF_WEEK"
    #echo "Alert time is $HOUR_RUN:$MINUTE_RUN "

    #if [ "$DAY_OF_WEEK" == "1" ] || [ "$DAY_OF_WEEK" == "2" ] || [ "$DAY_OF_WEEK" == "3" ] || [ "$DAY_OF_WEEK" == "4" ] || [ "$DAY_OF_WEEK" == "5" ] ; then
        if [ "$HOUR" == "$HOUR_RUN_ETF" ] && [ "$MINUTE" == "$MINUTE_RUN_ETF" ]; then
            etf_value=`python get_etf.py`
        fi
        if [ "$HOUR" == "$HOUR_RUN_OIL" ] && [ "$MINUTE" == "$MINUTE_RUN_OIL" ]; then
            oil_value=`python get_oil.py`
            sed '2i '"${etf_value}  ${oil_value}" -i data.txt
        fi
    #fi
    sleep 60
done
