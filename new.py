## que no 1 

def abc(new_txt):
    new_word=[]
    opened=open(new_txt,'r')
    for line in opened:
        first_word=line.split()[0]
        new_word.append(first_word)
    opened.close()
    return new_word
print(abc('sample.txt'))

## que no 2

with open('a.txt','r') as f ,open('b.txt','w') as d:
    for line in f.readlines():
     d.writelines(line)


## que no 3
with open ('a.txt','r') as f:
    line_num=1
    for line in f.readlines():
        no_word=len(line.split())
        print(f'line {line_num} has {no_word}')
        line_num+=1


## que no 4 

with open('a.txt','r') as f:
    total_count=0
    for line in f.readlines():
        total_count+=1
    print(total_count)

## que no 5

with open('a.txt','r') as f ,open('b.txt','w') as d:
    for line in f.readlines():
        if 'python' in line:
            d.writelines(line)

## que no 6

with open ('a.txt','r') as f , open('b.txt','w') as d :
    for line in f.readlines():
        int_num=int(line)
        d.writelines(f'{str(int_num**2)}\n')

# que no 7

with open('a.txt','a') as f:
    user=input('Enter anythong you want to write: ')
    f.writelines(f"{user}\n")

## que no 8
with open ('a.txt','r') as f , open ('b.txt','w') as d:
    for line in f.readlines():
        d.writelines(line.upper())
