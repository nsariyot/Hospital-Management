import MySQLdb


import patient
import doctor

from tabulate import tabulate

while True:

	choice = input("\n1.Register\n2.Display Records\n3.Update\n4.Delete\n5.Exit\n\n>>>  ")
	if choice == 1:
		choice = input("\n1.Patient\n2. Doctor\n3.Exit\n\n>>>  ")
		if choice ==  1:
		        while True:
		                s = patient.patient()
		                s.register()
		                choice = raw_input("Add more? [Y/n] ")
		                if choice.lower() == "y":
		                        pass
		                elif choice.lower() == "n":
		                        break
		                else:
		                        print "Please enter valid choice"
	
		elif choice ==  2:
		        while True:
		                s = doctor.doctor()
		                s.register()
		                choice = raw_input("Add more? [Y/n] ")
		                if choice.lower() == "y":
		                        pass
		                elif choice.lower() == "n":
		                        break
		                else:
		                        print "Please enter valid choice"	                
	        elif choice ==  3:
	        	break
	        else:
	                print("\nPlease enter a valid choice")
	elif choice == 2:
		choice = input("\n1.Patient\n2. Doctor\n3.Exit\n\n>>>  ")
		if choice ==  1:
		                s = patient.patient()
		                s.display()

		elif choice ==  2:
		                s = doctor.doctor()
		                s.display()
	                
	        elif choice ==  3:
		                break
		                
	        else:
	                print("\nPlease enter a valid choice")
	        
	elif choice == 3:
		choice = input("\n1.Patient\n2. Doctor\n3.Exit\n\n>>>  ")
		if choice ==  1:
		                s = patient.patient()
		                s.update()

		elif choice ==  2:
		                s = doctor.doctor()
		                s.update()
	                
	        elif choice ==  3:
		                break
		                
	        else:
	                print("\nPlease enter a valid choice")
	        
	
	elif choice == 4:
		choice = input("\n1.Patient\n2. Doctor\n3.Exit\n\n>>>  ")
		if choice ==  1:
		                s = patient.patient()
		                s.delet()

		elif choice ==  2:
		                s = doctor.doctor()
		                s.delet()
	                
	        elif choice ==  3:
		                break
		                
	        else:
	                print("\nPlease enter a valid choice")
		
	elif choice == 5:
		break
		
		
	else:
		print("\nPlease enter a valid choice")
			
		
