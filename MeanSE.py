 # -*- coding: utf-8 -*-
import csv
import pandas as pd
import numpy as np
import glob
import scipy
from scipy import stats
import matplotlib.pyplot as plt

def updateCSV2(export, sus, inf, cumInf, dailyInf, inc, asym, sym, rec, dead, dailyDead, hosp, breath, resp, ICU, 
    peopleTested, spreader, quarantined, symptomatic_tests, contact_trace_tests, extra_tests, positive_symptomatic_tests, positive_contact_trace_tests, positive_extra_tests):
    with open(export, 'w', newline='') as f:
        writer = csv.writer(f)

        l = []
        l.append('Day')
        l.append('Susceptible')
        l.append('Infected')
        l.append('Cumulative Infected')
        l.append('Daily Infected')
        l.append('Incubating')
        l.append('Asymptomatic')
        l.append('Symptomatic')
        l.append('Recovered')
        l.append('Dead')
        l.append('Daily Dead')
        l.append('Hospitalized')
        l.append('Breathing Issue')
        l.append('Respirator')
        l.append('ICU')
        l.append('Daily Tested')
        l.append('Spreader')
        l.append('Quarantined')
        l.append('Symptomatic Tests')
        l.append('Contact Trace Tests')
        l.append('Extra Tests')
        l.append('Positive Symptomatic Tests')
        l.append('Positive Contact Trace Tests')
        l.append('Positive Extra Tests')
        writer.writerow(l)

        for i in range(len(sus)):
            l = []
            l.append(i)
            l.append(sus[i])
            l.append(inf[i])
            l.append(cumInf[i])
            l.append(dailyInf[i])
            l.append(inc[i])
            l.append(asym[i])
            l.append(sym[i])
            l.append(rec[i])
            l.append(dead[i])
            l.append(dailyDead[i])
            l.append(hosp[i])
            l.append(breath[i])
            l.append(resp[i])
            l.append(ICU[i])
            l.append(peopleTested[i])
            l.append(spreader[i])
            l.append(quarantined[i])
            l.append(symptomatic_tests[i])
            l.append(contact_trace_tests[i])
            l.append(extra_tests[i])
            l.append(positive_symptomatic_tests[i])
            l.append(positive_contact_trace_tests[i])
            l.append(positive_extra_tests[i])
            writer.writerow(l)

def getMean(length, directory, title):
    file_names = glob.glob(directory + "/*.csv")

    List = []

    for file in file_names:
        if len(file.split('/')[1]) > 6:
           continue
        df = pd.read_csv(file, skiprows=1)
        List.append(df)

    SusMat = []
    InfMat = []
    CumInfMat = []
    DailyInfMat = []
    num_incub = []
    AsymMat = []
    SymMat = []
    RecMat = []
    DeadMat = []
    DailyDeadMat = []
    HospMat = []
    breathMat = []
    respMat = []
    icuMat = []
    DailyTestedMat = []
    SpreaderMat = []
    QuarantinedMat = []
    SymptomaticTestsMat = []
    ContactTraceTestsMat = []
    ExtraTestsMat = []
    Positive_SymptomaticTestsMat = []
    Positive_ContactTraceTestsMat = []
    Positive_ExtraTestsMat = []

    for elem in List:
        SusMat.append(elem['Susceptible'].tolist())
        InfMat.append(elem['Infected'].tolist())
        CumInfMat.append(elem['Cumulative Infected'].tolist())
        DailyInfMat.append(elem['Daily Infected'].tolist())
        num_incub.append(elem['Incubating'].tolist())
        AsymMat.append(elem['Asymptomatic'].tolist())
        SymMat.append(elem['Symptomatic'].tolist())
        RecMat.append(elem['Recovered'].tolist())
        DeadMat.append(elem['Dead'].tolist())
        DailyDeadMat.append(elem['Daily Dead'].tolist())
        HospMat.append(elem['Hospitalized'].tolist())
        breathMat.append(elem['Breathing Issue'].tolist())
        respMat.append(elem['Respirator'].tolist())
        icuMat.append(elem['ICU'].tolist())
        DailyTestedMat.append(elem['Daily Tested'].tolist())
        SpreaderMat.append(elem['Spreader'].tolist())
        QuarantinedMat.append(elem['Quarantined'].tolist())
        SymptomaticTestsMat.append(elem['Symptomatic Tests'].tolist())
        ContactTraceTestsMat.append(elem['Contact Trace Tests'].tolist())
        ExtraTestsMat.append(elem['Extra Tests'].tolist())
        Positive_SymptomaticTestsMat.append(elem['Positive Symptomatic Tests'].tolist())
        Positive_ContactTraceTestsMat.append(elem['Positive Contact Trace Tests'].tolist())
        Positive_ExtraTestsMat.append(elem['Positive Extra Tests'].tolist())
        

    SusMat = np.column_stack(tuple(SusMat))
    InfMat = np.column_stack(tuple(InfMat))
    CumInfMat = np.column_stack(tuple(CumInfMat))
    DailyInfMat = np.column_stack(tuple(DailyInfMat))
    num_incub = np.column_stack(tuple(num_incub))
    AsymMat = np.column_stack(tuple(AsymMat))
    SymMat = np.column_stack(tuple(SymMat))
    RecMat = np.column_stack(tuple(RecMat))
    DeadMat = np.column_stack(tuple(DeadMat))
    DailyDeadMat = np.column_stack(tuple(DailyDeadMat))
    HospMat = np.column_stack(tuple(HospMat))
    breathMat = np.column_stack(tuple(breathMat))
    respMat = np.column_stack(tuple(respMat))
    icuMat = np.column_stack(tuple(icuMat))
    DailyTestedMat = np.column_stack(tuple(DailyTestedMat))
    SpreaderMat = np.column_stack(tuple(SpreaderMat))
    QuarantinedMat = np.column_stack(tuple(QuarantinedMat))
    SymptomaticTestsMat = np.column_stack(tuple(SymptomaticTestsMat))
    ContactTraceTestsMat = np.column_stack(tuple(ContactTraceTestsMat))
    ExtraTestsMat = np.column_stack(tuple(ExtraTestsMat))
    Positive_SymptomaticTestsMat = np.column_stack(tuple(Positive_SymptomaticTestsMat))
    Positive_ContactTraceTestsMat = np.column_stack(tuple(Positive_ContactTraceTestsMat))
    Positive_ExtraTestsMat = np.column_stack(tuple(Positive_ExtraTestsMat))

    SusMat = SusMat.transpose()
    InfMat = InfMat.transpose()
    CumInfMat = CumInfMat.transpose()
    DailyInfMat = DailyInfMat.transpose()
    num_incub = num_incub.transpose()
    AsymMat = AsymMat.transpose()
    SymMat = SymMat.transpose()
    RecMat = RecMat.transpose()
    DeadMat = DeadMat.transpose()
    DailyDeadMat = DailyDeadMat.transpose()
    HospMat = HospMat.transpose()
    breathMat = breathMat.transpose()
    respMat = respMat.transpose()
    icuMat = icuMat.transpose()
    DailyTestedMat = DailyTestedMat.transpose()
    SpreaderMat = SpreaderMat.transpose()
    QuarantinedMat = QuarantinedMat.transpose()
    SymptomaticTestsMat = SymptomaticTestsMat.transpose()
    ContactTraceTestsMat = ContactTraceTestsMat.transpose()
    ExtraTestsMat = ExtraTestsMat.transpose()
    Positive_SymptomaticTestsMat = Positive_SymptomaticTestsMat.transpose()
    Positive_ContactTraceTestsMat = Positive_ContactTraceTestsMat.transpose()
    Positive_ExtraTestsMat = Positive_ExtraTestsMat.transpose()

    # get standard error
    semSus = scipy.stats.sem(SusMat)
    semInf = scipy.stats.sem(InfMat)
    semCumInf = scipy.stats.sem(CumInfMat)
    semDailyInf = scipy.stats.sem(DailyInfMat)
    semnum_incub = scipy.stats.sem(num_incub)
    semAsymMat = scipy.stats.sem(AsymMat)
    semSymMat = scipy.stats.sem(SymMat)
    semRec = scipy.stats.sem(RecMat)
    semDead = scipy.stats.sem(DeadMat)
    semDailyDead = scipy.stats.sem(DailyDeadMat)
    semHosp = scipy.stats.sem(HospMat)
    sembreathMat = scipy.stats.sem(breathMat)
    semrespMat = scipy.stats.sem(respMat)
    semicuMat = scipy.stats.sem(icuMat)
    semDailyTestedMat = scipy.stats.sem(DailyTestedMat)
    semSpreaderMat = scipy.stats.sem(SpreaderMat)
    semQuarantinedMat = scipy.stats.sem(QuarantinedMat)
    semSymptomaticTestsMat = scipy.stats.sem(SymptomaticTestsMat)
    semContactTraceTestsMat = scipy.stats.sem(ContactTraceTestsMat)
    semExtraTestsMat = scipy.stats.sem(ExtraTestsMat)
    semPositive_SymptomaticTestsMat = scipy.stats.sem(Positive_SymptomaticTestsMat)
    semPositive_ContactTraceTestsMat = scipy.stats.sem(Positive_ContactTraceTestsMat)
    semPositive_ExtraTestsMat = scipy.stats.sem(Positive_ExtraTestsMat)

    # get mean
    meanSus = SusMat.mean(0)
    meanInf = InfMat.mean(0)
    meanCumInf = CumInfMat.mean(0)
    meanDailyInf = DailyInfMat.mean(0)
    meannum_incub = num_incub.mean(0)
    meanAsymMat = AsymMat.mean(0)
    meanSymMat = SymMat.mean(0)
    meanRec = RecMat.mean(0)
    meanDead = DeadMat.mean(0)
    meanDailyDead = DailyDeadMat.mean(0)
    meanHosp = HospMat.mean(0)
    meanBreath = breathMat.mean(0)
    meanResp = respMat.mean(0)
    meanICU = icuMat.mean(0)
    meanDailyTested = DailyTestedMat.mean(0)
    meanSpreader = SpreaderMat.mean(0)
    meanQuarantined = QuarantinedMat.mean(0)
    meanSymptomaticTests = SymptomaticTestsMat.mean(0)
    meanContactTraceTests = ContactTraceTestsMat.mean(0)
    meanExtraTests = ExtraTestsMat.mean(0)
    meanPositive_SymptomaticTests = Positive_SymptomaticTestsMat.mean(0)
    meanPositive_ContactTraceTests = Positive_ContactTraceTestsMat.mean(0)
    meanPositive_ExtraTests = Positive_ExtraTestsMat.mean(0)

    updateCSV2(directory + title + '_mean.csv', meanSus, meanInf, meanCumInf, meanDailyInf, meannum_incub, meanAsymMat, meanSymMat,
        meanRec, meanDead, meanDailyDead, meanHosp, meanBreath, meanResp, meanICU, meanDailyTested, meanSpreader, meanQuarantined,
        meanSymptomaticTests, meanContactTraceTests, meanExtraTests, meanPositive_SymptomaticTests, meanPositive_ContactTraceTests, meanPositive_ExtraTests)
    updateCSV2(directory + title + '_se.csv', semSus, semInf, semCumInf, semDailyInf, semnum_incub, semAsymMat, semSymMat,
        semRec, semDead, semDailyDead, semHosp, sembreathMat, semrespMat, semicuMat, semDailyTestedMat, semSpreaderMat, semQuarantinedMat,
        semSymptomaticTestsMat, semContactTraceTestsMat, semExtraTestsMat, semPositive_SymptomaticTestsMat, semPositive_ContactTraceTestsMat, semPositive_ExtraTestsMat)

    fig = plt.figure()

    plt.errorbar(range(0,length), meanSus, 1.96*semSus, label='Sus')
    plt.errorbar(range(0,length), meanInf, 1.96*semInf, label='Inf')
    plt.errorbar(range(0,length), meanRec, 1.96*semRec, label='Rec')
    plt.errorbar(range(0,length), meannum_incub, 1.96*semnum_incub, label='Exp')
    plt.errorbar(range(0,length), meanCumInf, 1.96*semCumInf, label='Total Inf')
    #plt.errorbar(range(0,length), meanDailyTested, 1.96*semDailyTestedMat, label='Daily Tested')
    #plt.errorbar(range(0,length), meanDead, 1.96*semDead, label='Dead')
    #plt.errorbar(range(0,length), meanHosp, 1.96*semHosp, label='Hospitalized')
    #plt.errorbar(range(0,length), meanDailyInf, 1.96*semDailyInf, label='Daily Infected')
    #plt.errorbar(range(0,length), meanDailyDead, 1.96*semDailyDead, label='Daily Dead')
    #plt.errorbar(range(0,length), meanAsymMat, 1.96*semAsymMat, label='Asymptomatic')
    #plt.errorbar(range(0,length), meanSymMat, 1.96*semSymMat, label='Symptomatic')
    plt.xlabel('Num Days', figure=fig)
    plt.ylabel('Num People', figure=fig)
    plt.title(title)

    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    #plt.show()
    fig.savefig(directory + title + '_SEIR_Graph.png', bbox_inches='tight')

    #maX = max(meanInf)
    #day = np.where(meanInf == maX)
    #print(str(maX) + " people infected on day " + str(day[0][0]))
    #print(len(List))  # number of files tested