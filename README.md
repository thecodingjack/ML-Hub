bash create_model -i 1 -n test1 -t tips
bash train -i 1
bash test -i 1
bash predict -i 1 -s [0,1,3,1,0,0,0]