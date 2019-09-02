import MySQLdb
from tabulate import tabulate



class patient(object):
	
	def __init__(self):
		self.columnname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Ishant1998","hospital1" )
		self.cursor = self.db.cursor()
		
		
	def display(self):
        	sql = "desc patient"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		sql = "desc medical_record"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			if x[0] not in self.columnname:
				self.columnname.append(x[0])
                sql = "select * from patient natural join medical_record"
                self.cursor.execute(sql)
                self.entries = self.cursor.fetchall()
                print tabulate(self.entries, self.columnname, tablefmt='psql')
                
                self.columname = []
                
        def register(self):
        
        	empid = raw_input("Enter patient ID:-	")
        	sql = "select * from patient where p_id = %s"%(str(empid))
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			print "Patient already registered.."
		else:
			name = raw_input("Enter Name:-	")
			address = raw_input("Enter Address:-	")
			disease = raw_input("Enter Disease:-	")
			roomno = raw_input("Enter Room No:-	")
			
						
			sql = "insert into patient values(%s,%s,%s)"%(str(empid),('"'+str(name)+'"'),('"'+str(address)+'"'))
			
			if self.cursor.execute(sql):
				self.db.commit()
				sql = "insert into medical_record values(%s,%s,%s,%s)"%(str(empid),('"'+str(disease)+'"'),str(roomno),str(empid))
				if self.cursor.execute(sql):
					print "Successfully Registered.."
					self.db.commit()
					
	def delet(self):
		empid = raw_input("Enter patient ID:-	")
        	sql = "select * from patient where p_id = %s"%(str(empid))
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			sql = "delete from medical_record where p_id = %s"%(str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		
        		sql = "delete from patient where p_id = %s"%(str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		
        		print "Successfully deleted.."
        		
        	else:
        		print "Employee not found with ID:- %s"%(str(empid))
					
	def update(self):
		empid = raw_input("Enter patient ID:-	")
        	sql = "select * from patient where p_id = %s"%(str(empid))
        	
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			disease = raw_input("Enter New Disease:-	")
			roomno = raw_input("Enter New Room No:-	")
			sql = "update medical_record set disease = '%s', room_no = '%s' where p_id = %s"%(str(disease),str(roomno),str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		name = raw_input("Enter New Name:-	")
			address = raw_input("Enter New Address:-	")
        		sql = "update patient set name = '%s', address = '%s' where p_id = %s"%(str(name),str(address),str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		
        		print "Successfully Updated.."
        		
        	else:
        		print "Employee not found with ID:- %s"%(str(empid))
						

