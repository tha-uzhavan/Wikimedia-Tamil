count_lines = sum(1 for line in open('cleaned.csv'))
integer2string = str(count_lines)
print('Total contributors = '+integer2string)

content = open('uncleaned.csv','r').readlines()
content4set = set(content)
cleanedcontent = open('cleaned.csv','w')
for i, line in enumerate(content4set):
	cleanedcontent.write("{}.{}".format(str(i+1),line.replace('பக்கம்','அட்டவணை_பேச்சு')))
	line=line.strip()
	print(line)
