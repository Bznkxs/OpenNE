cd exps/src || echo "cd fails"
python3 logs_to_md.py $1 || echo "logs combination fails"
python3 process.py gen minimal || echo "logs processing fails"
cd ../..
python3 ss_exp_split.py autogen_script 4 || echo "split fails"
echo "check out src"
