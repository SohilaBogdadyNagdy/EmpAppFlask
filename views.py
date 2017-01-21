from app import app ,mysql
from flask  import render_template , redirect ,request
from  forms import NewempForm 
from  forms import RemoveForm
@app.route('/')
@app.route('/index')
def index():

	"""list alll  emp   view """
	print ("index view ")
	cursor  = mysql.connect().cursor()
	print(cursor)
	cursor.execute("select * from EMP")
	data = cursor.fetchall ()
	print (data)
    #now pass  data  to  our template 
	
	return   render_template('home.html',title="list",empdata=data)
	#return "<html><head><title>Home page</title></head><body><h1><center>Employee's application flask app <h3>"+user['name']+"</h3></center></h1></body></html>"
    #("<html><head><title>Index page<title></head></html>")
    # '''<html><head><title>Home Page</title></head><body><h1>Hello, ''' + user['name'] + '''</h1></body></html> '''



    
@app.route ('/add',methods =['POST','GET'])
def newEMp ():
	"""add  new emp  view """
	title = "new employee  page"
	print ("newEmp view method ")
	empform = NewempForm()
	print (empform.validate_on_submit())
	print (empform)
	if (empform.validate_on_submit()):
		print ("***form valiation true  **********")
		#save  user data 

		fn = empform.first_name.data
		ln = empform.last_name.data
		cl = empform.career_level.data 
		cur = mysql.connect().cursor() 
		mysql.connect().autocommit(False)
		try:
			con = mysql.connect()
			cur =con.cursor()
			cur.execute ("insert into EMP ( firstname ,lastname ,careerlevel) values (%s , %s , %s) ", (fn,ln,cl))
			con.commit()
			con.close ()
		except Exception as e:
			print(e)
		   	print ("-----sql operation not execute --------")
		#print ("now we need  to save  data  in db")
		return  redirect('/index')

	else :
		print ("-----emp form  not validated yet ----")
	return render_template('add.html',title='new emp',empform=empform)	
	

		





@app.route ('/remove',methods=['get'])
def deleEmp ():
	rform =RemoveForm ()
	print  ("creation instance from  remove employee  form ")
	#if rform.validate_on_submit():
        #return redirect('/success')
	#	print ("form submittedand and validated ")
	#	id = rform.empid.data
	#	print (id)
	#	print ("use coming id to  remove user from db")
    #		try :
	#		pass
	#	except :
	#		print ("++++")
			



	#else :
	#	print ("not validated ")
	try :
		if (request.args.get('empid')):

			print ("----------found  value---------------")
			del_id = request.args.get('empid')
			print (del_id)
			##########################delete record from FLASKDB EMP TABLE ------------------------------------------
			try:
				print ("")
				newcon = mysql.connect()
				newcur=newcon.cursor ()
				#newcur.execute("DELETE FROM 'EMP' WHERE empid =1")
				#newcon.commit()
				#newcon.close()
				delstatmt = "DELETE FROM EMP WHERE empid = %s "
				print(type(del_id))
				print(delstatmt%tuple(del_id))
				newcur.execute(delstatmt, (del_id))
				newcon.commit()
				return redirect('/')
			except Exception as error :
				print ("error in delete  record from  db ",error)
			finally :
				newcon.close ()
				newcur.close()
				
			    


		
	except Exception as e :

		print (e)
			


		
	return  render_template('rem.html', title="remove" , form=rform )











