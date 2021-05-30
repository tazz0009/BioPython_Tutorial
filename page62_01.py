from Bio.Seq import Seq

# 4.4.4 Sequence 객체 전사, 번역하기

dna = Seq("ATGCAGTAG")
mrna = dna.transcribe()
ptn = dna.translate()

print(type(mrna))
print(mrna)
print(type(ptn))
print(ptn)
print("----------")

# 4.4.5 첫 번째 종결 코돈에서 번역 종료하기

mRNA = Seq("AUGAACUAAGUUUAGAAU")
ptn = mRNA.translate()
print(ptn)
print("----------")

ptnStopTrue = mRNA.translate(to_stop=True)
print(ptnStopTrue)

# 4.4.6 종결 코돈 기준으로 서열 나누기
for seq in ptn.split("*"):
    print(seq)

print("----------")

# 4.4.7 DNA Sequence 상보적, 역상보적 서열 만들기

seq = Seq("TATAAAGGCCAATATGCAGTAG")
comp_seq = seq.complement()
rev_comp_seq = seq.reverse_complement()

print(seq)
print(comp_seq)
print(rev_comp_seq)

print("----------")
