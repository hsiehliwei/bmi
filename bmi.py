h = input('請輸入身高(cm):')
w= input('請輸入體重(kg):')
h = float(h)
w = float(w)
h = h / 100 #換算成m
bmi = w / h / h
print(bmi)
if bmi < 18.5:
	print('你的bmi值為', bmi, '體重過輕')
elif bmi >= 18.5 and bmi < 24:
	print('你的bmi值為', bmi, '正常範圍')
elif bmi >= 24 and bmi < 27:
	print('你的bmi值為', bmi, '過重')
elif bmi >= 27 and bmi < 30:
	print('你的bmi值為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
	print('你的bmi值為', bmi, '中度肥胖')
else:
	print('你的bmi值為', bmi, '重度肥胖')
