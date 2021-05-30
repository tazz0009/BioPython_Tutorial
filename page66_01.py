from Bio.Data import CodonTable
from Bio.Seq import Seq

# 4.4.8 코돈 테이블
codon_table = CodonTable.unambiguous_dna_by_name["Standard"]
print(codon_table)

print("----------")


# 미토콘드리아 코돈 테이블
codon_table2 = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]
print(codon_table2)

print("----------")

# 4.4.9orf_finder

tatabox_seq = Seq("tataaaggcAATATGCAGTAG")
start_idx = tatabox_seq.find("ATG")
end_idx = tatabox_seq.find("TAG", start_idx)
orf = tatabox_seq[start_idx:end_idx+3]
print(orf)

print("----------")
