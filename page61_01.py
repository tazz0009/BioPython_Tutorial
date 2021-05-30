from Bio.Seq import Seq

# 4.4.3 Sequence 객체 서열 대소문자 변환하기

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
print(tatabox_seq.upper())
print(tatabox_seq.lower())
