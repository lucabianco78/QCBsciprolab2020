import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Bio import SeqIO


def computeStats(filename, show_output = True):
    sInfo = pd.read_csv(filename, sep="\t", header = 0)
    if show_output:
        print("The file contains {} entries".format(sInfo.shape[0]))
        scaffolds = sInfo["ScaffID"].unique()
        print("... {} scaffolds".format(scaffolds.shape[0]))
        contigs = sInfo[sInfo["type"] == "W"]
        c_sizes = contigs["c_end"].astype(int) - contigs["c_start"].astype(int)
        print("... {} contigs (tot. size: {:,} bases)".format(contigs.shape[0], 
                                                        np.sum(c_sizes)))
        gaps = sInfo[sInfo["type"] == "N"]
        print("... and {} gaps (tot. size: {:,} bases)".format(gaps.shape[0], 
                                                        np.sum(gaps["contig"].astype(int))))

        cont_by_scaff = contigs.groupby("ScaffID").aggregate(pd.DataFrame.count)['contig']
        #print(cont_by_scaff)
        cont_by_scaff.plot(kind = 'box')
        plt.ylabel("# contigs per scaffold")
        plt.show()
    return sInfo

def printSequence(scaffInfo, scafID, sequenceFile):
        
        scaff = scaffInfo[scaffInfo["ScaffID"] == scafID]
        hdr = ">" + scafID
        seq = ""
        if len(scaff) > 0:
            seqDict = SeqIO.to_dict(SeqIO.parse(sequenceFile, "fasta"))
            
            for entry in range(len(scaff)):
                entry_data = scaff.iloc[entry]
                if entry_data["type"] == "N":
                    seq += "N" * int(entry_data["contig"])
                elif entry_data["type"] == "W":
                    ctg = entry_data["contig"]
                    if not ctg in seqDict:
                        print("Warning: contig {} not present. Exiting...".format(ctg))
                        break
                    else:
                        c_s = int(entry_data["c_start"])
                        c_e = int(entry_data["c_end"])
                        c_strand = entry_data["c_strand"]
                        t_s = seqDict[ctg][c_s -1: c_e ]
                        if c_strand == "-":
                            t_s = t_s.reverse_complement()
                        seq += t_s.seq
        if len(seq) > 0:
            print(hdr)
            print(seq)
        else:
            print("Warning: scaffold {} not present".format(scafID))

if __name__ == "__main__":


    fn = "data_reduced.agp"

    scaffDF = computeStats(fn)
    scaffDF = computeStats("small.agp", show_output = False)
    printSequence(scaffDF,"my_scaff","small_seq.fasta")
    print("")
    printSequence(scaffDF,"my_scaff2","small_seq.fasta")
    print("")
    printSequence(scaffDF,"my_other_scaff","small_seq.fasta")
    print("")
    printSequence(scaffDF,"scaffold3","small_seq.fasta")
