def triangular(low):
    # altura do trian... 
    for i in range(0 ,low + low):
        # fazer forma do triangulo 
        if  i % 2 != 0:
          if i == 1 or i == low + low -1:
            #  fazer print em toda linha Ex 'x'*3 or xxx
            t = i  * 'x'
          else:
            # coloca espaço dentro triangulo
            t = 'x'+' '* (i-2) + 'x'
          # centraliza x 
          print(t.center(low + low))
        
def Quadrado(width, height):
    for h in range(height):
        print(width * ' O')

def Quadrado_vaz(width, height):
  sp = (width - 4) 
  for h in range(height + 1):
    if h == 0 or h == height:
       print(width * 'o')
    else:
       if width >= 4:
          print('o',''*sp,'o')
       else:
         if width == 3:
            print('o o')
         else: 
            print('o'*width)
    
t = triangular(9)

q = Quadrado_vaz(3, 4)
