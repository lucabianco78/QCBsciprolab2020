from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

result_handle = NCBIWWW.qblast("blastn", "nr", "23307792",
                               entrez_query='"Homo Sapiens" [Organism]')



for res in NCBIXML.parse(result_handle):
    for d in res.descriptions:
        
        print("TITLE:{}\nSCORE:{}\nN.ALIGN:{}\nE-VAL:{}".format(
            d.title,d.score, d.num_alignments,d.e))
        
    for a in res.alignments:
        print("Align Title:{}\nAlign Len: {}".format(a.title, a.length))

        
    
        for h in a.hsps:
            s = h.score
            b = h.bits
            e = h.expect
            n = h.num_alignments
            i = h.identities
            p = h.positives
            g = h.gaps
            st = h.strand
            f = h.frame
            q = h.query
            sb = h.sbjct
            qs = h.query_start
            ss = h.sbjct_start
            qe = h.query_end
            se = h.sbjct_end
            m = h.match 
            al = h.align_length
            
            print("Score: {} Bits: {} E-val: {}".format(s,b,e))
            print("N.aligns: {} Idents: {} Positives: {} Gaps: {} Align len: {}".format(
                n,i,p,g,al))
            print("Strand: {} Frame: {}".format(st,f))
            print("Query:", q, " start:", qs, " end:", qe)
            print("Match:",m)
            print("Subjc:",sb, " start:", ss, " end:", se)
            

result_handle.close()