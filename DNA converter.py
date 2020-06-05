import importlib

def translate()
     with open("DNA.txt", "r") as f: 
		DNAinput = f.read() 
     DNAinput = DNAinput.replace("\n", "") 
     DNAinput = DNAinput.replace("\r", "") 
     if len(DNAinput)%3 == 0:
          table = ['ATA:I', 'ATC:I', 'ATT:I', 'ATG:M', 
		   'ACA:T', 'ACC:T', 'ACG:T', 'ACT:T', 
		   'AAC:N', 'AAT:N', 'AAA:K', 'AAG:K', 
		   'AGC:S', 'AGT:S', 'AGA:R', 'AGG:R',				 
		   'CTA:L', 'CTC:L', 'CTG:L', 'CTT:L', 
	           'CCA:P', 'CCC:P', 'CCG:P', 'CCT:P', 
	           'CAC:H', 'CAT:H', 'CAA:Q', 'CAG:Q', 
		   'CGA:R', 'CGC:R', 'CGG:R', 'CGT:R', 
		   'GTA:V', 'GTC:V', 'GTG:V', 'GTT:V', 
		   'GCA:A', 'GCC:A', 'GCG:A', 'GCT:A', 
		   'GAC:D', 'GAT:D', 'GAA:E', 'GAG:E', 
		   'GGA:G', 'GGC:G', 'GGG:G', 'GGT:G', 
		   'TCA:S', 'TCC:S', 'TCG:S', 'TCT:S', 
		   'TTC:F', 'TTT:F', 'TTA:L', 'TTG:L', 
		   'TAC:Y', 'TAT:Y', 'TAA:_', 'TAG:_', 
		   'TGC:C', 'TGT:C', 'TGA:_', 'TGG:W', ]
         protein=""
         for i in range(0,len(DNAinput),3):
             for key in range(len(table)):
                 if DNAinput[i:3]== table[key][:3]:
                     if len(protein)>5:
                         protein=protein+'X'
                     else:
			 protein=protein + table[key][len(table[key])-1
	 print (protein)
		        
     else:
         print ("DNA strand is incorrect")

def mutate(): 
	with open("DNA.txt", "r") as DNA: 
		seq = DNA.read() 
	 seq = seq.replace("\n", "") 
	 seq = seq.replace("\r", "")
     for i in range(len(seq)):
        if seq[i]=="a":
            seq=seq.replace("a","A")
     f = open("normalDNA.txt", "a")
     f.write(seq)
     print("Normal DNA:"+seq) 
     for i in range(len(seq)):
         if seq[i]=="A":
             seq=seq.replace("A","T")
     f = open("mutatedDNA.txt", "a")
     f.write(seq)

mutate() 
translate() 



