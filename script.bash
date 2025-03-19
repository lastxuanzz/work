#!/bin/bash

if [[ $(whoami) != "root" ]]; then
    echo "Please run with root privileges."
    exit 1
fi

export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080

input_file="filename.csv"
logfile="output_$(date +%Y%m%d%H%M%S).log"

if [ ! -f "$input_file" ]; then
    echo "Error: Input file $input_file does not exist." >&2
    exit 1
fi

while IFS=, read -r systemcode message webhook_url; do

    echo "##################${systemcode}##################" >> "$logfile"
    # 現在のタイムスタンプを書き込む
    timestamp=$(date "+%Y/%m/%d %H:%M:%S")
    echo "$timestamp" >> "$logfile"
    # コマンドを構築して記録する
    command="echo '{\"text\": \"TEST MESSAGE $message\"}' | curl -H 'Content-type: application/json' -d @- $webhook_url --insecure"
    echo "$command" >> "$logfile"
    $(eval $command) >> "$logfile"

    echo "" >> "$logfile"

    # ループごとに1秒待つ
    sleep 1
done < "$input_file"
