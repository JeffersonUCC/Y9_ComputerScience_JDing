#import packages
from tkinter import *
import random
import csv
import os
from pynput.keyboard import Key,Controller
import time
root = Tk()

#Colour Theme
Sunshine = '#ffd280'
Steel_Blue = '#426E86'
Bone = '#F8F1E5'
Honey = '#EB8A3E'

#RSA Encryption
cipher = []
n=7441826991206406709576923798652306546773056383923657355748125433921170166237822700978602733318243198872391448038717383645273135292865009135623454648457251152479774667822283716405812196213269778591708092613681639094858652600822484100505704226715130775144353675554189536174751655752733823725881192996003709612306625816000913962672752947794794592929812789552418862834752848089722689574309164356302742239632448304296692333917423975797637051507227100217475335583330661060121209180098107074150139550375959262626119833501770072868699207069770140058936323994415274097579352438105654231135473547937006233631692474761658579637
e=6553
d=4165515245497497300584183807943943295218002566188306909947218692449695127385981026581644258478760270633897731024876447918642127308748489777119919372888935941903832364042749377655504217260838325633203919381502251213175879404824793480948408836195803400462305704552535818508925541477342845326801803129763712323707922729320122183190848453201638965312192858220393090816213720436537019479473566613916791146451770874471143677665974186271603566727889259702727174612886772425044819676162383477897768349836907574509704980372425128806961289095835294370498521487628563707891665120639474055335033475762900708067357970775016255657
#Variable Declariation 
def random_password_generator_ico():
    random_password_generator_ico = """
    #############################################################
    #                  Random Password Generetor                #
    #                                                           #
    #             DEVELOPER :Jeofo                              #
    #          E-Mail Address : jefferson.ding@ucc.on.ca        #
    #               Teacher : Mr. Miskew                        #
    #                                                           #
    #############################################################
    """
    print(random_password_generator_ico)
keyboard=Controller()
autofillbuffer = ''
Letter = BooleanVar()
Numbers= BooleanVar()
Caps= BooleanVar()
Special_Characters= BooleanVar()
Easy_to_Read= BooleanVar()
Generate = StringVar()
Size = IntVar()
Username = StringVar()
Password = StringVar()
Memo = StringVar()
SUsername = StringVar()
SMemo = StringVar()
SPassword = StringVar()
PasswordO = StringVar()
word = []
chars = []
generate = []
special = ['!','@','#','$','%','&_','-','?','!','@','#','$','%','&_','-','?','!','@','#','$','%','&_','-','?']
ascii_uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ascii_lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

logonUsername = StringVar()
logonPassword = StringVar()
destination = StringVar()
personalvault = StringVar()
#Button Functions
def Search():
	try:
		root.clipboard_clear()
		User_Data = open(destination.get(), 'r+')
		User_Data_Reader = csv.DictReader(User_Data)
		for row in User_Data_Reader:
			if(row['Username']==SUsername.get()):
				SUsername.set(row['Username'])
				SMemo.set(row['Memo'])
				SPassword.set('Username: '+row['Username']+'\n'+'Memo: '+row['Memo']+'\n'+'Password: ')
				Decrypt_Display(row['Password'])
			if(row['Memo']==SMemo.get()):
				SUsername.set(row['Username'])
				SMemo.set(row['Memo'])
				SPassword.set('Username: '+row['Username']+'\n'+'Memo: '+row['Memo']+'\n'+'Password: ')
				Decrypt_Display(row['Password'])
		User_Data.close()
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def removeList(b):
	try:
		try:
			for i in b:
				chars.remove(i)
		except:
			print("None to remove")
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def appendLU():
	try:
		global chars
		if(Letter.get() == True):
			chars.extend(ascii_lowercase)
		else:
			removeList(ascii_lowercase)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def appendLL():
	try:
		global chars
		if(Caps.get() == True):
			chars.extend(ascii_uppercase)
		else:
			removeList(ascii_uppercase)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def appendN():
	try:
		global chars
		if(Numbers.get() == True):
			chars.extend(digits)
		else:
			removeList(digits)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def appendS():
	try:
		global chars
		if(Special_Characters.get() == True):
			chars.extend(special)
		else:
			removeList(special)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Create():
	try:
		global generate
		global chars
		global word
		generate = []
		if(Easy_to_Read.get()==False):
			removeList(word)
		elif(Easy_to_Read.get()==True):
			removeList(word)
			word = []
			for i in range(0,26):
				word.append(random.choice(open('English_noun.txt').readlines()).strip('\n'))
			chars.extend(word)
		if(Size.get()<20):
			for i in range(0,Size.get()):
				generate.append(random.choice(chars))
			Generate.set(''.join(generate))
		else:
			Generate.set("Thats tooo large :)")
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Fill():
	try:
		Password.set(Generate.get())
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Encrypt(a):
	try:
		encryptmp = []
		for x in a:
			encryptmp.append(str(pow(ord(x),e,n)))
		return '\t'.join(encryptmp)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Encrypt_Save():
	try:
		User_Data = open(destination.get(), 'a+')
		fieldnames = ['Username', 'Memo','Password']
		User_Data_Writer = csv.DictWriter(User_Data, fieldnames=fieldnames)
		if(Password.get()!= '' and Username.get()!='' and Memo.get()!= '' and Password.get()!= 'Saved' and Password.get()!= 'Please input'):
			plaintext=Password.get()
			for x in plaintext:
				cipher.append(str(pow(ord(x),e,n)))
			User_Data_Writer.writerow({'Username':Username.get(),'Memo':Memo.get(),'Password':str('\t'.join(cipher))})
			Password.set('Saved')
			Username.set('Saved')
			Memo.set('Saved')
		else:
			Password.set('Please input')
			Username.set('Please input')
			Memo.set('Please input')
		User_Data.close()
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Decrypt_Display(a):
	try:
		decryption=[]
		plaintextset=[]
		text = a.split('\t')
		for y in text:
			q = int(y)
			decryption.append(pow(q,d,n))
		for char in decryption:
			plaintextset.append(chr(char))
		plaintext=''.join(plaintextset)
		PasswordO.set(plaintext)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Decrypt(a):
	try:
		decryption=[]
		plaintextset=[]
		text = a.split('\t')
		for y in text:
			q = int(y)
			decryption.append(pow(q,d,n))
		for char in decryption:
			plaintextset.append(chr(char))
		return(''.join(plaintextset))
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Open_Vault():
	try:
		User_Data = open(destination.get(), 'r+')
		User_Data_Reader = csv.DictReader(User_Data)
		personalvault.set('Users/'+logonUsername.get()+'/'+logonUsername.get()+'_Vault.csv')
		Secret_Vault = open(personalvault.get(), 'a+') 
		Secret_Vault_Writer = csv.DictWriter(Secret_Vault, fieldnames=['Username','Memo','Password'])
		for row in User_Data_Reader:
			Secret_Vault_Writer.writerow({'Username':row['Username'],'Memo':row['Memo'],'Password':Decrypt(row['Password'])})
		Secret_Vault.close()
		os.system(f'open {personalvault.get()}')
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def AutoFill():
	try:
		root.clipboard_append(PasswordO.get())
		if(PasswordO.get()==''):
			q = SUsername.get()
			SUsername.set("No Data to AutoFill")
			time.sleep(1)
			SUsername.set(q)
		else:
			time.sleep(3)
			for a in PasswordO.get():
				keyboard.press(a)
				keyboard.release(a)
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Logon():
	try:
		directory = 'Users/'+logonUsername.get()
		if(os.path.isdir(directory)):
			destination.set(directory+'/'+logonUsername.get()+'_User.csv')
			Logon_Data = open('Logon_Data.csv','r+')
			logonfield = ['Username','Password']
			Logon_Data_Reader = csv.DictReader(Logon_Data)
			Logon_Data_Writer = csv.DictWriter(Logon_Data,fieldnames=['Username','Password'])
			for row in Logon_Data_Reader:
				if(logonUsername.get() == row['Username'] and logonPassword.get() == Decrypt(row['Password'])):
					Logonf.pack_forget()
					Mainf.grid(row = 0,column = 0,columnspan = 2)
					generatorf.grid(row =1 , column = 0 )
					vaultf.grid(row =1 , column = 1)
					managerf.grid(row = 2, column =0,columnspan = 2 )
		else:
			logonUsername.set('Please Register!!')
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
def Register():
	try:
		directory = 'Users/'+logonUsername.get()
		if(os.path.isdir(directory)):
			logonUsername.set('Please Logon')
		else:
			os.mkdir(directory)
			destination.set(directory+'/'+logonUsername.get()+'_User.csv')
			Logon_Data = open('Logon_Data.csv','a+')
			logonfield = ['Username','Password']
			Logon_Data_Writer = csv.DictWriter(Logon_Data, fieldnames=logonfield)
			Logon_Data_Writer.writerow({'Username':logonUsername.get(),'Password':Encrypt(logonPassword.get())})
			Logon_Data.close()
	
			User_Data = open(destination.get(), 'w+')
			fieldnames = ['Username', 'Memo','Password']
			User_Data_Writer = csv.DictWriter(User_Data, fieldnames=fieldnames)
			User_Data_Writer.writeheader()
	except:
		print("Sorry! An Error Occured\nError Code 0x1f4d44\nPlease contact DEVELOPER!")
		random_password_generator_ico()
#Frame Creation and Configure
generatorf = Frame(root)
generatorf.configure(background = Bone)
vaultf = Frame(root)
vaultf.configure(background =Bone)
managerf = Frame(root)
managerf.configure(background = Bone)
Mainf = Frame(root)
Logonf = Frame(root)
#Generator Frame Create and Configure
cb = []
EtGSize = Entry(generatorf,text="Size",textvariable = Size,background = 'white')
cb.append(Checkbutton(generatorf,text="Letters", variable=Letter,onvalue = True, offvalue = False, height = 2,width = 15,command = appendLU,background = Bone))
cb.append(Checkbutton(generatorf,text="Numbers", variable=Numbers,onvalue = True, offvalue = False, height = 2,width = 15,command = appendN,background = Bone))
cb.append(Checkbutton(generatorf,text="Caps", variable=Caps,onvalue = True, offvalue = False, height = 2,width = 15,command = appendLL,background = Bone))
cb.append(Checkbutton(generatorf,text="Special Characters", variable=Special_Characters,onvalue = True, offvalue = False, height = 2,width = 15,command = appendS,background = Bone))
cb.append(Checkbutton(generatorf,text="Easy to Read", variable=Easy_to_Read,onvalue = True, offvalue = False, height = 2,width = 15,background = Bone))
lbGSize = Label(generatorf,text = "Size",background = Bone)
lbGSize.grid(row =0,column = 1)
EtGSize.grid(row = 0,column = 0)
for x in range(0,5):
	cb[x].grid(row = x+1, column = 0)

#Logon Frame Create and Configure
lbLTitle = Label(Logonf,text = "RPG Logon")
lbLUser = Label(Logonf,text = 'Username')
lbLPass = Label(Logonf,text = 'Password')
EntLUser = Entry(Logonf,textvariable = logonUsername)
EntLPass = Entry(Logonf,textvariable = logonPassword)
BtnLGo = Button(Logonf,text = 'Logon',command = Logon)
BtnLRegister = Button(Logonf,text = 'Register',command = Register)
lbLTitle.grid(row = 0,column =0,columnspan = 2)
lbLUser.grid(row = 1,column =0 )
lbLPass.grid(row =2 ,column = 0)
EntLUser.grid(row =1 ,column = 1)
EntLPass.grid(row =2 ,column = 1)
BtnLGo.grid(row = 3,column =1) 
BtnLRegister.grid(row = 3,column =0) 


#Vault Frame Create and Configure
LbVPassword = Label(vaultf,text = "Password",background = Sunshine)
EtVPassword = Entry(vaultf,text = "Password ... ",textvariable = Password,background = 'white')
LbVUsername =Label(vaultf,text = "Username",background = Sunshine)
EtVUsername = Entry(vaultf,text = "Username ... ",textvariable = Username,background = 'white')
LbVMemo = Label(vaultf,text = "   Memo   ",background = Sunshine)
EtVMemo = Entry(vaultf,text = "Memo ...",textvariable = Memo,background = 'white')
BtnVSave = Button(vaultf,text = "Save !",command = Encrypt_Save,background = Honey)
BtnVFill = Button(vaultf,text = "Fill from Generator",command = Fill,background = Honey)
LbVPassword.grid(row = 1, column = 0,padx = 10,pady = 10)
EtVPassword.grid(row = 1, column = 1)
LbVUsername.grid(row =0 , column =0)
EtVUsername.grid(row = 0, column = 1)
LbVMemo.grid(row = 2, column = 0)
EtVMemo.grid(row = 2, column =1 )
BtnVSave.grid(row = 3, column = 1,columnspan = 2)
BtnVFill.grid(row = 1,column = 2)

#Password Manager Create and Configure

LbMSearch = Label(managerf,text = "   Search in Vault   ",bg = Sunshine,font=('',15))
LbMUsername=Label(managerf,text = "Username",bg = Sunshine)
EntMUsername =  Entry(managerf,text = "Username...",textvariable = SUsername)
LbMMemo=Label(managerf,text = "   Memo   ",bg = Sunshine)
EntMMemo = Entry(managerf,text = "Memo ...",textvariable = SMemo)
BtnMSearch = Button(managerf,text = "Search ! ",command = Search)
SPassword.set('Password will display here')
LbMResult=Label(managerf,text = "Passwords information will display here ...",textvariable = SPassword,bg = Sunshine)
PasswordO.set('    Password...    ')
LbMPasswordO = Label(managerf,textvariable = PasswordO,bg = Sunshine)
BtnMAutoFill = Button(managerf,text = "AutoFill",command =  AutoFill)
BtnMOpenVault = Button(managerf,text = "Open Vault",command = Open_Vault)
LbMSearch.grid(row = 0, column = 0,columnspan = 2)
LbMUsername.grid(row = 1, column =0 )
LbMMemo.grid(row = 2, column = 0)
BtnMSearch.grid(row =3 , column = 0)
LbMResult.grid(row = 1, column = 3,rowspan = 2)
EntMUsername.grid(row = 1, column = 1)
EntMMemo.grid(row =2 , column = 1)
BtnMOpenVault.grid(row =3 ,column =1 )
BtnMAutoFill.grid(row = 3,column = 2)
LbMPasswordO.grid(row = 3,column = 3,padx = 6,pady = 6)

#Main Frame Configure
Mainf.configure(height = 20,width = 150,background = Bone)
Title = Label(Mainf,text = "Random Password Generator",font=("Times", 32),background = Bone)
Account = Label(Mainf,textvariable = logonUsername,font = ("Times",10),bg = Bone)
EtGPassword = Entry(Mainf,text = "Pleas Enter Password",textvariable = Generate,background = 'white')
btnGGo = Button(Mainf,text = "Go !",command = Create,bg = Sunshine)
EtGPassword.grid(row = 1, column = 0)
Account.grid(row = 0,column = 1)
btnGGo.grid(row = 1, column = 1)
Title.grid(row = 0,column = 0)

#Frame Pack and final configure
root.configure(background = Bone)
Logonf.pack()
root.mainloop()
try:
	os.remove(personalvault.get())
	random_password_generator_ico()
except:
	random_password_generator_ico()