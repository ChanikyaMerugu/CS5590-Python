def katthi(list_of_dicts):
    for d in list_of_dicts:
        n1 = d.pop('L-GPA')
        n2 = d.pop('C-GPA')
        d['V+VI'] = (n1 + n2)/2
    return list_of_dicts
details= [
  { 'Subjct' : 'python', 'L-GPA' : 90, 'C-GPA' : 82},
   { 'Subjct' : 'web', 'L-GPA' : 70, 'C-GPA' : 82},
   { 'Subjct' : 'M-1', 'L-GPA' : 60, 'C-GPA' : 82}
]
print(katthi(details))
