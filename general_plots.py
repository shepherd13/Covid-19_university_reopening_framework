 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import matplotlib.pyplot as plt
import os

#files = os.listdir("Plots_specific")
directory = "Plots_specific/"
os.chdir(directory)







##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Students
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################






# ##############################################################################################
# #										Student Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Student Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Student Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Student Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Professor Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']



# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Instructor Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Instructor Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Instructor Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Student Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']


# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Student Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Student Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Student Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Instructor Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Instructor Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Instructor Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Instructor Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')









# ##############################################################################################
# #										Ventilation rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_2acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_2acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']


# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_3acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_3acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']


# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']


# df_mean_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_5acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_5acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']


# df_mean_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_6acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_6acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='2 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='3 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='4 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Ventilation Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='2 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='3 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='4 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Ventilation Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='2 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='3 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='4 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='5 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='5 air changes/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Ventilation Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Student Density
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_15sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_50Pcompliance_15sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_20sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_20sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_30sqftpstudent_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_50Pcompliance_30sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_35sqftpstudent_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_50Pcompliance_35sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='15 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='25 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='30 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='35 sqft/student Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Student Density on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='15 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='25 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='30 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='35 sqft/student Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Student Density on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='15 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='25 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='30 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='35 sqft/student Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Student Density on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Quanta rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("14qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("14qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("48qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("48qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='14 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='48 quanta/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Quanta Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='14 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='48 quanta/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Quanta Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='14 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='48 quanta/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Quanta Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')






# ##############################################################################################
# #										Initially Infected Population
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")

# #df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# S_mean_1 = df_mean_1['Spreader']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
# #df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# #DI_se_2 = df_se_2['Daily Infected']
# #CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_2 = df_se_2['Hospitalized']
# S_mean_2 = df_mean_2['Spreader']
# I_mean_2 = df_mean_2['Infected']

# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_3 = df_mean_3['Spreader']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_4 = df_mean_4['Spreader']
# I_mean_4 = df_mean_4['Infected']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_5.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_5 = df_mean_5['Spreader']
# I_mean_5 = df_mean_5['Infected']

# df_mean_6 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_6.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_6 = df_mean_6['Daily Infected']
# CI_mean_6 = df_mean_6['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_6 = df_mean_6['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_6 = df_mean_6['Spreader']
# I_mean_6 = df_mean_6['Infected']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()
# plt.plot(range(0,length), CI_mean_1, label='Initial Infection=0.1% CI')
# plt.plot(range(0,length), CI_mean_2, label='Initial Infection=0.5% CI')
# plt.plot(range(0,length), CI_mean_3, label='Initial Infection=1.0% CI')
# plt.plot(range(0,length), CI_mean_4, label='Initial Infection=2.0% CI')
# plt.plot(range(0,length), CI_mean_5, label='Initial Infection=5.0% CI')
# plt.plot(range(0,length), CI_mean_6, label='Initial Infection=10.0% CI')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Initial Infected Population on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()
# plt.plot(range(0,length), DI_mean_1, label='Initial Infection=0.1% DI')
# plt.plot(range(0,length), DI_mean_2, label='Initial Infection=0.5% DI')
# plt.plot(range(0,length), DI_mean_3, label='Initial Infection=1.0% DI')
# plt.plot(range(0,length), DI_mean_4, label='Initial Infection=2.0% DI')
# plt.plot(range(0,length), DI_mean_5, label='Initial Infection=5.0% DI')
# plt.plot(range(0,length), DI_mean_6, label='Initial Infection=10.0% DI')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Initial Infected Population on new Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()
# plt.plot(range(0,length), H_mean_1, label='Initial Infection=0.1% H')
# plt.plot(range(0,length), H_mean_2, label='Initial Infection=0.5% H')
# plt.plot(range(0,length), H_mean_3, label='Initial Infection=1.0% H')
# plt.plot(range(0,length), H_mean_4, label='Initial Infection=2.0% H')
# plt.plot(range(0,length), H_mean_5, label='Initial Infection=5.0% H')
# plt.plot(range(0,length), H_mean_6, label='Initial Infection=10.0% H')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Initial Infected Population on new Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')


# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), S_mean_1, label='Initial Infection=0.1% S')
# plt.plot(range(0,length), S_mean_2, label='Initial Infection=0.5% S')
# plt.plot(range(0,length), S_mean_3, label='Initial Infection=1.0% S')
# plt.plot(range(0,length), S_mean_4, label='Initial Infection=2.0% S')
# plt.plot(range(0,length), S_mean_5, label='Initial Infection=5.0% S')
# plt.plot(range(0,length), S_mean_6, label='Initial Infection=10.0% S')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Impact of different Initial Infected Population on active Infection Spreaders"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')


# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_1, label='Initial Infection=0.1% I')
# plt.plot(range(0,length), I_mean_2, label='Initial Infection=0.5% I')
# plt.plot(range(0,length), I_mean_3, label='Initial Infection=1.0% I')
# plt.plot(range(0,length), I_mean_4, label='Initial Infection=2.0% I')
# plt.plot(range(0,length), I_mean_5, label='Initial Infection=5.0% I')
# plt.plot(range(0,length), I_mean_6, label='Initial Infection=10.0% I')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Impact of different Initial Infected Population on active Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Outside Infection=0.5 people/day'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')




# ##############################################################################################
# #										Outside Infection
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")

# #df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# S_mean_1 = df_mean_1['Spreader']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
# #df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# #DI_se_2 = df_se_2['Daily Infected']
# #CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_2 = df_se_2['Hospitalized']
# S_mean_2 = df_mean_2['Spreader']
# I_mean_2 = df_mean_2['Infected']

# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_3 = df_mean_3['Spreader']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_4 = df_mean_4['Spreader']
# I_mean_4 = df_mean_4['Infected']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_5.csv")
# #df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# #DI_se_3 = df_se_3['Daily Infected']
# #CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# #H_se_3 = df_se_3['Hospitalized']
# S_mean_5 = df_mean_5['Spreader']
# I_mean_5 = df_mean_5['Infected']

# df_mean_6 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_6.csv")
# #df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpstudent_4acph_airborne_se.csv")
# DI_mean_6 = df_mean_6['Daily Infected']
# CI_mean_6 = df_mean_6['Cumulative Infected']
# #DI_se_4 = df_se_4['Daily Infected']
# #CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_6 = df_mean_6['Hospitalized']
# #H_se_4 = df_se_4['Hospitalized']
# S_mean_6 = df_mean_6['Spreader']
# I_mean_6 = df_mean_6['Infected']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()
# plt.plot(range(0,length), CI_mean_1, label='Outside Infection=0.25 people/day CI')
# plt.plot(range(0,length), CI_mean_2, label='Outside Infection=0.50 people/day CI')
# plt.plot(range(0,length), CI_mean_3, label='Outside Infection=1 people/day CI')
# plt.plot(range(0,length), CI_mean_4, label='Outside Infection=2 people/day CI')
# plt.plot(range(0,length), CI_mean_5, label='Outside Infection=3 people/day CI')
# plt.plot(range(0,length), CI_mean_6, label='Outside Infection=4 people/day CI')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Impact of different Outside Infection on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()
# plt.plot(range(0,length), DI_mean_1, label='Outside Infection=0.25 people/day DI')
# plt.plot(range(0,length), DI_mean_2, label='Outside Infection=0.50 people/day DI')
# plt.plot(range(0,length), DI_mean_3, label='Outside Infection=1 people/day DI')
# plt.plot(range(0,length), DI_mean_4, label='Outside Infection=2 people/day DI')
# plt.plot(range(0,length), DI_mean_5, label='Outside Infection=3 people/day DI')
# plt.plot(range(0,length), DI_mean_6, label='Outside Infection=4 people/day DI')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "Impact of different Outside Infection on new Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()
# plt.plot(range(0,length), H_mean_1, label='Outside Infection=0.25 people/day H')
# plt.plot(range(0,length), H_mean_2, label='Outside Infection=0.50 people/day H')
# plt.plot(range(0,length), H_mean_3, label='Outside Infection=1 people/day H')
# plt.plot(range(0,length), H_mean_4, label='Outside Infection=2 people/day H')
# plt.plot(range(0,length), H_mean_5, label='Outside Infection=3 people/day H')
# plt.plot(range(0,length), H_mean_6, label='Outside Infection=4 people/day H')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "Impact of different Outside Infection on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')


# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), S_mean_1, label='Outside Infection=0.25 people/day S')
# plt.plot(range(0,length), S_mean_2, label='Outside Infection=0.50 people/day S')
# plt.plot(range(0,length), S_mean_3, label='Outside Infection=1 people/day S')
# plt.plot(range(0,length), S_mean_4, label='Outside Infection=2 people/day S')
# plt.plot(range(0,length), S_mean_5, label='Outside Infection=3 people/day S')
# plt.plot(range(0,length), S_mean_6, label='Outside Infection=4 people/day S')

# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Impact of different Outside Infection on active Infection Spreaders"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')


# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_1, label='Outside Infection=0.25 people/day I')
# plt.plot(range(0,length), I_mean_2, label='Outside Infection=0.50 people/day I')
# plt.plot(range(0,length), I_mean_3, label='Outside Infection=1 people/day I')
# plt.plot(range(0,length), I_mean_4, label='Outside Infection=2 people/day I')
# plt.plot(range(0,length), I_mean_5, label='Outside Infection=3 people/day I')
# plt.plot(range(0,length), I_mean_6, label='Outside Infection=4 people/day I')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Impact of different Outside Infection on active Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')






##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Instructors
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################









# ##############################################################################################
# #										Professor Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']



# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Instructor Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Instructor Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Instructor Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Student Mask Type
# ##############################################################################################

# df_mean_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_0Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_55Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_95Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='No Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='Cloth Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='Medical Mask Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='N95 Mask Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Mask Types on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='No Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='Cloth Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='Medical Mask Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='N95 Mask Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Mask Types on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='No Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='Cloth Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='Medical Mask Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='N95 Mask Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Mask Types on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')











# ##############################################################################################
# #										Professor Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Instructor Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Instructor Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Instructor Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Student Mask Compliance
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_25Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_50Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']

# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='0% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='25% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='50% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='75% Mask Compliance Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='100% Mask Compliance Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Mask Compliances on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='0% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='25% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='50% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='75% Mask Compliance Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='100% Mask Compliance Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Mask Compliances on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='0% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='25% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='50% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='75% Mask Compliance Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='100% Mask Compliance Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Mask Compliances on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ###############################################################################################
# ##										Ventilation rate
# ###############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_2acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_2acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_3acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_3acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_5acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_5acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_6acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_6acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='2 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='3 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='4 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='5 air changes/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Ventilation Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='2 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='3 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='4 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='5 air changes/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Ventilation Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='2 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='3 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='4 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='5 air changes/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='5 air changes/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Ventilation Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')








# ##############################################################################################
# #										Student Density
# ##############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_15sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_75Pcompliance_15sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_20sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_20sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']

# df_mean_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_30sqftpprofessor_4acph_airborne_mean.csv")
# df_se_4 = pd.read_csv("20qph_38Pcover_75Pcompliance_30sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# DI_se_4 = df_se_4['Daily Infected']
# CI_se_4 = df_se_4['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# H_se_4 = df_se_4['Hospitalized']

# df_mean_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_35sqftpprofessor_4acph_airborne_mean.csv")
# df_se_5 = pd.read_csv("20qph_38Pcover_75Pcompliance_35sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_5 = df_mean_5['Daily Infected']
# CI_mean_5 = df_mean_5['Cumulative Infected']
# DI_se_5 = df_se_5['Daily Infected']
# CI_se_5 = df_se_5['Cumulative Infected']
# H_mean_5 = df_mean_5['Hospitalized']
# H_se_5 = df_se_5['Hospitalized']



# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='15 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='25 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_4, 1.96*CI_se_4, label='30 sqft/student Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_5, 1.96*CI_se_4, label='35 sqft/student Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Student Density on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='15 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='25 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_4, 1.96*DI_se_4, label='30 sqft/student Daily Infected')
# plt.errorbar(range(0,length), DI_mean_5, 1.96*DI_se_4, label='35 sqft/student Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Student Density on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='15 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='25 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_4, 1.96*H_se_4, label='30 sqft/student Hospitalized')
# plt.errorbar(range(0,length), H_mean_5, 1.96*H_se_5, label='35 sqft/student Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Student Density on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')







# ##############################################################################################
# #										Quanta rate
# ##############################################################################################
# df_mean_1 = pd.read_csv("14qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_1 = pd.read_csv("14qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']

# df_mean_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_2 = pd.read_csv("20qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# DI_se_2 = df_se_2['Daily Infected']
# CI_se_2 = df_se_2['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# H_se_2 = df_se_2['Hospitalized']

# df_mean_3 = pd.read_csv("48qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_mean.csv")
# df_se_3 = pd.read_csv("48qph_38Pcover_75Pcompliance_25sqftpprofessor_4acph_airborne_se.csv")
# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# DI_se_3 = df_se_3['Daily Infected']
# CI_se_3 = df_se_3['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# H_se_3 = df_se_3['Hospitalized']


# #length = sparse_matrix.shape[0] ## time

# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='14 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_2, 1.96*CI_se_2, label='20 quanta/hour Cumulative Infected')
# plt.errorbar(range(0,length), CI_mean_3, 1.96*CI_se_3, label='48 quanta/hour Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of different Quanta Rates on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='14 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_2, 1.96*DI_se_2, label='20 quanta/hour Daily Infected')
# plt.errorbar(range(0,length), DI_mean_3, 1.96*DI_se_3, label='48 quanta/hour Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of different Quanta Rates on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='14 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_2, 1.96*H_se_2, label='20 quanta/hour Hospitalized')
# plt.errorbar(range(0,length), H_mean_3, 1.96*H_se_3, label='48 quanta/hour Hospitalized')

# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of different Quanta Rates on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=50%',
# 					'Instructor Mask Type=Cloth Mask',
# 					'Instructor Mask Compliance=75%',
# 					'Student Density=25 sqft/student',
# 					'Ventilation Rate=4 air changes/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')











##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
#
#										Policies
#
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################












# #############################################################################################
# #										No Policy
# #############################################################################################
# df_mean_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_38.01sqftpprofessor_4acph_airborne_60maxClassSize_mean.csv")
# df_se_1 = pd.read_csv("20qph_38Pcover_0Pcompliance_38.01sqftpprofessor_4acph_airborne_60maxClassSize_se.csv")
# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']



# length = 84
# fig1 = plt.figure()

# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Instructors', figure=fig1)
# title = "Impact of No Mask Policy on Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')

# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Instructors', figure=fig2)
# title = "Impact of No Mask Policy on Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')


# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Instructors', figure=fig3)
# title = "Impact of No Mask Policy on Hospitalized"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=No Mask',
# 					'Student Mask Compliance=0%',
# 					'Instructor Mask Type=No Mask',
# 					'Instructor Mask Compliance=0%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=38.01 sqft/student',
# 					'Quanta Rate=20 quanta/hour',
# 					'Max Offline Class Size=60'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')





# ##############################################################################################
# #										Strict Policy
# ##############################################################################################
# #df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_se.csv")

# df_mean_0 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_0.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_0 = df_mean_0['Daily Infected']
# CI_mean_0 = df_mean_0['Cumulative Infected']
# S_mean_0 = df_mean_0['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_0 = df_mean_0['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_0 = df_mean_0['Infected']

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# S_mean_1 = df_mean_1['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# S_mean_2 = df_mean_2['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_2 = df_mean_2['Infected']


# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# S_mean_3 = df_mean_3['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# S_mean_4 = df_mean_4['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_4 = df_mean_4['Infected']

# length = 84
# fig1 = plt.figure()

# #plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# plt.plot(range(0,length), CI_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), CI_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), CI_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), CI_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), CI_mean_4, label='Class Fraction=50%')

# plt.xlabel('Num Days', figure=fig1)
# plt.ylabel('Num Students', figure=fig1)
# title = "Cumulative Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
# #plt.show()
# fig1.savefig(title + '.png', bbox_inches='tight')


# fig2 = plt.figure()

# #plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
# plt.plot(range(0,length), DI_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), DI_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), DI_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), DI_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), DI_mean_4, label='Class Fraction=50%')


# plt.xlabel('Num Days', figure=fig2)
# plt.ylabel('Num Students', figure=fig2)
# title = "New Daily Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig2.savefig(title + '.png', bbox_inches='tight')


# fig3 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), H_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), H_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), H_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), H_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), H_mean_4, label='Class Fraction=50%')
# # plt.plot(range(0,length), H_mean_3, label='Class Fraction=100%')
# # plt.plot(range(0,length), H_mean_4, label='Outside Infection=8 people/day')


# plt.xlabel('Num Days', figure=fig3)
# plt.ylabel('Num Students', figure=fig3)
# title = "New Hospitalizations"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig3.savefig(title + '.png', bbox_inches='tight')



# fig4 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), S_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), S_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), S_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), S_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), S_mean_4, label='Class Fraction=50%')


# plt.xlabel('Num Days', figure=fig4)
# plt.ylabel('Num Students', figure=fig4)
# title = "Active Infection Spreaders"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig4.savefig(title + '.png', bbox_inches='tight')



# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), I_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), I_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), I_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), I_mean_4, label='Class Fraction=50%')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Pool of Active Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')

























# ##############################################################################################
# #										Strict Policy
# ##############################################################################################
# df_mean_1 = pd.read_csv("14 quantum per hour, Student with Strictest Mask - Short_mean.csv")
# df_se_1 = pd.read_csv("14 quantum per hour, Student with Strictest Mask - Short_se.csv")

# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# DI_se_1 = df_se_1['Daily Infected']
# CI_se_1 = df_se_1['Cumulative Infected']

# H_mean_1 = df_mean_1['Hospitalized']
# H_se_1 = df_se_1['Hospitalized']


# #length = sparse_matrix.shape[0] ## time
# length = 84
# fig = plt.figure()

# plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
# plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
# plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')

# plt.xlabel('Num Days', figure=fig)
# plt.ylabel('Num Students', figure=fig)	 # EDIT NUM PEOPLE WITH INSTRUCTORS OR STUDENTS
# title = "Policy: Everyone wears medical mask"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Medical Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=Medical Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=25 sqft/student',
# 					'Quanta Rate=20 quanta/hour'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig.savefig(title + '.png', bbox_inches='tight')










##############################################################################################
#										Strict Policy
##############################################################################################
#df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
#df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_38.01sqftpstudent_4acph_airborne_60maxClassSize_se.csv")

df_mean_0 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean.csv")
#df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")
ST_mean_0 = df_mean_0['Symptomatic Tests']
PST_mean_0 = df_mean_0['Positive Symptomatic Tests']
SI_mean_0 = df_mean_0['Symptomatic']
AI_mean_0 = df_mean_0['Asymptomatic']
CTT_mean_0 = df_mean_0['Contact Trace Tests']
PCTT_mean_0 = df_mean_0['Positive Contact Trace Tests']
ET_mean_0 = df_mean_0['Extra Tests']
PET_mean_0 = df_mean_0['Positive Extra Tests']

DI_mean_0 = df_mean_0['Daily Infected']
CI_mean_0 = df_mean_0['Cumulative Infected']
S_mean_0 = df_mean_0['Spreader']

# H_mean_0 = df_mean_0['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
I_mean_0 = df_mean_0['Infected']

# df_mean_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_1.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_1 = df_mean_1['Daily Infected']
# CI_mean_1 = df_mean_1['Cumulative Infected']
# S_mean_1 = df_mean_1['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_1 = df_mean_1['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_1 = df_mean_1['Infected']

# df_mean_2 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_2.csv")
#df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_2 = df_mean_2['Daily Infected']
# CI_mean_2 = df_mean_2['Cumulative Infected']
# S_mean_2 = df_mean_2['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_2 = df_mean_2['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_2 = df_mean_2['Infected']


# df_mean_3 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_3.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_3 = df_mean_3['Daily Infected']
# CI_mean_3 = df_mean_3['Cumulative Infected']
# S_mean_3 = df_mean_3['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_3 = df_mean_3['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_3 = df_mean_3['Infected']

# df_mean_4 = pd.read_csv("20qph_38Pcover_100Pcompliance_78.15sqftpstudent_4acph_airborne_30maxClassSize_mean_4.csv")
# #df_se_1 = pd.read_csv("20qph_38Pcover_100Pcompliance_25sqftpstudent_4acph_airborne_60maxClassSize_mean.csv")

# DI_mean_4 = df_mean_4['Daily Infected']
# CI_mean_4 = df_mean_4['Cumulative Infected']
# S_mean_4 = df_mean_4['Spreader']
# #DI_se_1 = df_se_1['Daily Infected']
# #CI_se_1 = df_se_1['Cumulative Infected']
# H_mean_4 = df_mean_4['Hospitalized']
# #H_se_1 = df_se_1['Hospitalized']
# I_mean_4 = df_mean_4['Infected']

length = 84
fig1 = plt.figure()

#plt.errorbar(range(0,length), CI_mean_1, 1.96*CI_se_1, label='Cumulative Infected')
plt.plot(range(0,length), ST_mean_0, label='Symptomatic Tests')
plt.plot(range(0,length), SI_mean_0, label='Symptomatic Infected')
plt.plot(range(0,length), PST_mean_0, label='Positive Symptomatic Tests')
#plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
#plt.plot(range(0,length), CTT_mean_0, label='Contact Trace Tests')
plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')

plt.xlabel('Num Days', figure=fig1)
plt.ylabel('Num Students', figure=fig1)
title = "Symptomatic Infected and Testing"
plt.title(title)
plt.grid(True)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

textstr = '\n'.join(['Student Mask Type=Cloth Mask',
					'Student Mask Compliance=100%',
					'Instructor Mask Type=N95 Mask',
					'Instructor Mask Compliance=100%',
					'Ventilation Rate=4 air changes/hour',
					'Student Density=78.15 sqft/student',
					'Max Offline Class Size=30',
					'Quanta Rate=20 quanta/hour',
					'Initial Infection=1% population',
					'Outside Infection=2 people/day',
					'Testing Gap Days=3 days',
					'Class Fraction=50%',
					'Contact Trace Test Type=Random'])
props = dict(boxstyle='round', facecolor='white', alpha=0.15)
plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)
#plt.show()
fig1.savefig(title + '.png', bbox_inches='tight')


fig2 = plt.figure()

#plt.errorbar(range(0,length), DI_mean_1, 1.96*DI_se_1, label='Daily Infected')
#plt.plot(range(0,length), ST_mean_0, label='Symptomatic Tests')
#plt.plot(range(0,length), PST_mean_0, label='Positive Symptomatic Tests')
#plt.plot(range(0,length), SI_mean_0, label='Symptomatic Infected')
plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
plt.plot(range(0,length), CTT_mean_0, label='Contact Trace Tests/Symptomatic Class Tests')
plt.plot(range(0,length), PCTT_mean_0, label='Positive Contact Trace Tests')
plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')


plt.xlabel('Num Days', figure=fig2)
plt.ylabel('Num Students', figure=fig2)
title = "Contact Tracing and Testing"
plt.title(title)
plt.grid(True)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

textstr = '\n'.join(['Student Mask Type=Cloth Mask',
					'Student Mask Compliance=100%',
					'Instructor Mask Type=N95 Mask',
					'Instructor Mask Compliance=100%',
					'Ventilation Rate=4 air changes/hour',
					'Student Density=78.15 sqft/student',
					'Max Offline Class Size=30',
					'Quanta Rate=20 quanta/hour',
					'Initial Infection=1% population',
					'Outside Infection=2 people/day',
					'Testing Gap Days=3 days',
					'Class Fraction=50%',
					'Contact Trace Test Type=Random'])
props = dict(boxstyle='round', facecolor='white', alpha=0.15)
plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

#plt.show()
fig2.savefig(title + '.png', bbox_inches='tight')


fig3 = plt.figure()

#plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
plt.plot(range(0,length), AI_mean_0, label='Asymptomatic Infected')
plt.plot(range(0,length), ET_mean_0, label='Asymptomatic Class Tests')
plt.plot(range(0,length), PET_mean_0, label='Positive Asymptomatic Class Tests')
plt.plot(range(0,length), DI_mean_0, label='Daily New Infected')
plt.plot(range(0,length), S_mean_0, label='Active Virus Spreaders')

plt.xlabel('Num Days', figure=fig3)
plt.ylabel('Num Students', figure=fig3)
title = "Asymptomatic Class Tests"
plt.title(title)
plt.grid(True)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

textstr = '\n'.join(['Student Mask Type=Cloth Mask',
					'Student Mask Compliance=100%',
					'Instructor Mask Type=N95 Mask',
					'Instructor Mask Compliance=100%',
					'Ventilation Rate=4 air changes/hour',
					'Student Density=78.15 sqft/student',
					'Max Offline Class Size=30',
					'Quanta Rate=20 quanta/hour',
					'Initial Infection=1% population',
					'Outside Infection=2 people/day',
					'Testing Gap Days=3 days',
					'Class Fraction=50%',
					'Contact Trace Test Type=Random'])
props = dict(boxstyle='round', facecolor='white', alpha=0.15)
plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

#plt.show()
fig3.savefig(title + '.png', bbox_inches='tight')



fig4 = plt.figure()

#plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
plt.plot(range(0,length), I_mean_0, label='Active pool of Infected')
plt.plot(range(0,length), CI_mean_0, label='Cumulative Infected')


plt.xlabel('Num Days', figure=fig4)
plt.ylabel('Num Students', figure=fig4)
title = "Infection Spread"
plt.title(title)
plt.grid(True)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

textstr = '\n'.join(['Student Mask Type=Cloth Mask',
					'Student Mask Compliance=100%',
					'Instructor Mask Type=N95 Mask',
					'Instructor Mask Compliance=100%',
					'Ventilation Rate=4 air changes/hour',
					'Student Density=78.15 sqft/student',
					'Max Offline Class Size=30',
					'Quanta Rate=20 quanta/hour',
					'Initial Infection=1% population',
					'Outside Infection=2 people/day',
					'Testing Gap Days=3 days',
					'Class Fraction=50%',
					'Contact Trace Test Type=Random'])
props = dict(boxstyle='round', facecolor='white', alpha=0.15)
plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

#plt.show()
fig4.savefig(title + '.png', bbox_inches='tight')



# fig5 = plt.figure()

# #plt.errorbar(range(0,length), H_mean_1, 1.96*H_se_1, label='Hospitalized')
# plt.plot(range(0,length), I_mean_0, label='Class Fraction=0%')
# plt.plot(range(0,length), I_mean_1, label='Class Fraction=5%')
# plt.plot(range(0,length), I_mean_2, label='Class Fraction=10%')
# plt.plot(range(0,length), I_mean_3, label='Class Fraction=25%')
# plt.plot(range(0,length), I_mean_4, label='Class Fraction=50%')

# plt.xlabel('Num Days', figure=fig5)
# plt.ylabel('Num Students', figure=fig5)
# title = "Pool of Active Infected"
# plt.title(title)

# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

# textstr = '\n'.join(['Student Mask Type=Cloth Mask',
# 					'Student Mask Compliance=100%',
# 					'Instructor Mask Type=N95 Mask',
# 					'Instructor Mask Compliance=100%',
# 					'Ventilation Rate=4 air changes/hour',
# 					'Student Density=78.15 sqft/student',
# 					'Max Offline Class Size=30',
# 					'Quanta Rate=20 quanta/hour',
# 					'Initial Infection=1% population',
# 					'Outside Infection=2 people/day',
# 					'Testing Gap Days=3 days'])
# props = dict(boxstyle='round', facecolor='white', alpha=0.15)
# plt.text(1.06, 0.05, textstr, transform=plt.gca().transAxes, bbox=props)

# #plt.show()
# fig5.savefig(title + '.png', bbox_inches='tight')
