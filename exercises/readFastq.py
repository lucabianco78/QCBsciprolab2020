from Bio import SeqIO



def parseFasta(fn,fout):
    records = []
    for seq_record in SeqIO.parse(fn, "fastq"):
        s = seq_record[len(seq_record) - 100 : ]
        records.append(s)
        print(s.letter_annotations)

    #SeqIO.write(records,fout, "fastq")
        #print(seq_record.letter_annotations)
infile = "../file_samples/test_reads.fastq"
outfile = "../file_samples/test_reads.fastq"

parseFasta(infile, outfile)


