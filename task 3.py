def costSlab1(m):
  for i in range(len(m)):
     print(m[i]*10,end='\t')

def costSlab2(m):
  for i in range(len(m)):
     print(m[i]*15,end='\t')

def costSlab3(m):
  for i in range(len(m)):
     print(m[i]*20,end='\t')
def main():
  u = [[55,65,75],[120,150,170],[210,230,240]]
  inp = int(input('Enter Your choice\nPress 1 to display the bill of slab 1 and slab 2.\nPress 2 to display the bill  of slab 3.\nPress any other key to exit. '))
  if inp == 1:
      print('Bill for slab 1:')
      costSlab1(u[0])
      print()
      print('Bill for slab 2:')
      costSlab2(u[1])
  elif inp == 2:
    print('Bill for slab 3:')
    costSlab3(u[2])
main()