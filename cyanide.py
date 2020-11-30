"""A hackable minesweeper game"""
#MineSweeper
from Tkinter import *
from tkMessageBox import *
from random import *
import math
frame = Tk()

Label(frame, text="Enter the grid size n:").grid(row=0,column=0)
e1=Entry(frame)
e1.grid(row=1,column=0)

#gives dictionary with position as key and how many adjacent mines at each position as value
def mine_number(mine_pos,m,size_of_grid):
    mine_number={}
    for p in m:
        neighbours=[]
        if p not in mine_pos:
            i=p[0]
            j=p[1]
            l1=[i]
            l2=[j]
            if i+1<=size_of_grid:
                l1.append(i+1)
            if i-1>0 :
                l1.append(i-1)
            if j+1<=size_of_grid :
                l2.append(j+1)
            if j-1>0 :
                l2.append(j-1)
            for ele in l1:
                for elem in l2:
                    if (l1.index(ele)==0 and l2.index(elem)== 0):
                        pass
                    else:
                        neighbours.append([ele,elem])
            mines=len(list(set(tuple(y) for y in neighbours)& set(tuple(k) for k in mine_pos)))
            mine_number[p]=mines
    return mine_number
#gives position of all mines in a list of tuples
def mine_positions(n,m):
    no_of_mines=math.floor((n**2)/4.0)
    print 'no_of_mines',no_of_mines
    pos=[]
    for i in range(0,int(no_of_mines)):
        while True:
            k=randint(0,len(m)-1)
            z=m[k]
            if z not in pos:
                pos.append(z)
                break
    return pos
#creating main grid
def fetch_grid_size():
    grid_size = e1.get()
    frame.destroy()
    root=Tk()
    size_of_grid=int(grid_size)
    x={}
    for i in range (1,size_of_grid+1):
        for j in range(1,size_of_grid+1):
            x[i,j]=Button(root,height=1,width=1)
            x[i,j].grid(row=i,column=j)
        (x.keys()).sort()

    mine_pos=mine_positions(size_of_grid,x.keys())
    #list of positions that have mines
    mines_at_pos=mine_number(mine_pos,x.keys(),size_of_grid)
    #dictionary with position as key and number of neighbour mines as value
    flag_pos=[]
    for i in mine_pos:
        mines_at_pos[tuple(i)]='*'
    
    def left_number(event):
        for each in x:
            if str(event.widget)==str(x[each]):
                c=each

        event.widget['text']=mines_at_pos[c]
        check()

    def left_mine(event):
        event.widget["text"] = "X"
        event.widget["bg"] = "red"
        event.widget['state']='disabled'
        event.widget.config(relief=SUNKEN)
        for all in mines_at_pos:
            if mines_at_pos[all]=='*':

                x[all]["text"] = "X"
                x[all]["state"] = "disabled"
            else:
                x[all]["text"]=mines_at_pos[all]
                x[all]["state"] = "disabled"
        showinfo('Lost','You Loser!')
        check()
    def right(event):
        event.widget['text']='|>'
        for h in x:
            if str(event.widget)==str(x[h]):
                flag_pos.append(h)
        check()
    def check():
        #if all open except for mines
        tex=[]
        for all in x:
            tex.append(x[all]['text'])
        if tex.count('')== math.floor((size_of_grid**2)/4.0) and len(flag_pos)==0 :
            showinfo('WIN','You Win!')

        #if flags in correct position
        mine_pos.sort()
        flag_pos.sort()
        count=0
        if mine_pos==flag_pos :
            for posi in mines_at_pos:
                if mines_at_pos[posi]!='*' :
                    if x[posi]['text']!='':
                        count+=1
            if count==(size_of_grid*size_of_grid)-math.floor((size_of_grid**2)/4.0):


                showinfo('WIN','You Win!')

    for b1 in mines_at_pos:
        f=b1[0]
        g=b1[1]
        if mines_at_pos[b1]=='*':

            x[(f,g)].bind("<Button-1>",left_mine)
            x[(f,g)].bind("<Button-3>",right)
        else:
            x[(f,g)].bind("<Button-1>",left_number)
            x[(f,g)].bind("<Button-3>",right)


Button(frame,text='ok',command=fetch_grid_size).grid(row=2,column=0,sticky=W,pady=4)
#main.minsize(height=600,width=400)


frame.mainloop()