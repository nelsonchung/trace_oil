while [ 1 ]
do
    DATE=`date +"%Y-%m-%d"`
    echo $DATE
    oil_value=`python hour_get_oil.py`
    echo $oil_value
    sleep 300
done
