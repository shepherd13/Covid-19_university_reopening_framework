from main import run

f = open("template.txt")
a = f.read().split("\n")
f.close()
# mr = ['0','25','50','75','100']
# mrp = ['0.00','0.25','0.50','0.75','1.00']
# me = ['0','38','55','95']
# mep = ['0.0','0.38','0.55','0.95']
mr = ['75']
mrp = ['0.75']
me = ['38']
mep = ['0.38']
#vent = ['2','3','4','5','6']
vent = ['4']
line_1_part_1 = "Output Directory: 20qph_"
line_1_part_2 = "Pcover_"
line_1_part_3 = "Pcompliance_25sqftpprofessor_"
line_1_part_4 = "acph_airborne"

line_3_part_1 = "Vent Rate: "
line_7_part_1 = "Mask Rate 2: "
line_8_part_1 = "Mask Efficiency 2: "

for k in range(len(vent)):
	for i in range(len(mr)):
		for j in range(len(me)):
			line1 = line_1_part_1 + me[j] + line_1_part_2 + mr[i] + line_1_part_3 + vent[k] + line_1_part_4
			line3 = line_3_part_1 + vent[k]
			line7 = line_7_part_1 + mrp[i]
			line8 = line_8_part_1 + mep[j]
			a[0] = line1
			a[2] = line3
			a[6] = line7
			a[7] = line8
			print(line1)
			f = open("template.txt",'w')
			f.write("\n".join(a))
			f.close()
			run()



# # Students
# from main import run

# f = open("template.txt")
# a = f.read().split("\n")
# f.close()
# mr = ['0','25','50','75','100']
# mrp = ['0.00','0.25','0.50','0.75','1.00']
# # me = ['0','38','55','95']
# # mep = ['0.0','0.38','0.55','0.95']
# mr = ['50']
# mrp = ['0.50']
# me = ['38']
# mep = ['0.38']
# vent = ['2','3','4','5','6']
# # vent = ['4']
# line_1_part_1 = "Output Directory: 20qph_"
# line_1_part_2 = "Pcover_"
# line_1_part_3 = "Pcompliance_25sqftpstudent_"
# line_1_part_4 = "acph_airborne"

# line_3_part_1 = "Vent Rate: "
# line_5_part_1 = "Mask Rate: "
# line_6_part_1 = "Mask Efficiency: "

# for k in range(len(vent)):
# 	for i in range(len(mr)):
# 		for j in range(len(me)):
# 			line1 = line_1_part_1 + me[j] + line_1_part_2 + mr[i] + line_1_part_3 + vent[k] + line_1_part_4
# 			line3 = line_3_part_1 + vent[k]
# 			line5 = line_5_part_1 + mrp[i]
# 			line6 = line_6_part_1 + mep[j]
# 			a[0] = line1
# 			a[2] = line3
# 			a[4] = line5
# 			a[5] = line6
# 			print(line1)
# 			f = open("template.txt",'w')
# 			f.write("\n".join(a))
# 			f.close()
# 			run()

