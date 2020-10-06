from Bio import SeqIO

seqIterator = SeqIO.parse("../file_samples/filtered_contigs.fasta", "fasta")

sRcds = []
for s in seqIterator:
    transl = s.seq.translate()
    stop_cnt = transl.count("*")
    print(s.id,"\t", stop_cnt)
    s.seq = transl
    sRcds.append(s)

N = SeqIO.write(sRcds,"../file_samples/filtered_contigs_translated.fasta", "fasta")
print("")
print("{} sequences written to output file".format(N))