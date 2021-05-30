from Bio.Data import IUPACData
from Bio.Seq import Seq
from Bio.SeqUtils import GC, molecular_weight, six_frame_translations, seq1, seq3
from Bio.SeqUtils import MeltingTemp as mt

# 4.5.1 Bio.SeqUtils로 GC-contents(%) 게산하기

exon_seq = Seq("ATGCAGTAG")
gc_contents = GC(exon_seq)
print(gc_contents)

print("----------")

# 4.5.2 Bio.SeqUtils로 서열의 무게 계산하기

myseq = Seq("ATGCAGTAG")
# seq2 = Seq("ATGCAGTAG", IUPACData.unambiguous_dna_weights)
# seq3 = Seq("ATGCAGTAG", IUPACData.protein_weights)

print(molecular_weight(myseq))
print(molecular_weight(myseq, "DNA"))
print(molecular_weight(myseq, "protein"))

print("----------")

# 4.5.3 Bio.SeqUtils로 가능한 모든 번역 구하기

print(six_frame_translations(myseq))

print("----------")

# 4.5.4 Bio.SeqUtils로 DNA 서열 Tm 계산하기

myseq = Seq("AGTCTGGGACGGCGCGGCAATCGCA")
print(mt.Tm_Wallace(myseq))

print("----------")

# 4.5.6 Bio.SeqUtils로 아미노산 서열의 약자와 기호간 변환하기

essential_amino_acid_3 = "LeuLysMetValIleThrTrpPhe"
print(seq1(essential_amino_acid_3))


dna = Seq("ATGCAGTAG")
mrna = dna.transcribe()
ptn = dna.translate()
print(ptn)
print(seq3(ptn, custom_map={"*": "***"}))
