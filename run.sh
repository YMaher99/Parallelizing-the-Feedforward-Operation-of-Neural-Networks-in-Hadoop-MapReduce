#!/bin/bash
rm -rf ./output/
rm -rf ./res
cp -r res-orig res


for (( i = 1 ; i <= $1; i++))
do
	echo "running pre mapper for layer $i"
    run_activation=$(python ./src/pre_mapper.py)
	echo "run act $run_activation"
	echo "running layer $i"
	$HADOOP_HOME/bin/hadoop jar \
	$HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar\
	-files ./res/cache.txt,./res/network_info.txt,./res/w$i.txt,./src/mapper.py,./src/reducer.py\
	-mapper ./mapper.py \
	-reducer "./reducer.py  $run_activation" \
	-input ./res/input.txt \
	-output ./output/layer$i

	rm ./res/temp.txt
	$HADOOP_HOME/bin/hadoop fs -copyToLocal -p \
	./output/layer$i/part-00000 ./res/temp.txt

	if [ $i == $1 ]
	then
		break
	fi
	echo "running post reducer for layer $i"
    python3 ./src/post_reducer.py
done
	echo "running soft max layer"
	python3 ./src/softmax.py