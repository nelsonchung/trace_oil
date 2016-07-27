            etf_value=`python get_etf.py`
            echo $etf_value
            #for golden
            etf_golden_value=`python get_etf_golden.py`
            echo $etf_golden_value

            oil_value=`python get_oil.py`
            echo $oil_value
            sed '2i '"${etf_value}  ${oil_value}" -i data.txt
            #for golden
            sed '2i '"${etf_golden_value}" -i data_golden.txt
            commit_log="Update golden information - 日期 淨值 市值: ${etf_golden_value} "
            git commit data_golden.txt -m "${commit_log}"

            echo "Run git commit and git push"
            commit_log="Update oil information - 日期 淨值 市值 原油價格: ${etf_value} ${oil_value}"
            git commit data.txt -m "${commit_log}"
            git push
 
