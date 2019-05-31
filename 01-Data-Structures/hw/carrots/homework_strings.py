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
    rna = dna.replace('T', 'U')  
    return rna

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
    protein = ''
    if len(rna) % 3 == 0:
        for num in range(0, len(rna), 3):
            codon = rna[num: num + 3]
            protein += codons_table[codon]
    return protein + '\n'

""" read the file dna.fasta """
dna = open('.\\files\\dna.fasta', 'r')
dna_data = dna.readlines()
dna.close()

""" data processing """
dna_sequences = {}
for data_line in dna_data:
    if data_line.startswith('>'):
        dna_sequences[data_line] = []
        name = data_line
    else:
        dna_sequences[name].append(data_line)

""" count nucleotites + build histograms """
dna_statistic = open('.\\files\\result_dna_statistic.txt', 'w')
for name in dna_sequences:
    """ count DNA from and save data """
    dna_statistic.write(name)
    curr_count = count_nucleotides(*dna_sequences[name])
    for elem in curr_count:
        dna_statistic.write(elem + ' = ' + str(curr_count[elem]) + '\n')
        
    """ histograms """
    values = curr_count.values()
    y_pos = range(len(values))
    #ax = plt.gca()
    plt.bar(y_pos, values, align='center', alpha=0.4)
    plt.xticks(y_pos, curr_count)
    plt.ylabel('Quantity')
    plt.title('DNA statistic. Object -' + str(name))
    plt.savefig('.\\files\\' + name[2:-2] + '.png')
    plt.close()
dna_statistic.close()


""" read codon's transfer table from file """
flag = 1
last_elem = ''
codons_data = {}
codons_obj = open('.\\files\\rna_codon_table.txt', 'r')
codons_lines = codons_obj.readlines()
for line in codons_lines:
    for element in line.split():
        if flag:
            codons_data[element] = None
            last_elem = element
            flag = 0
        else:
            codons_data[last_elem] = element
            flag = 1

""" transfer dna to rna + rna to protein """
dna_to_rna = open('.\\files\\result_dna_to_rna.txt', 'w')
rna_to_protein = open('.\\files\\result_rna_to_protein.txt', 'w')

for name in dna_sequences:
    dna_to_rna.write(name)
    rna_to_protein.write(name)
    for dna_line in dna_sequences[name]:
        """ transfer dna to rna and save data """
        rna_line = translate_from_dna_to_rna(dna_line)
        dna_to_rna.write(rna_line)
        """ transfer rna to protein and save data """
        protein_line = translate_rna_to_protein(rna_line, codons_data)
        rna_to_protein.write(protein_line)
                   
dna_to_rna.close()
rna_to_protein.close()
