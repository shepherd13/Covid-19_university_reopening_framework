import random
import sparse
import copy

def get_inPerson_classes_today(matric, day, parameters):
	inPerson_classes_today = []
	class_sizes_today = matric[day].sum(axis=0)
	for course in range(matric.shape[2]):
		if (class_sizes_today[course] <= parameters['Upper Limit Offline Class Size'] and class_sizes_today[course] > 1):
			inPerson_classes_today.append(course)
	# Find distribution of all classes
	inPerson_classes_sizes_today = [class_sizes_today[course] for course in inPerson_classes_today]
	return inPerson_classes_today, inPerson_classes_sizes_today

def distribute_tests_coursewise(matric, inPerson_classes_today, inPerson_classes_sizes_today, extra_test_capacity):
	# Distribute extra tests to each class
	tests_for_each_class = [0] * (matric.shape[2])
	class_weights = [size/sum(inPerson_classes_sizes_today) for size in inPerson_classes_sizes_today]
	for i in range(int(extra_test_capacity)):
		tests_for_each_class[random.choices(inPerson_classes_today, class_weights)[0]] += 1
	return tests_for_each_class

def distribute_tests_coursewise_on_infectability(matric, inPerson_classes_today, inPerson_classes_sizes_today, extra_test_capacity, course_infectability):
	# Distribute extra tests to each class
	tests_for_each_class = [0] * (matric.shape[2])
	class_weights = [course_infectability[course_num]/sum(course_infectability.values()) for course_num in course_infectability.keys()]
	for i in range(int(extra_test_capacity)):
		tests_for_each_class[random.choices(inPerson_classes_today, class_weights)[0]] += 1
	return tests_for_each_class

def days_since_tested(parameters, test_state, person, day):
	# check if they have been tested in last 7 days
	if len(test_state[:, person].nonzero()[1]) > 0:
		days_since_tested = day - test_state[:, person].nonzero()[1][-1]
	else:
		days_since_tested = parameters['Testing Days Gap']	# Just to continue the simulation/says ready for testing
	return days_since_tested

def run_test(matric, day, state, test_state, parameters, infectability, inPerson_people, inPerson_classes, symptomatic_classes, asymptomatic_classes):
	random_tests = 0
	random_tests_positive = 0
	# Types of test candidates
	symptomatic_tests = 0
	contact_trace_tests = 0
	extra_tests = 0
	# Positive tested candidates
	positive_symptomatic_tests = 0
	positive_contact_trace_tests = 0
	positive_extra_tests = 0
	symptomatic_classes_left = copy.deepcopy(symptomatic_classes)
	symptomatic_classes_removed = []
	test_capacity = int(parameters['Test Capacity'])

	if parameters['Test Upon Entry'] == 1 and day == 0:
		for person in range(matric.shape[1]):
			cur_state = state[day, person]
			viral_testing(day, person, cur_state, test_state, parameters)
	else:
		# symptomatic_testing
		symptomatic_testing = [person for person in range(matric.shape[1]) if state[day, person] == 3 and parameters['Students'] > person]
		for person in symptomatic_testing:
			cur_state = state[day, person]
			ts = viral_testing(day, person, cur_state, test_state, parameters)
			if ts == 1:
				positive_symptomatic_tests += 1
			symptomatic_tests += 1
			test_capacity -= 1

		# asymptomatic_testing
		if test_capacity > 0:
			if parameters['Test Type'] == 0: # Random
				# Find total offline classes
				#inPerson_classes_today, inPerson_classes_sizes_today = get_inPerson_classes_today(matric, day, parameters)
				inPerson_classes_today = inPerson_classes[day%7]
				inPerson_people_today = inPerson_people[day%7]
				if len(inPerson_classes_today) != 0:
					for i in range(int(extra_test_capacity)):
						count = 0
						while(count <= 2):
							count += 1
							#random_course = random.choice(inPerson_classes_today)
							#random_person = random.choice(matric[day,:,random_course].nonzero()[0])
							random_person = random.choice(inPerson_people_today)
							days_since_last_test = days_since_tested(parameters, test_state, random_person, day)
							if days_since_last_test >= parameters['Testing Days Gap']:
								cur_state = state[day, random_person]
								ts = viral_testing(day, random_person, cur_state, test_state, parameters)
								if ts == 1:
									random_tests_positive += 1
								random_tests += 1
								break

			elif parameters['Test Type'] == 1: # Person Degree
				# Find total offline classes
				inPerson_classes_today = inPerson_classes[day%7]
				inPerson_people_today = inPerson_people[day%7]
				if len(inPerson_classes_today) != 0:
					people_last_tested = [-1] * (matric.shape[1])
					if day >= parameters['Testing Days Gap']:
						for person_ in inPerson_people_today:
							people_last_tested[person_] = sum(test_state[day-int(parameters['Testing Days Gap']):day, person_])
					else:
						for person_ in inPerson_people_today:
							people_last_tested[person_] = sum(test_state[0:day, person_])
					course_people_infectability = {person_:infectability[person_] for person_ in inPerson_people_today if people_last_tested[person_] == 0}
					course_people_infectability = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]

					if len(course_people_infectability) >= parameters['Extra Test Capacity']:
						test_people = course_people_infectability[:int(parameters['Extra Test Capacity'])]
					else:
						test_people = course_people_infectability[:]
					for i in range(len(test_people)):
						person_, infectability_ = test_people[i]
						cur_state = state[day, person_]
						ts = viral_testing(day, person_, cur_state, test_state, parameters)
						if ts == 1:
							random_tests_positive += 1
						extra_test_capacity -= 1
						random_tests += 1

			elif parameters['Test Type'] == 2: # Random classwise degree
				# Find total offline classes
				# inPerson_classes_today = inPerson_classes[day%7]
				# inPerson_people_today = inPerson_people[day%7]
				inPerson_classes_today, inPerson_classes_sizes_today = get_inPerson_classes_today(matric, day, parameters)
				if len(inPerson_classes_today) != 0:
					tests_for_each_class = distribute_tests_coursewise(matric, inPerson_classes_today, inPerson_classes_sizes_today, extra_test_capacity)
					# Run tests
					for course in inPerson_classes_today:
						for i in range(tests_for_each_class[course]):
							count = 0
							while(count <= 2):
								count += 1
								person_ = random.choice(matric[day,:,course].nonzero()[0])
								days_since_last_test = days_since_tested(parameters, test_state, person_, day)
								if days_since_last_test >= 7:
									cur_state = state[day, person_]
									ts = viral_testing(day, person_, cur_state, test_state, parameters)
									if ts == 1:
										random_tests_positive += 1
									extra_test_capacity -= 1
									random_tests += 1
									break

			elif parameters['Test Type'] == 3: # Person Degree Classwise degree
				inPerson_classes_today, inPerson_classes_sizes_today = get_inPerson_classes_today(matric, day, parameters)
				if len(inPerson_classes_today) != 0:
					tests_for_each_class = distribute_tests_coursewise(matric, inPerson_classes_today, inPerson_classes_sizes_today, extra_test_capacity)
					# Run tests
					for course in inPerson_classes_today:
						course_people_infectability = {person_:infectability[person_] for person_ in matric[day,:,course].nonzero()[0]}
						course_people_infectability = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]
						for i in range(tests_for_each_class[course]):
							for j in range(len(course_people_infectability)):
								person_, infectability_ = course_people_infectability[j]
								days_since_last_test = days_since_tested(parameters, test_state, person_, day)
								if days_since_last_test >= 7:
									cur_state = state[day, person_]
									ts = viral_testing(day, person_, cur_state, test_state, parameters)
									if ts == 1:
										random_tests_positive += 1
									extra_test_capacity -= 1
									random_tests += 1
									break

			elif parameters['Test Type'] == 4: # Randomly pick based on their infectability
				inPerson_classes_today = inPerson_classes[day%7]
				inPerson_people_today = inPerson_people[day%7]
				if len(inPerson_classes_today) != 0:
					people_last_tested = [-1] * (matric.shape[1])
					if day >= parameters['Testing Days Gap']:
						for person_ in inPerson_people_today:
							people_last_tested[person_] = sum(test_state[day-int(parameters['Testing Days Gap']):day, person_])
					else:
						for person_ in inPerson_people_today:
							people_last_tested[person_] = sum(test_state[0:day, person_])
					course_people_infectability = {person_:infectability[person_] for person_ in inPerson_people_today if people_last_tested[person_] == 0}
					#course_people_infectability = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]
					potential_carriers = list(course_people_infectability.keys())
					carrier_infection = list(course_people_infectability.values())
					total_infection_today = sum(carrier_infection)
					for i in range(int(extra_test_capacity)):
						count = 0
						while(count <= 2):
							count += 1
							random_person = random.choices(potential_carriers, [infection_/total_infection_today for infection_ in carrier_infection])[0]
							if test_state[day, random_person] == 0:
								cur_state = state[day, random_person]
								ts = viral_testing(day, random_person, cur_state, test_state, parameters)
								if ts == 1:
									random_tests_positive += 1
								random_tests += 1
								break

			elif parameters['Test Type'] == 5:  # Person Degree (randomized) class-wise sum_infectability degree
				inPerson_classes_today, inPerson_classes_sizes_today = get_inPerson_classes_today(matric, day, parameters)
				if len(inPerson_classes_today) != 0:
					course_infectability_sums = {}
					for course in inPerson_classes_today:
						course_people_infectability = {person_: infectability[person_] for person_ in matric[day,:,course].nonzero()[0]}
						course_infectability_sums[course] = sum(course_people_infectability.values())
					tests_for_each_class = distribute_tests_coursewise_on_infectability(matric, inPerson_classes_today, inPerson_classes_sizes_today, extra_test_capacity, course_infectability_sums)
					# Run tests
					for course in inPerson_classes_today:
						course_people_infectability = {person_:infectability[person_] for person_ in matric[day,:,course].nonzero()[0]}
						course_people_infectability = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]
						course_persons = [course_people[0] for course_people in course_people_infectability]
						course_infectabilities = [course_people[1] for course_people in course_people_infectability]

						for i in range(tests_for_each_class[course]):
							for j in range(len(course_people_infectability)):
								person_ = random.choices(course_persons, [course_infectabilities_/course_infectability_sums[course] for course_infectabilities_ in course_infectabilities])[0]
								days_since_last_test = days_since_tested(parameters, test_state, person_, day)
								if days_since_last_test >= 7:
									cur_state = state[day, person_]
									ts = viral_testing(day, person_, cur_state, test_state, parameters)
									if ts == 1:
										random_tests_positive += 1
									extra_test_capacity -= 1
									random_tests += 1
									break

			elif parameters['Test Type'] == 6:		# Natural Testing
				#print("Classes to test:", len(test_classes))
				for course_ in test_classes:
					classes_left.remove(course_)
					tests_available = int(len(matric[day,:,course_].nonzero()[0]) * parameters['Test Class Fraction'])
					for i in range(tests_available):
						count = 0
						while(count <= 2):
							count += 1
							person_ = random.choice(matric[day,:,course_].nonzero()[0])
							days_since_last_test = days_since_tested(parameters, test_state, person_, day)
							if days_since_last_test >= parameters['Testing Days Gap']:
								cur_state = state[day, person_]
								ts = viral_testing(day, person_, cur_state, test_state, parameters)
								if ts == 1:
									positive_contact_trace_tests += 1
								#extra_test_capacity -= 1
								contact_trace_tests += 1
								break

			elif parameters['Test Type'] == 7:	# Natural Testing and Weighted Random selection of people
				for course_ in test_classes:
					classes_left.remove(course_)
					tests_available = int(len(matric[day,:,course_].nonzero()[0]) * parameters['Test Class Fraction'])

					potential_carriers = []
					carrier_infection = []
					#course_people_infectability = [(k,v) for k, v in sorted(course_people_infectability.items(), key=lambda item: item[1])][::-1]
					for person_ in matric[day,:,course_].nonzero()[0]:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers.append(person_)
							carrier_infection.append(infectability[person_])

					total_infection_today = sum(carrier_infection)
					for i in range(int(tests_available)):
						count = 0
						while(count <= 2):
							count += 1
							random_person = random.choices(potential_carriers, [infection_/total_infection_today for infection_ in carrier_infection])[0]
							if test_state[day, random_person] == 0:
								cur_state = state[day, random_person]
								ts = viral_testing(day, random_person, cur_state, test_state, parameters)
								if ts == 1:
									contact_trace_tests += 1
								contact_trace_tests += 1
								break

			elif parameters['Test Type'] == 8:	# Symptomatic Testing, Symptomatic Class Pool Testing, Asymptomatic Class Pool Testing
				inPerson_classes_today = inPerson_classes[day%7]
				# Symptomatic Class Pool Testing
				if test_capacity > 0 and len(inPerson_classes_today) > 0:
					# People in symptomatic classes
					symptomatic_classes_people = []
					for course_ in symptomatic_classes:
						if course_ in inPerson_classes_today:
							symptomatic_classes_left.remove(course_)
							symptomatic_classes_removed.append(course_)
							symptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							symptomatic_classes_people = list(set(symptomatic_classes_people))

					# Tests alloted to symptomatic classes
					symptomatic_class_test_requirement = int(len(symptomatic_classes_people) * parameters['Test Class Fraction'])
					if symptomatic_class_test_requirement > test_capacity:
						symptomatic_class_test_requirement = test_capacity

					# Determine infectability of people from symptomatic classes
					potential_carriers = []
					carrier_infection = []
					for person_ in symptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers.append(person_)
							carrier_infection.append(infectability[person_])

					# Test People
					total_infection_today = sum(carrier_infection)
					for i in range(int(symptomatic_class_test_requirement)):
						count = 0
						while(count <= 2):
							count += 1
							random_person = random.choices(potential_carriers, [infection_/total_infection_today for infection_ in carrier_infection])[0]
							if test_state[day, random_person] == 0:
								cur_state = state[day, random_person]
								ts = viral_testing(day, random_person, cur_state, test_state, parameters)
								if ts == 1:
									positive_contact_trace_tests += 1
								contact_trace_tests += 1
								test_capacity -= 1
								break

				# Asymptomatic Class Pool Testing
				if test_capacity > 0 and len(inPerson_classes_today) > 0:
					# People in asymptomatic classes
					asymptomatic_classes_people = []
					for course_ in asymptomatic_classes:
						if course_ in inPerson_classes_today:
							asymptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							asymptomatic_classes_people = list(set(asymptomatic_classes_people))

					# Tests alloted to symptomatic classes
					asymptomatic_class_test_requirement = test_capacity

					# Determine infectability of people from symptomatic classes
					potential_carriers = []
					carrier_infection = []
					for person_ in asymptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers.append(person_)
							carrier_infection.append(infectability[person_])

					# Test People
					total_infection_today = sum(carrier_infection)
					#print("Carriers:", len(potential_carriers),"Total Infection:",sum(carrier_infection),"Infection=1:", sum([infection_/total_infection_today for infection_ in carrier_infection]))
					for i in range(int(asymptomatic_class_test_requirement)):
						count = 0
						while(count <= 2):
							count += 1
							random_person = random.choices(potential_carriers, [infection_/total_infection_today for infection_ in carrier_infection])[0]
							if test_state[day, random_person] == 0:
								cur_state = state[day, random_person]
								ts = viral_testing(day, random_person, cur_state, test_state, parameters)
								if ts == 1:
									positive_extra_tests += 1
								extra_tests += 1
								test_capacity -= 1
								break


			elif parameters['Test Type'] == 9:	# Symptomatic Testing, Symptomatic Class Pool Testing, Asymptomatic Class Pool Testing
				inPerson_classes_today = inPerson_classes[day%7]
				# Symptomatic Class Pool Testing
				if test_capacity > 0 and len(inPerson_classes_today) > 0 and len(symptomatic_classes) > 0:
					# People in symptomatic classes
					symptomatic_classes_people = []
					for course_ in symptomatic_classes:
						if course_ in inPerson_classes_today:
							symptomatic_classes_left.remove(course_)
							symptomatic_classes_removed.append(course_)
							symptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							symptomatic_classes_people = list(set(symptomatic_classes_people))

					# Tests alloted to symptomatic classes
					#symptomatic_class_test_requirement = int(len(symptomatic_classes_people) * parameters['Test Class Fraction'])
					#if symptomatic_class_test_requirement > test_capacity:
					#	symptomatic_class_test_requirement = test_capacity

					# Determine infectability of people from symptomatic classes
					potential_carriers_sym = []
					carrier_infection_sym = []
					for person_ in symptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers_sym.append(person_)
							carrier_infection_sym.append(infectability[person_])
					total_infection_today_sym = sum(carrier_infection_sym)
					#print("total symptomatic infection:", total_infection_today_sym)


					# People in asymptomatic classes
					asymptomatic_classes_people = []
					for course_ in asymptomatic_classes:
						if course_ in inPerson_classes_today:
							asymptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							asymptomatic_classes_people = list(set(asymptomatic_classes_people))

					# Tests alloted to symptomatic classes
					#asymptomatic_class_test_requirement = test_capacity

					# Determine infectability of people from symptomatic classes
					potential_carriers_asym = []
					carrier_infection_asym = []
					for person_ in asymptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers_asym.append(person_)
							carrier_infection_asym.append(infectability[person_])
					total_infection_today_asym = sum(carrier_infection_asym)
					#print("total asymptomatic infection:", total_infection_today_asym)


					# Test People
					sym_weight = parameters['Symptomatic Class Tests Weight']
					asym_weight = parameters['Asymptomatic Class Tests Weight']
					total_weight = sym_weight + asym_weight
					for i in range(test_capacity):
						count = 0
						while(count <= 2):
							count += 1
							if (random.choices([0, 1], [sym_weight/total_weight, asym_weight/total_weight])[0] == 0):
								if total_infection_today_sym > 0:
									random_person = random.choices(potential_carriers_sym, [infection_/total_infection_today_sym for infection_ in carrier_infection_sym])[0]
									if test_state[day, random_person] == 0:
										cur_state = state[day, random_person]
										ts = viral_testing(day, random_person, cur_state, test_state, parameters)
										if ts == 1:
											positive_contact_trace_tests += 1
										contact_trace_tests += 1
										break
							else:
								if total_infection_today_asym > 0:
									random_person = random.choices(potential_carriers_asym, [infection_/total_infection_today_asym for infection_ in carrier_infection_asym])[0]
									if test_state[day, random_person] == 0:
										cur_state = state[day, random_person]
										ts = viral_testing(day, random_person, cur_state, test_state, parameters)
										if ts == 1:
											positive_extra_tests += 1
										extra_tests += 1
										break

			elif parameters['Test Type'] == 10:	# Symptomatic Testing, Symptomatic Class Pool Testing, Asymptomatic Class Pool Testing
				inPerson_classes_today = inPerson_classes[day%7]
				# Symptomatic Class Pool Testing
				if test_capacity > 0 and len(inPerson_classes_today) > 0 and len(symptomatic_classes) > 0:
					# People in symptomatic classes
					symptomatic_classes_people = []
					for course_ in symptomatic_classes:
						if course_ in inPerson_classes_today:
							symptomatic_classes_left.remove(course_)
							symptomatic_classes_removed.append(course_)
							symptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							symptomatic_classes_people = list(set(symptomatic_classes_people))

					# Determine infectability of people from symptomatic classes
					potential_carriers_sym = []
					for person_ in symptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers_sym.append(person_)


					# People in asymptomatic classes
					asymptomatic_classes_people = []
					for course_ in asymptomatic_classes:
						if course_ in inPerson_classes_today:
							asymptomatic_classes_people.extend(matric[day,:,course_].nonzero()[0])
							asymptomatic_classes_people = list(set(asymptomatic_classes_people))

					# Determine infectability of people from symptomatic classes
					potential_carriers_asym = []
					for person_ in asymptomatic_classes_people:
						days_since_last_test = days_since_tested(parameters, test_state, person_, day)
						if days_since_last_test >= parameters['Testing Days Gap']:
							potential_carriers_asym.append(person_)

					# Test People
					sym_weight = parameters['Symptomatic Class Tests Weight']
					asym_weight = parameters['Asymptomatic Class Tests Weight']
					total_weight = sym_weight + asym_weight
					for i in range(test_capacity):
						count = 0
						while(count <= 2):
							count += 1
							if (random.choices([0, 1], [sym_weight/total_weight, asym_weight/total_weight])[0] == 0):
								if len(potential_carriers_sym) > 0:
									random_person = random.choice(potential_carriers_sym)
									if test_state[day, random_person] == 0:
										cur_state = state[day, random_person]
										ts = viral_testing(day, random_person, cur_state, test_state, parameters)
										if ts == 1:
											positive_contact_trace_tests += 1
										contact_trace_tests += 1
										break
							else:
								if len(potential_carriers_asym) > 0:
									random_person = random.choice(potential_carriers_asym)
									if test_state[day, random_person] == 0:
										cur_state = state[day, random_person]
										ts = viral_testing(day, random_person, cur_state, test_state, parameters)
										if ts == 1:
											positive_extra_tests += 1
										extra_tests += 1
										break

				#print("Day:", day, "Random Tests:", random_tests)#, "Random Tests Positive:", random_tests_positive)
	return symptomatic_classes_left, symptomatic_classes_removed, symptomatic_tests, contact_trace_tests, extra_tests, positive_symptomatic_tests, positive_contact_trace_tests, positive_extra_tests


def viral_testing(day, person, cur_state, test_state, parameters):
	if cur_state == 0:
		test_state[day, person] =  random.choices([-1, 1], [1.0 - parameters['False Positive Rate'], parameters['False Positive Rate']])[0]

	elif cur_state == 1:
		#test_state[day, person] =  random.choices([0, 1], [1.0 - parameters['False Positive Rate'], parameters['False Positive Rate']])[0]
		test_state[day, person] =  random.choices([-1, 1], [parameters['False Negative Rate'], 1.0 - parameters['False Negative Rate']])[0]

	elif cur_state == 2:
		test_state[day, person] =  random.choices([-1, 1], [parameters['False Negative Rate'], 1.0 - parameters['False Negative Rate']])[0]

	elif cur_state == 3:
		test_state[day, person] =  random.choices([-1, 1], [parameters['False Negative Rate'], 1.0 - parameters['False Negative Rate']])[0]

	elif cur_state == 9:
		test_state[day, person] =  random.choices([-1, 1], [parameters['False Negative Rate'], 1.0 - parameters['False Negative Rate']])[0]

	return test_state[day, person]

def antibody_testing():
	pass