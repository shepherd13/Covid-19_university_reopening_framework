main.py:
	file you need to run
	line 300 set how many processes you want at a time, 10 is the max on my 6 core 12 thread machine that still allows me to use other applications without lag
	line 333 set how many total runs you want generated
	line 336 set what template file you want
	if code having issue comment line 323 and uncomment 322, prevents running in parallel
	Currently results are only for students or only for professors, networks are combined together regardless
	
airborne.py:
	airborneProb returns the probability using the wells-riley equation
	diffProb returns the probability with the differentiate wells-riley equation
	they take same inputs, only default is pulmonary ventilation rate of 0.48
	
disease_progression.py:
	handle disease progression
	takes different progression rates for the first and second network
	
surface_transfer.py:
	surface infection transfer score model that decays daily, commented out in main currently
	
MeanSE.py
	find means and standard error and exports them to a csv, generates a SEIR graph
	
template.txt:
	simulation gets parameters from this file (or whatever the file input into sim is called). Can add whatever following this format.
	format: "name": number or string
	main takes template and converts to list, so if you add line "Temp: 15" this can be accessed by parameters['Temp']
	
	Output Directory - name of folder you want to generate, simulation will not overwrite a non empty file with same name
	Quant Rate - Quantum production rate for disease
	Vent Rate - Room ventilation rate
	Density - Students per sq ft
	Mask Rate - mask rate for people in the first network
	Mask Efficiency - mask efficiency for people in the first network
	Mask Rate 2 - mask rate for people in the second network
	Mask Efficiency 2 - mask efficiency for people in the second network
	Class Mode - set to 1 if want to do airborne transfer
	Professor Mode - decides if you want results for students (0) or professors (1), sim does find results for both but runs sims for both
	Network - tensor, currently the student tensor
	Courses - CSV for course listing with start times, end times and class sizes
	Other Network - second tensor, currently professor tensor
	Asymptomatic Rate - rate people are symptomatic, got number from included UMN SPH + MN DOH model
	
	# students
	Infectious Death Rate - rate non-hospitalized infectious death for students, got number from included UMN SPH + MN DOH model (based on age ranges)
	Hospitalization Rate - rate of hospitalization for students, got number from included UMN SPH + MN DOH model (based on age ranges)
	Hospitalization Death Rate - rate hospitalized death for students, got number from included UMN SPH + MN DOH model (based on age ranges)
	Breath Rate - rate which students experience shortness of breath (Lancet model)
	Breath Death Rate - just have been using same rate for hospitalized
	Respirator Rate - rate which students get put on respirator (Lancet model)
	Respirator Death Rate - just have been using same rate for icu
	ICU Rate - rate of icu for hospitalized students, got number from included UMN SPH + MN DOH model (based on age ranges)
	ICU Death Rate - rate of icu  death for icu students, got number from included UMN SPH + MN DOH model (based on age ranges)
	
	# professors, same concepts just higher numbers due to higher age groups
	Infectious Death Rate 2: 0.01544444444
	Hospitalization Rate 2: 0.3127888889
	Hospitalization Death Rate 2: 0.03578888889
	Breath Rate 2: 0.50
	Breath Death Rate 2: 0.03578888889
	Respirator Rate 2: 0.20
	Respirator Death Rate 2: 0.3575
	ICU Rate 2: 0.2436111111
	ICU Death Rate 2: 0.3575
	
	
	"Individual infectiousness is assumed to be variable, described by a gamma distribution with mean 1 and shape parameter 0.25." - Imperial Report
	Infectiousness Mean: 1 
	Infectiousness Shape: 0.25
	
	"The survival time of the virus on surfaces and in air is exponentially distributed with means, 3 days and 3 hours respectively." - NEJM
	Mean Decay Length: 72
	
	
	Incubation Mean: 5.2 - average length of incubation in days, from UMN SPH + MN DOH model
	Infectious Mean: 7.8 - average length of infectiousness in days, from UMN SPH + MN DOH model
	
	Leave Infection Rate: 0.80 - rate of leaving infection when visiting a location
	Symptomatic Infection: 1.50 - rate which symptomatic people leave more infection
	Symptomatic Quarantine Rate: 1.00 - rate which symptomatic people self quarantine
	
	# fram Lancet report
	Hospitalization Median: 7
	Hospitalization Lower Range: 4
	Hospitalization Upper Range: 8
	Breath Median: 8
	Breath Lower Range: 5
	Breath Upper Range: 13
	Respirator Median: 9
	Respirator Lower Range: 8
	Respirator Upper Range: 14
	ICU Median: 10
	ICU Lower Range: 8
	ICU Upper Range: 17
	
	# from UMN SPH + MN DOH model, mean length in days. Used in gamma distributions.
	Hospitalization Length Mean: 11
	ICU Length Mean: 8
	
	# quarantine parameters
	Quarantine Type: None
	Quarantine File: None
	Quarantine Percent: 0
	Quarantine Length: 0
	Quarantine Start Day: 0
	Quarantine Object: None
	
	# token parameters, set to -1  (or any negative) when not using
	Tokens Per Person: -1
	Token Policy Length: 3
	Token Policy Start: 1000000
	Token Policy End: 1000000
	
	# lockdown compliance policies (set to 0.00 when not using or a large start)
	Stay Home Compliance 1: 0.00
	Location Max Capacity 1: 1.00
	Policy 1 Start: 1000000
	Stay Home Compliance 2: 0.00
	Location Max Capacity 2: 1.00
	Policy 2 Start: 1000000

Testing:
	Test Capacity: 1000
	Test Upon Entry: 1						# 0 off / 1 on
	Symptomatic False Positive Rate: 0.001
	Symptomatic False Negative Rate: 0.03
	Asymptomatic False Positive Rate: 0.001
	Asymptomatic False Negative Rate: 0.03
	Initial Infected Population: 0.01		# percent of population
	Contact Tracing: 0						# 0 off / 1 on
	Quarantined Contact Traced: 10 			# Total people contact traced for each positive test
	Outside Transmission Rate: 0.05			# 5 percent chance of outside transmission

		
Useful things:
	parameter calibration with UMN SPH and UMN DOH data: https://docs.google.com/spreadsheets/d/19-3JzZC3Lt4vEiZ79SDLpiHgLZsO3SaJ_Ji-sw6Myjw/edit#gid=0
	airborne infection model links: https://docs.google.com/document/d/1wi7k19EDexWKsRZrrNnpOsEdIa5qtR-CcSSo8niViSw/edit
	figures and references from NSF proposal: https://docs.google.com/presentation/d/1uy0V56G_JBgaFg80Y3iDTeIuc_OSsHacR3WR4CNCalA/edit#slide=id.g843b06f1fd_0_0
