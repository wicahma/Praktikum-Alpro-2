hari=['Senin', 'Selasa', 'Rabu', 'Kamis', "Jum'at", 'Sabtu', 'Minggu']
keg={'Senin':[], 'Selasa':[], 'Rabu':[], 'Kamis':[], "Jum'at":[], 'Sabtu':[], 'Minggu':[]}
def input_act():
    for h in range(len(hari)):
        inp_yn=input('Apakah ada kegiatan di hari '+hari[h]+' y/n >>')
        if inp_yn=='y':
            inp_keg='y'
            while inp_keg != 'n': 
                inp_keg=input('Masukkan macam kegiatan hari '+hari[h]+' anda (n=berhenti)>> ')
                keg[hari[h]].append(inp_keg)
            keg[hari[h]].remove('n')
        else:
            pass
    print('==Daftar kegiatan dalam 1 minggu:')
    for har,ke in keg.items():
        print('- %s => '%(har),end='')
        if keg[har]==[]:
            print(' --- ')
        else:
            print(', '.join(ke))

input_act()

import random
skor=0
total=0
cr=int(input('Apakah siap? y=1/n=2'))
while total<33 and cr==1:
    rn=random.randint(0,10)
    total+=rn
    print('total: ',total)
    cr=int(input('Apakah siap? y=1/n=2'))
if total<24:
    print('game over')
    print('Point: 0')
elif total>33:
    print('game over')
    print('total anda lebih dari 33')
    print('Point: 0')
else:
    print('game over')
    score=10*(total-23)
    print('total anda lebih dari 33')
    print('point: ',score)