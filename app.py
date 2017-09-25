from tkinter import *

root = Tk()


def insert_e1 (value) :
	e1.insert(END,value)
	
def equals() :
	try:
		a = e1.get()
		result =eval(a)
		e1.delete(0,END)
		e1.insert(END,result)
	except(ValueError, SyntaxError):
		e1.delete(0,END)
		e1.insert(END,'INVALID INPUT')
	except(ZeroDivisionError):
		e1.delete(0,END)
		e1.insert(END,'DIVIDED BY 0')
		
		
		
		
		
		
		
	
	
def delete_e1 () :
		e1.delete(0,END)
	

Label(root, text = 'CALCULATOR')

e1 = Entry(root,bd =4,width = 50)
e1.grid(row =0, columnspan =8)


Button(root, text = '0', width = 15,command = lambda: insert_e1(0)).grid(row = 1, column =0)
Button(root, text = '1',width = 15,command = lambda: insert_e1(1)).grid(row = 1, column =1)
Button(root, text = '2',width = 15,command = lambda: insert_e1(2)).grid(row = 1, column =2)
Button(root,text = '+',width = 15,command = lambda: insert_e1('+')).grid(row = 1, column = 3)
Button(root, text = '3',width = 15,command = lambda: insert_e1(3)).grid(row = 2, column =0)
Button(root, text = '4',width = 15,command = lambda: insert_e1(4)).grid(row = 2, column =1)
Button(root, text = '5',width = 15,command = lambda: insert_e1(5)).grid(row = 2, column =2)
Button(root,text =  '-',width =15,command = lambda: insert_e1('-')).grid(row =2, column =3)
Button(root, text = '6',width = 15,command = lambda: insert_e1(6)).grid(row = 3, column =0)
Button(root, text = '7',width = 15,command = lambda: insert_e1(7)).grid(row = 3, column =1)
Button(root, text = '8',width = 15,command = lambda: insert_e1(8)).grid(row = 3, column =2)
Button(root,text  =  'x', width = 15,command = lambda: insert_e1('*')).grid(row =3 ,column =3)
Button(root,text  =  '9', width = 15,command = lambda: insert_e1(9)).grid(row =4 ,column =0)
Button(root,text  =  '=', width = 15,command = lambda: equals()).grid(row =4,column =1)
Button(root,text  =  'C', width = 15,command = lambda: delete_e1()).grid(row =4 ,column =2)
Button(root,text  =  '%', width = 15,command = lambda: insert_e1('/')).grid(row =4,column =3)





root.mainloop()
 
