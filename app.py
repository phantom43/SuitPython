from tkinter import *
import random
root = Tk()
root.title('panini')
pil = ('batu','gunting','kertas')

def logic(i):
	a = random.choice(pil)
	while i != i:
		a = random.choice(pil)
		break
	b = pil[i]
	pt1 = Label(root, text=f'AI : {a}')
	pt2 = Label(root, text=f'you : {b}')
	pt1.grid(row=2, column=4)
	pt2.grid(row=3, column=4)
	if b == 'kertas' and a == 'batu':
		pt3 = Label(root, text='You Win!!!')
		pt3.grid(row=6, column=4)
	elif b == 'gunting' and a == 'kertas':
		pt4 = Label(root, text='You Win!!!')
		pt4.grid(row=6, column=4)
	elif b == 'batu' and a == 'gunting':
		pt5 = Label(root, text='You Win!!!')
		pt5.grid(row=6, column=4)
	elif a == b:
		pt6 = Label(root, text='seri!!!')
		pt6.grid(row=6, column=4)
	else:
		pt7 = Label(root, text='You Lose!!!')
		pt7.grid(row=6, column=4)

pt = Label(root, text='You Vs AI\nCreate your decission')
p1 = Button(root, text='batu', command= lambda:logic(0))
p2 = Button(root, text='gunting', command=lambda:logic(1))
p3 = Button(root, text='kertas', command=lambda:logic(2))

pt.grid(row=1,column=4)
p1.grid(row=4,column=3)
p2.grid(row=4,column=4)
p3.grid(row=4,column=5)
root.mainloop()