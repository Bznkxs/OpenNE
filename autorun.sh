cd exps/src || echo "cd fails"
python3 logs_to_md.py $1 || echo "logs combination fails"
python3 process.py minimal || echo "logs processing fails"
cd ../..
python3 ss_exp_split.py || echo "split fails"
cd src || echo "cd fails"
nohup sh autogen_script_0.sh --devices 5 >a0.out &
nohup sh autogen_script_1.sh --devices 6 >a1.out &
nohup sh autogen_script_2.sh --devices 7 >a2.out &
echo "automatic execution"
