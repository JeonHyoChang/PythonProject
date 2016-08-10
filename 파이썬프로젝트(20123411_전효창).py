#-*- coding: utf-8 -*-
from Tkinter import *
import os
import string

# 함수&기능 부분
def date_list(str):
	temp = ""
	data_li = []
	for s in str:
		if s != '\n':
			temp += s
		else:
			data_li.append(temp)
			temp = ""
			
	return data_li

def is_digit(str):
	try:
		tmp = float(str)
		return True
	except ValueError:
		False
		
def enter_count(str):
	c = 0
	
	for s in str:
		if s == '\n':
			c += 1
	return c
	
def list_del(str, num):
	display_01.delete(1.0, END)
	c = 0
	temp = num + "\t"
	x = 0
	for s in date_list(str):
		if s.startswith(temp):
			c = 1
		else:
			if x==enter_count(str)-1:
				display_01.insert(END, s)
			else:
				display_01.insert(END, s)
				display_01.insert(END, '\n')
		x += 1
			
	return c
	
def split_data(str):
	data=[]
	count = 0
	for s in date_list(str):
		if count < int(enter_count(str)-1):
			temp = string.split(s)
			temp[0]	= int(temp[0])
			temp[2] = float(temp[2])
			data.append(temp)
		count += 1
	return data
	
def re_print_split(str):
	display_01.delete(1.0, END)
	
	for s in str:
		display_01.insert(END, s[0])
		display_01.insert(END, "\t")
		display_01.insert(END, s[1].ljust(20))
		display_01.insert(END, "\t")
		display_01.insert(END, s[2])
		display_01.insert(END, "\n")

def number_sort(str):
	data=split_data(str)
	
	def number(t):
		return t[0]
	
	data.sort(key=number)
				
	re_print_split(data)
		
def name_sort(str):
	data=split_data(str)
	
	def name(t):
		return t[1]
		
	data.sort(key=name)
					
	re_print_split(data)

def score_sort(str, check):
	data=split_data(str)
	
	def score(t):
		return t[2]
	
	if check == '점수내림차순':
		data.sort(key=score, reverse=True)
	else:
		data.sort(key=score)
						
	re_print_split(data)	

def click(key):
	temp1 = name.get()
	temp2 = score.get()
	temp3 = display_01.get(1.0, END)
	
	if key == '추가':
		if temp1=="" or not is_digit(temp2) or temp2=="" or temp3.count(temp1) >= 1:
			if temp1=="":
				error_text = "이름이 공란입니다."
			elif not is_digit(temp2) or temp2=="":
				error_text = "점수가 올바른 형태가 아닙니다."
			else:
				error_text = "동일한 이름이 이미 존재합니다."
				
			display_02.insert(END, "\n[추가 실패] " + error_text)
			display_02.see(END)
		else:
			display_01.insert(END, enter_count(temp3))
			display_01.insert(END, "\t")
			display_01.insert(END, temp1.ljust(20))
			display_01.insert(END, "\t")
			display_01.insert(END, temp2)
			display_01.insert(END, "\n")
			name.delete(0, END)
			score.delete(0, END)
			
			display_02.insert(END, "\n성공적으로 추가하였습니다.")
			display_02.see(END)
		
	elif key == '삭제':
		temp4 = number.get()
		if not is_digit(temp4) or temp4=="":
			error_text = "번호가 올바른 형태가 아닙니다."

			display_02.insert(END, "\n[삭제 실패] " + error_text)
			display_02.see(END)
	
		else:
			if list_del(temp3, temp4):
				number.delete(0, END)
				display_02.insert(END, "\n성공적으로 삭제하였습니다.")
			else:
				display_02.insert(END,  "\n[삭제 실패] 존재하지 않는 번호를 입력하셨습니다.")
				
			display_02.see(END)
		
		
	elif key == '저장':
		temp5 = file_name_01.get()
		
		if temp5 != "":
			f = open(os.path.dirname(os.path.realpath(__file__)) + '\\' + temp5, 'w')
			f.write(temp3.rstrip())
			f.write('\n')
			f.close
			
			file_name_01.delete(0, END)
			
			display_02.insert(END, "\n성공적으로 저장하였습니다. (파일이름: " + temp5 + ")")
		else:
			display_02.insert(END, "\n파일 저장에 실패하였습니다.")
			
		display_02.see(END)
		
	elif key == '열기':
		temp6 = file_name_02.get()
		
		if temp6 != "":
			if os.path.exists(os.path.dirname(os.path.realpath(__file__)) + "\\" + temp6):
				f = open(os.path.dirname(os.path.realpath(__file__)) + '\\' + temp6, 'r')
								
				display_01.delete(1.0, END)
				for str in f.readlines():
					display_01.insert(END, str)
				
				f.close
				
				file_name_02.delete(0, END)
				
				display_02.insert(END, "\n성공적으로 파일을 열었였습니다. (파일이름: " + temp6 + ")")
			else:
				display_02.insert(END, "\n파일 불러오기에 실패하였습니다.")
		else:
			display_02.insert(END, "\n파일 불러오기에 실패하였습니다.")
			
		display_02.see(END)
		
	elif key == '번호순':
		number_sort(temp3)
		display_02.delete(1.0, END)
		
	elif key == '이름순':
		name_sort(temp3)
		display_02.delete(1.0, END)
		
	else:
		score_sort(temp3, key)
		display_02.delete(1.0, END)

lbl_list = [
	'이름', '점수',
	'번호', '파일이름',
	'파일이름'
]
but_01_list = [
	'추가', '삭제',
	'저장', '열기'
]
but_02_list = [
	'번호순', '이름순',
	'점수내림차순', '점수오름차순'
]	
	
# UI부분
window = Tk()
window.title('tk')


take_01 = Frame(window)
take_01.grid(row=0, column=0)

# 라벨 입력
r=0; c=0
for input_lbl in lbl_list:
	Label(take_01, text=input_lbl).grid(row=r, column=c, sticky=E)
	if c == 2:
		r += 1
	c=2

# 라벨에 따른 text상자 입력
name = Entry(take_01, width=20, bg="light green")
name.pack()
name.grid(row=0, column=1, sticky=W)

score = Entry(take_01, width=7, bg="light green")
score.pack()
score.grid(row=0, column=3, sticky=W)

number = Entry(take_01, width=5, bg="light green")
number.pack()
number.grid(row=1, column=3, sticky=W)

file_name_01 = Entry(take_01, width=20, bg="light blue")
file_name_01.pack()
file_name_01.grid(row=2, column=3, sticky=W)

file_name_02 = Entry(take_01, width=20, bg="light blue")
file_name_02.pack()
file_name_02.grid(row=3, column=3, sticky=W)


# 버튼01 입력
r=0; c=4
for input_but_01 in but_01_list:
	def cmd(x=input_but_01):
		click(x)
	Button(take_01, text=input_but_01, width=5, command=cmd).grid(row=r, column=c, sticky=W)
	r += 1


take_02 = Frame(window)
take_02.grid(row=4, column=0)
# 버튼02 입력
r=0; c=0; count=0
for input_but_02 in but_02_list:
	if count < 2:
		wid = 5
	else:
		wid = 15
	def cmd(x=input_but_02):
		click(x)
	Button(take_02, text=input_but_02, width=wid, command=cmd).grid(row=r, column=c)
	c += 1
	count += 1


take_03 = Frame(window)
take_03.grid(row=5, column=0)
# 텍스트(데이터 출력창)
display_01=Text(take_03, width=75, height=10, bg="light yellow")
display_01.pack()
c = display_01.get('0.0', END).count('\n') + 1

take_04 = Frame(window)
take_04.grid(row=6, column=0)
# 텍스트(상태 메시지 출력창)
display_02=Text(take_04, width=75, height=1, bg="pink")
display_02.pack()


window.mainloop()