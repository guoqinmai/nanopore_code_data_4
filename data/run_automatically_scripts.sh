#!/bin/sh
SCRIPTS=(
    "1_zhikong.sh"
    "2_suzhu.sh"
    "3_yasuo.sh"
    "4_jieya.sh"
    "5_fasta.sh"
    "6_blastn.sh"
    "8_blastn_amr.sh"
    "7_bingyuanjun_tongji.py"
    "9_bingyuanjun_tongji.py"    
)

echo "======脚本开始执行======="
echo "开始时间：$(date)"

for SCRIPT in "${SCRIPTS[@]}"; do
    echo "准备执行：$SCRIPT"
    echo "开始执行：$SCRIPT(时间:$(date))"


    # 根据扩展名选择解释器
    if [[ "$SCRIPT" == *.py ]]; then
        interprete="python3"  # 执行Python脚本
    else
       interprerte="bash"     # 执行Shell脚本
    fi

    start_time=$(date +%s)
    if $interprete "$SCRIPT"; then
        end_time=$(date +%s)
        duration=$((end_time - start_time))
        echo "执行成功：SCRIPT (耗时：${duration}s)"
    else
        exit_status=$?
        end_time=$(date +%s)
        duration=$((end_time - start_time))
        echo "错误：$SCRIPT 执行失败"
        exit $exit_status
    fi
done

echo "======所有脚本执行完成======"
