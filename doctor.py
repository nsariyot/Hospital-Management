import MySQLdb
from tabulate import tabulate



class doctor(object):
	
	def __init__(self):
		self.columnname = []
		self.entries = None
		self.db = MySQLdb.connect("localhost","root","Ishant1998","hospital1" )
		self.cursor = self.db.cursor()
		
		
	def display(self):
        	sql = "desc doctor"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			self.columnname.append(x[0])
		sql = "desc employee"
		self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		for x in self.entries:
			if x[0] not in self.columnname:
				self.columnname.append(x[0])
                sql = "select * from doctor natural join employee"
                self.cursor.execute(sql)
                self.entries = self.cursor.fetchall()
                print tabulate(self.entries, self.columnname, tablefmt='psql')
                
                self.columname = []
                
        def register(self):
        
        	empid = raw_input("Enter employee ID:-	")
        	sql = "select * from doctor where emp_id = %s"%(str(empid))
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			print "Employee already registered.."
		else:
			name = raw_input("Enter Name:-	")
			salary = raw_input("Enter Salary:-	")
			gender = raw_input("Enter Gender:-	")
			spec = raw_input("Enter Specialization:-	")
						
			sql = "insert into employee values(%s,%s,%s,%s)"%(str(empid),('"'+str(gender)+'"'),('"'+str(name)+'"'),(str(salary)))
			
			if self.cursor.execute(sql):
				self.db.commit()
				sql = "insert into doctor values(%s,%s,%s)"%(str(empid),('"'+str(spec)+'"'),str(empid))
				if self.cursor.execute(sql):
					print "Successfully Registered.."
					self.db.commit()
					
	def delet(self):
		empid = raw_input("Enter employee ID:-	")
        	sql = "select * from doctor where emp_id = %s"%(str(empid))
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			sql = "delete from doctor where d_id = %s"%(str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		sql = "delete from employee where emp_id = %s"%(str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		
        		print "Successfully deleted.."
        		
        	else:
        		print "Employee not found with ID:- %s"%(str(empid))
        		
        		
        def update(self):
		empid = raw_input("Enter Employee ID:-	")
        	sql = "select * from employee where emp_id = %s"%(str(empid))
        	
        	self.cursor.execute(sql)
		self.entries = self.cursor.fetchall()
		print self.entries
		if len(list(self.entries)) != 0:
			name = raw_input("Enter New Name:-	")
			salary = raw_input("Enter New Salary:-	")
			sql = "update employee set name = '%s', salary = '%s' where emp_id = %s"%(str(name),str(salary),str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		spec = raw_input("Enter New Spqcialization:-	")
        		sql = "update doctor set specialisation = '%s' where d_id = %s"%(str(spec),str(empid))
        		self.cursor.execute(sql)
        		self.db.commit()
        		
        		print "Successfully Updated.."
        		
        	else:
        		print "Employee not found with ID:- %s"%(str(empid))
        		
        		
        		
        		
		
		
		
			        

