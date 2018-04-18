python Final_code.py
java -cp "/home/arpan/Mallet/class:/home/arpan/Mallet/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger --train true --test lab --threads 2 --iterations 100 --model-file nouncrf train_feature.txt
java -cp "/home/arpan/Mallet/class:/home/arpan/Mallet/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger  --threads 2 --iterations 100 --model-file nouncrf dev_feature.txt > dev_out.txt
java -cp "/home/arpan/Mallet/class:/home/arpan/Mallet/lib/mallet-deps.jar" cc.mallet.fst.SimpleTagger  --threads 2 --iterations 100 --model-file nouncrf test_feature.txt > test_out.txt
python Pred.py

