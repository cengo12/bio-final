from Bio import Entrez, SeqIO

Entrez.email = "cengizhantoksari@gmail.com"
Entrez.api_key = "d71fafa6c25daefb5a00cde8a13d3878fc09"


def from_ncbi(ncbiId):
    handle = Entrez.efetch(db="nucleotide", id=ncbiId, rettype="fasta")
    for record in SeqIO.parse(handle, "fasta"):
        return str(record.seq)


def parse_fasta(fasta):
    first_line = fasta.find('\n')
    mystr = fasta[first_line:]
    return mystr.replace('\n', '')


primer_sequences = {}
genesequence = ""
def get_primer_sequences(gene_sequence):
    # Initialize empty dictionary to store primer sequences
    global primer_sequences
    primer_sequences = {}
    global genesequence
    genesequence = gene_sequence

    # Loop through each starting position in the gene sequence
    for i in range(len(gene_sequence)):
        # Loop through each ending position for the primer sequence
        for j in range(i + 18, i + 31):
            # Get the current primer sequence
            primer_seq = gene_sequence[i:j]

            if check_conditions(primer_seq) == False:
                continue

            # If all criteria are met, add the primer sequence to the dictionary
            primer_sequences[i]= primer_seq


    # Return the dictionary of primer sequences
    return primer_sequences


def melting_temperature(primer_seq):
    # Calculate the melting temperature of the primer sequence
    w = primer_seq.count('A')
    x = primer_seq.count('T')
    y = primer_seq.count('G')
    z = primer_seq.count('C')
    tm = 64.9 + 41 * (y + z - 16.4) / (w + x + y + z)
    return tm


def complement(seq):
    seq = seq.translate(str.maketrans("ATGC", "TACG"))
    return seq

def endprimers(location, startprimer):
    endprimerdict = {}
    gene_sequence = complement(genesequence)

    # Loop through each starting position in the gene sequence
    for i in range(location, len(gene_sequence)):
        # Loop through each ending position for the primer sequence
        for j in range(i + 18, i + 31):
            print(i,j)
            # Get the current primer sequence
            primer_seq = gene_sequence[i:j]

            # Check end primers in complementary DNA sequence
            if not check_conditions(primer_seq):
                continue

            # Check if tm is within 5 celcius.
            if abs(melting_temperature(primer_seq) - melting_temperature(startprimer)) > 5:
                continue

            # Check inter-primer homology
            if complement(startprimer) == primer_seq:
                continue

            # If all criteria are met, add the primer sequence to the dictionary
            endprimerdict[i] = primer_seq

    # Return the dictionary of end primer sequences
    return endprimerdict


def check_conditions(primer_seq):
    # Calculate the GC content of the primer sequence
    gc_content = (primer_seq.count('G') + primer_seq.count('C')) / len(primer_seq)
    # Check if the GC content is within the desired range
    if gc_content < 0.4 or gc_content > 0.6:
        return False

    # Check if the primer sequence ends in G or C
    if primer_seq[-1] != 'G' and primer_seq[-1] != 'C':
        return False

    tm = melting_temperature(primer_seq)
    # Check if the melting temperature is within the desired range
    if tm < 55 or tm > 65:
        return False

    # Check if there are any runs of 4 or more of one base
    runs_of_4 = False
    for base in ['A', 'T', 'G', 'C']:
        if base * 4 in primer_seq:
            runs_of_4 = True
            break
    if runs_of_4:
        return False

    # Check if there are any dinucleotide repeats
    dinuc_repeats = False
    for k in range(len(primer_seq)):
        if primer_seq[k:k + 2] * 4 in primer_seq:
            dinuc_repeats = True
            break
    if dinuc_repeats:
        return False

    # Check if there is any intra-primer homology
    intra_homology = False
    for l in range(len(primer_seq) - 4):
        for m in range(l + 3, len(primer_seq)):
            if complement(primer_seq[l:m]) in primer_seq:
                intra_homology = True
                break
    if intra_homology:
        return False

    return True