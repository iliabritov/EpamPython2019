""""
Задание 1

0) Повторение понятий из биологии (ДНК, РНК, нуклеотид, протеин, кодон)

1) Построение статистики по входящим в последовательность ДНК нуклеотидам 
для каждого гена (например: [A - 46, C - 66, G - 23, T - 34])

2) Перевод последовательности ДНК в РНК (окей, Гугл)

3) Перевод последовательности РНК в протеин*

Выход - 3 файла:
 - статистика по количеству нуклеотидов в ДНК
 - последовательность РНК для каждого гена
 - последовательность кодонов для каждого гена

"""
import matplotlib.pyplot as plt



def translate_from_dna_to_rna(dna):  
    return dna.replace('T', 'U')  


def count_nucleotides(*dna):
    num_of_nucleotides = {}
    for line in dna:
        for element in list(line.replace('\n','')):
            if element in num_of_nucleotides:
                num_of_nucleotides[element] += 1
            else:
                num_of_nucleotides[element] = 1     
    return num_of_nucleotides


def translate_rna_to_protein(rna, codons_table):
    rna = rna.replace('\n', '')
    if len(rna) % 3:
        rna = rna[:-(len(rna) % 3)]
    protein = ''
    for num in range(0, len(rna), 3):
        codon = rna[num: num + 3]
        protein += codons_table[codon]
    return protein + '\n'


""" read the file dna.fasta """
with open('.\\files\\dna.fasta', 'r') as file:
    dna_data = file.readlines()

dna_sequences = {}
for data_line in dna_data:
    if data_line.startswith('>'):
        dna_sequences[data_line] = []
        name = data_line
    else:
        dna_sequences[name].append(data_line)

""" count nucleotites + build histograms """
with open('.\\files\\result_dna_statistic.txt', 'w') as file:
    for name in dna_sequences:
        """ count DNA from and save data """
        file.write(name)
        curr_count = count_nucleotides(*dna_sequences[name])
        for elem in curr_count:
            file.write(elem + ' = ' + str(curr_count[elem]) + '\n')
            
        """ histograms """
        values = curr_count.values()
        y_pos = range(len(values))
        plt.bar(y_pos, values, align='center', alpha=0.4)
        plt.xticks(y_pos, curr_count)
        plt.ylabel('Quantity')
        plt.xlabel('Nucleotide')
        plt.title('DNA statistic. Object -' + str(name))
        plt.savefig('.\\files\\' + name[2:-1] + '.png')
        plt.close()

""" read codon's transfer table from file """
with open('.\\files\\rna_codon_table.txt', 'r') as file:
    codons_lines = file.readlines()

codons_data = {}
for line in codons_lines:
    data = line.split()
    codons = {i:j for i,j in zip(data[::2], data[1::2])}
    codons_data = {**codons_data, **codons}

""" transfer dna to rna + rna to protein """
with open('.\\files\\result_dna_to_rna.txt', 'w') as rna_file:
    with open('.\\files\\result_rna_to_protein.txt', 'w') as protein_file:
        for name in dna_sequences:
            rna_file.write(name)
            protein_file.write(name)
            for dna_line in dna_sequences[name]:
                """ transfer dna to rna and save data """
                rna_line = translate_from_dna_to_rna(dna_line)
                rna_file.write(rna_line)
                """ transfer rna to protein and save data """
                protein_line = translate_rna_to_protein(rna_line, codons_data)
                protein_file.write(protein_line)
