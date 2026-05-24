print("   Крестики-нолик")
print("1 игорк-Х, 2 игок-О")

print(f"    1   |    2   |    3   ")
print("---------------------------")
print(f"    4   |    5   |    6   ")
print("---------------------------")
print(f"    7   |    8   |    9   ")
hod=0
player1=input("Имя 1-го игрока: ")
player2=input("Имя 2-го игрока: ")
odin=0
dva=0
tri=0
ch=0
pt=0
st=0
sm=0
vm=0
dv=0
c1=" "
c2=" "
c3=" "
c4=" "
c5=" "
c6=" "
c7=" "
c8=" "
c9=" "
def check_win():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9
    if(c1==c2==c3!=" "):return True
    if(c4==c5==c6!=" "):return True
    if(c7==c8==c9!=" "):return True
    if(c1==c5==c9!=" "):return True
    if(c3==c5==c7!=" "):return True
    if(c1==c4==c7!=" "):return True
    if(c2==c5==c8!=" "):return True
    if(c3==c6==c9!=" "):return True
    return False
def draw_table():
    print(f"  {c1}  |  {c2}  |  {c3}  ")
    print("-----+-----+-----")
    print(f"  {c4}  |  {c5}  |  {c6}  ")
    print("-----+-----+-----")
    print(f"  {c7}  |  {c8}  |  {c9}  ")
try:
    while hod!=9:
        if hod%2==0:
            try:
                choice=int(input(f"{player1}: "))
            except ValueError:
                print("Цифры, дебил!")
                continue
            if choice<1 or choice>9:
                print("Вводить цифры от 1 до 9, дебил")
                continue
            
            elif choice==1:
                if odin!=1:
                    c1="X"
                    odin+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==2:
                if dva!=1:
                    c2="X"
                    dva+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==3:
                if tri!=1:
                    c3="X"
                    tri+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==4:
                if ch!=1:
                    c4="X"
                    ch+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==5:
                if pt!=1:
                    c5="X"
                    pt+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue

            elif choice==6:
                if st!=1:
                    c6="X"
                    st+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==7:
                if sm!=1:
                    c7="X"
                    sm+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==8:
                if vm!=1:
                    c8="X"
                    vm+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            elif choice==9:
                if dv!=1:
                    c9="X"
                    dv+=1
                else:
                    print(f"{player1}, эта клетка занятя, выберите другую")
                    continue
            draw_table()  
            if check_win():
                print(f"Победил {player1}")
                break
            hod+=1  
            
        else:
            try:
                choice=int(input(f"{player1}: "))
            except ValueError:
                print("Цифры, дебил!")
                continue
            if choice<1 or choice>9:
                print("Вводить цифры от 1 до 9, дебил")
                continue
            
            elif choice==1:
                if odin!=1:
                    c1="O"
                    odin+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue

            elif choice==2:
                if dva!=1:
                    c2="O"
                    dva+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==3:
                if tri!=1:

                    c3="O"
                    tri+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==4:
                if ch!=1:
                    c4="O"
                    ch+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==5:
                if pt!=1:
                    c5="O"
                    pt+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue

            elif choice==6:
                if st!=1:
                    c6="O"
                    st+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==7:
                if sm!=1:
                    c7="O"
                    sm+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==8:
                if vm!=1:
                    c8="O"
                    vm+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            elif choice==9:
                if dv!=1:
                    c9="O"
                    dv+=1
                else:
                    print(f"{player2}, эта клетка занятя, выберите другую")
                    continue
            draw_table()
            if check_win():
                print(f"Победил {player2}")
                break
            
            hod+=1
        
except KeyboardInterrupt:
    print("\nЗавершение.")
