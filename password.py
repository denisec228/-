#Генератор паролей

from tkinter import *
import pyperclip
import random

colors = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff', 'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender', 'lavender blush', 'misty rose', 'gray', 'light grey',  'blue', 'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'light steel blue', 'light blue', 'powder blue', 'pale turquoise', 'light cyan', 'medium aquamarine', 'aquamarine', 'dark sea green', 'pale green', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow', 'light yellow', 'light goldenrod', 'pink', 'light pink', 'thistle', 'snow2', 'snow3', 'seashell2', 'AntiqueWhite1', 'AntiqueWhite2', 'AntiqueWhite3', 'bisque2', 'bisque3', 'PeachPuff2', 'PeachPuff3', 'NavajoWhite2', 'NavajoWhite3', 'LemonChiffon2', 'LemonChiffon3', 'cornsilk2', 'cornsilk3', 'ivory2', 'ivory3', 'honeydew2', 'honeydew3', 'LavenderBlush2', 'LavenderBlush3', 'MistyRose2', 'MistyRose3', 'azure2', 'azure3', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'DeepSkyBlue2', 'DeepSkyBlue3', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightCyan2', 'LightCyan3', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'turquoise1', 'turquoise2', 'turquoise3', 'cyan2', 'cyan3', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'SeaGreen1', 'SeaGreen2', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'SpringGreen2', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'khaki1', 'khaki2', 'khaki3', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightYellow2', 'LightYellow3', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'burlywood1', 'burlywood2', 'burlywood3', 'wheat1', 'wheat2', 'wheat3', 'tan1', 'tan2', 'salmon1', 'salmon2', 'salmon3', 'LightSalmon2', 'LightSalmon3', 'coral1', 'coral2', 'coral3', 'tomato2', 'tomato3', 'HotPink1', 'HotPink2', 'HotPink3', 'pink1', 'pink2', 'pink3', 'LightPink1', 'LightPink2', 'LightPink3', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'plum1', 'plum2', 'plum3',]
background_color = random.choice(colors)

window = Tk()
window.title("Генератор паролей")
window.geometry("224x300")
window.resizable(False, False)
window["bg"] = background_color

print_password = StringVar()

def Generating_a_password():
	
	numbers_1 = '1234567890'
	numbers_2 = '+-/*!&$#?=@<>'
	numbers_3 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers_4 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*!&$#?=@<>'
	numbers_5 = 'abcdefghijklmnopqrstuvwxyz'
	numbers_6 = 'abcdefghijklmnopqrstuvwxyz+-/*!&$#?=@<>'
	numbers_7 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers_8 = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*!&$#?=@<>'
	numbers_9 = '1234567890+-/*!&$#?=@<>'
	numbers_10 = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	numbers_11 = '1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ+-/*!&$#?=@<>'
	numbers_12 = '1234567890abcdefghijklmnopqrstuvwxyz'
	numbers_13 = '1234567890abcdefghijklmnopqrstuvwxyz+-/*!&$#?=@<>'

	length = 1
	number = int("{}".format(number_of_characters.get()))

	for x in range(length):
		password = ''

		for i in range(number):

			if (chk_state_1.get() == 0) and (chk_state_2.get() == 0) and (chk_state_3.get() == 0) and (chk_state_4.get() == 0):
				print('Ошибка')
			elif (chk_state_1.get() == 0) and (chk_state_2.get() == 0) and (chk_state_3.get() == 0) and (chk_state_4.get() == 1):
				password += random.choice(numbers_2)
			elif (chk_state_1.get() == 0) and (chk_state_2.get() == 0) and (chk_state_3.get() == 1) and (chk_state_4.get() == 0):
				password += random.choice(numbers_3)
			elif (chk_state_1.get() == 0) and (chk_state_2.get() == 0) and (chk_state_3.get() == 1) and (chk_state_4.get() == 1):
				password += random.choice(numbers_4)
			elif (chk_state_1.get() == 0) and (chk_state_2.get() == 1) and (chk_state_3.get() == 0) and (chk_state_4.get() == 0):
				password += random.choice(numbers_5)
			elif (chk_state_1.get() == 0) and (chk_state_2.get() == 1) and (chk_state_3.get() == 0) and (chk_state_4.get() == 1):
				password += random.choice(numbers_6)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 1) and (chk_state_3.get() == 1) and (chk_state_4.get() == 0):
				password += random.choice(numbers_7)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 1) and (chk_state_3.get() == 1) and (chk_state_4.get() == 1):
				password += random.choice(numbers_8)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 0) and (chk_state_3.get() == 0) and (chk_state_4.get() == 0):
				password += random.choice(numbers_1)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 0) and (chk_state_3.get() == 0) and (chk_state_4.get() == 1):
				password += random.choice(numbers_9)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 0) and (chk_state_3.get() == 1) and (chk_state_4.get() == 0):
				password += random.choice(numbers_10)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 0) and (chk_state_3.get() == 1) and (chk_state_4.get() == 1):
				password += random.choice(numbers_11)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 1) and (chk_state_3.get() == 0) and (chk_state_4.get() == 0):
				password += random.choice(numbers_12)
			elif (chk_state_1.get() == 1) and (chk_state_2.get() == 1) and (chk_state_3.get() == 0) and (chk_state_4.get() == 1):
				password += random.choice(numbers_13)

		print_password.set(password)

def Copy_password():
	random_password = print_password.get()
	pyperclip.copy(random_password)

lbl_1 = Label(window, text="Количество символов", bg = background_color, fg = 'gray1')  
lbl_1.grid(column=0, row=1)
number_of_characters = Entry(window,width=10) 												 
number_of_characters.grid(column=0, row=2)

chk_state_1 = IntVar()  
chk_state_1.set(1)
chk_1 = Checkbutton(window, text='Цифры', variable=chk_state_1, bg = background_color, fg = 'gray1', onvalue=1, offvalue=0)  
chk_1.grid(column=0, row=3)

chk_state_2 = IntVar()  
chk_state_2.set(0)
chk_2 = Checkbutton(window, text='Строчные буквы', variable=chk_state_2, bg = background_color, fg = 'gray1', onvalue=1, offvalue=0)  
chk_2.grid(column=0, row=4)

chk_state_3 = IntVar()  
chk_state_3.set(0)
chk_3 = Checkbutton(window, text='Заглавные буквы', variable=chk_state_3, bg = background_color, fg = 'gray1', onvalue=1, offvalue=0)  
chk_3.grid(column=0, row=5)

chk_state_4 = IntVar()  
chk_state_4.set(0)
chk_4 = Checkbutton(window, text='Спец символы', variable=chk_state_4, bg = background_color, fg = 'gray1', onvalue=1, offvalue=0)  
chk_4.grid(column=0, row=6)

btn = Button(window, text="Сгенерировать пароль", bg = background_color, fg = 'gray1', command = Generating_a_password)
btn.grid(column=0, row=7)

output_window = Entry(window, textvariable = print_password, width=36)
output_window.grid(column=0, row=8)

btn_2 = Button(window, text="Скопировать пароль", bg = background_color, fg = 'gray1', command = Copy_password)
btn_2.grid(column=0, row=9)

window.mainloop()