from tkinter import *
from CurrencyApi import currencies,rateof

master = Tk()

master.title("Currency Converter")

master.geometry("715x250")

Label(master,text="Enter amount").grid(row=0)
e1 = Entry(master)
e1.grid(row=0, column=1)



# Set the Menu initially
menu= StringVar()
menu.set("Select Any Currency")

# currency = currencies()


curr_with_name = []
fullname = currencies()
for i,v in fullname.items():
	curr_with_name.append(i+" - "+v)
# print(curr_with_name)



#Create a dropdown Menu
drop= OptionMenu(master, menu,*curr_with_name)
drop.grid(row=0,column=2)



def proccess_conversion():
	# print(menu.get(),e1.get())
	# print(rateof('EUR'))
	amnt = int(e1.get())
	curr = menu.get()
	rates = rateof(curr)
	# print(type(amnt),type(amnt/rates['ind_rate']))
	converted_amnt = round((amnt/rates['ind_rate'])*rates['req_rate'],2)
	# print(converted_amnt)
	ourMessage = f"{amnt} INR is {converted_amnt} {curr}"
	messageVar = Message(master, text = ourMessage)
	messageVar.config(bg='lightgreen')
	messageVar.grid( )

# submit buton
# Create a Button
btn = Button(master, text = 'Submit', bd = '5', command = proccess_conversion)
btn.grid(row=0,column=4)

# Label(master, text= "Select any One Currency!", font= ("", 10)).grid(row=0,pady=30)

# #Access the Menu Widget using StringVar function
# clicked= StringVar()
# #Create an instance of Menu in the frame
# main_menu = OptionMenu(master, clicked, "C++", "Java", "Python", "Rust","Go","Ruby")
# main_menu.grid()

master.mainloop()