question_list=["(1)Which animal is known as the ship of the desert?","(2)How many consonant are there in the English alphabet","(3)Which planet is known as the red planet?","(4)Which is the following is not a metal:gold,resin,glass?","(5)Which country does Volleyball originate from?","(6)During which year did world war 1st begin?","(7)Which first electrical item did Thomas Edison invent?","(8)How many players are there in an Volleyball team?","(9)How many days are there in a year?","(10)How many colours are there in a rainbow?"]
first_option=["1.horse","1.21","1.shani","1.resin","1.India","1.1920","1.Train engin","1.eight","1.366","1.7"]
second_option=["2.camel","2.23","2.Varun","2.gold","2.the USA","2.1915","2.Light bulb","2.four","2.365","2.9"]
third_option=["3.lion","3.20","3.mars","3.glass","3.england","3.1914","3.fan","3.seven","3.360","3.8"]
fourth_option=["4.tiger","4.26","4.sun","4.silver","4.australia","4.1916","4.watch","4.six","4.368","4.10"]
#all_options=[first_option,second_option,third_option,fourth_option]
ans_key=[2,1,3,1,2,3,2,4,2,1]
amount=[20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
a=0
ans_list=[]
while a<len(question_list):
	if a%5==0 and a!=0:
		print "congrats!aapka pehla padaav pura ho gaya hai"
	print question_list[a],len(question_list[a])
	print first_option[a]
	print second_option[a]
	print third_option[a]
	print fourth_option[a]
	ans=input("input your option number-")
	if ans==ans_key[a]:
		print "congrates! aapka answer sahi hai aap",amount[a],"rupaye jeet gaye"
	else:
		print "aapka answer galat hai"
		break
	ans_list.append(ans)
	a=a+1
else:
	print "Congrates! aap ek coror(10000000)rupaye jeet gaye hai"
print "Total your answer keys",ans_list
