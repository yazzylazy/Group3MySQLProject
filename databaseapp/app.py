from flask import *
from flaskext.mysql import MySQL
import random, string

app = Flask(__name__)
mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'b559517d77ae6e'
app.config['MYSQL_DATABASE_PASSWORD'] = '74499144'
app.config['MYSQL_DATABASE_DB'] = 'heroku_a9a58dad9c5e526'
app.config['MYSQL_DATABASE_HOST'] = 'us-cdbr-east-05.cleardb.net'
mysql.init_app(app)

_name = ''
_password = ''
_role = ''


@app.route('/viewappointments', methods=['GET', 'POST'])
def appointmentview():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointment where appointmentstatus != 'cancelled'")
        userslist = cursor.fetchall()
        return render_template('appointments.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/viewappointments2', methods=['GET', 'POST'])
def appointmentview2():
    try:
        global _name
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointment where appointmentstatus != 'cancelled' and eid = %s", _name)
        userslist = cursor.fetchall()
        return render_template('appointments2.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/viewappointments3', methods=['GET', 'POST'])
def appointmentview3():
    try:
        global _name
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM appointment where pid = %s", _name)
        userslist = cursor.fetchall()
        return render_template('appointments3.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route("/updateappointment",methods=["POST","GET"])
def updateappointment():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        if request.method == 'POST':
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form['id']
             
            if field == 'employeeid':
               sql = "UPDATE appointment SET eid=%s WHERE appointmentid=%s"
            if field == 'appointmentdate':        
                sql = "UPDATE appointment SET appointmentdate=%s WHERE appointmentid=%s"
            if field == 'starttime':        
                sql = "UPDATE appointment SET starttime=%s WHERE appointmentid=%s"
            if field == 'endtime':        
                sql = "UPDATE appointment SET endtime=%s WHERE appointmentid=%s"
            if field == 'appointmenttype':        
                sql = "UPDATE appointment SET appointmenttype=%s WHERE appointmentid=%s"
            if field == 'appointmentstatus':        
                sql = "UPDATE appointment SET appointmentstatus=%s WHERE appointmentid=%s"
            if field == 'roomnum':        
                sql = "UPDATE appointment SET roomnumber=%s WHERE appointmentid=%s"
            if field == 'invoiceid':        
                sql = "UPDATE appointment SET invoiceid=%s WHERE appointmentid=%s"
 
            data = (value, editid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()



@app.route('/editpatients', methods=['GET', 'POST'])
def patientinfo():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM userinformation where UiD in (select uid from user where role = "patient") ')
        userslist = cursor.fetchall()
        return render_template('patientinfo.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/patientrecord', methods=['GET', 'POST'])
def patientinfo2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select pid, fName, mName, lName, gender, dateofbirth, details from record,userinformation where record.pid = userinformation.uid')
        userslist = cursor.fetchall()
        return render_template('patientrecord.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()

@app.route('/patientrecord2', methods=['GET', 'POST'])
def patientinfo3():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute('select pid, fName, mName, lName, gender, dateofbirth, details from record,userinformation where record.pid = userinformation.uid and record.pid =%s', _name)
        userslist = cursor.fetchall()
        return render_template('patientrecord2.html',userslist=userslist)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()





@app.route("/update2",methods=["POST","GET"])
def update2():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        if request.method == 'POST':
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form['id']
             
            if field == 'details':
               sql = "UPDATE record SET details=%s WHERE pid=%s"
 
            data = (value, editid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()



@app.route("/update",methods=["POST","GET"])
def update():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        if request.method == 'POST':
            field = request.form['field'] 
            value = request.form['value']
            editid = request.form['id']
             
            if field == 'address':
               sql = "UPDATE userinformation SET address=%s WHERE uid=%s"
            if field == 'city':        
                sql = "UPDATE userinformation SET city=%s WHERE uid=%s"
            if field == 'province':        
                sql = "UPDATE userinformation SET province=%s WHERE uid=%s"
            if field == 'fname':        
                sql = "UPDATE userinformation SET fname=%s WHERE uid=%s"
            if field == 'mname':        
                sql = "UPDATE userinformation SET mname=%s WHERE uid=%s"
            if field == 'lname':        
                sql = "UPDATE userinformation SET lname=%s WHERE uid=%s"
            if field == 'dob':        
                sql = "UPDATE userinformation SET dateofbirth=%s WHERE uid=%s"
            if field == 'phone':        
                sql = "UPDATE userinformation SET phonenumber=%s WHERE uid=%s"
            if field == 'gender':        
                sql = "UPDATE userinformation SET gender=%s WHERE uid=%s"
            if field == 'email':        
                sql = "UPDATE userinformation SET email=%s WHERE uid=%s"
            if field == 'ssn':        
                sql = "UPDATE userinformation SET ssn=%s WHERE uid=%s"
 
            data = (value, editid)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            success = 1
        return jsonify(success)
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()


@app.route('/logout')
def logout():
    return redirect('/')


@app.route("/receptionistlogin")
def receptionistlogin():
    return render_template('receptionistlogin.html')


@app.route("/patientlogin")
def patientlogin():
    return render_template('patientlogin.html')

@app.route("/dentistlogin")
def dentistlogin():
    return render_template('dentistlogin.html')


@app.route("/")
def main():
	return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/addappointment')
def addappointment():
    return render_template('appointmentadd.html')

@app.route('/requestappointment')
def requestappointment():
    return render_template('requestappointment.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/validatelogin',methods=['POST'])
def validatelogin():
    # read the posted values from the UI
    global _name
    _name = request.form['username']
    _password = request.form['password'] 
    # validate the received values
    if _name and _password:
        print(_name)
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('login',(_name,_password))
        data = cursor.fetchall()
        if str(data[0]) == "(1, 'Patient')":
            conn.commit()
            _role = 'Patient'
            return redirect('/patientlogin')
        elif str(data[0]) == "(1, 'Dentist')":
            conn.commit()
            _role = 'Dentist'
            return redirect('/dentistlogin')
        elif str(data[0]) == "(1, 'Receptionist')":
            conn.commit()
            _role = 'Receptionist'
            return redirect('/receptionistlogin')
        else:
            return json.dumps({'error':'Please ensure your are inputting the correct username and password (case sensitive)!'}),  {"Refresh": "2; /"}
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/api/signup',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _role = 'Patient'
    _password = request.form['inputPassword'] 
    _address = request.form['inputAddress']
    _city = request.form['inputCity']
    _province = request.form['inputProvince']
    _fName = request.form['inputfName']
    _mName = request.form['inputmName']
    _lName = request.form['inputlName']
    _dateOfBirth = request.form['inputDateOfBirth']
    _phoneNumber = request.form['inputPhoneNumber']
    _gender = request.form['inputGender']
    _email = request.form['inputEmail']
    _ssn = request.form['inputSSN']
    # validate the received values
    if _name and _email and _password and _role and _address and _city and _province and _fName and _mName and _lName and _dateOfBirth and _phoneNumber and _gender and _email and _ssn:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('createUser',(_name,_role,_password, _address, _city, _province, _fName, _mName, _lName, _dateOfBirth, _phoneNumber, _gender, _email, _ssn))
        sql = (_name, _name, _name)
        sql2 = (_name,_name)
        cursor.execute("insert into patient(pid,uid,record) values(%s,%s,%s)",sql)
        cursor.execute("insert into record(recordid, pid) values(%s,%s)", sql2)
        data = cursor.fetchall()
        if len(data) == 0:
            conn.commit()
            return redirect('/editpatients')
        else:
            return json.dumps({'error':str(data[0])}), {"Refresh": "2; /receptionistlogin"}
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'}), {"Refresh": "2; /receptionistlogin"}


@app.route('/api/addappointment',methods=['POST'])
def appointmentadder():
    _appointmentID = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    # read the posted values from the UI
    _pid = request.form['inputPID']
    _eid = request.form['inputEID']
    _appointmentdate = request.form['inputAppointmentDate'] 
    _starttime = request.form['inputStartTime']
    _endtime = request.form['inputEndTime']
    _appointmenttype = request.form['inputAppointmentType']
    _appointmentstatus = request.form['inputAppointmentStatus']
    _roomnumber = request.form['inputRoomNumber']
    _invoiceid = request.form['inputInvoiceID']
    # validate the received values
    if _pid and _eid and _appointmentdate and _starttime and _endtime and _appointmenttype and _appointmentstatus and _roomnumber and _invoiceid:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = (_appointmentID,_pid,_eid,_appointmentdate,_starttime,_endtime,_appointmenttype,_appointmentstatus,_roomnumber,_invoiceid)
        cursor.execute('insert into appointment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', sql)
        conn.commit()
        return redirect('/viewappointments')
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'}), {"Refresh": "2; /receptionistlogin"}

@app.route('/api/requestappointment',methods=['POST'])
def requestappointment2():
    global _name
    _appointmentID = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    # read the posted values from the UI
    _pid = _name
    _eid = "pending"
    _appointmentdate = request.form['inputAppointmentDate'] 
    _starttime = request.form['inputStartTime']
    _endtime = "pending"
    _appointmenttype = "pending"
    _appointmentstatus = "not approved yet"
    _roomnumber = "pending"
    _invoiceid = "pending"
    # validate the received values
    if _appointmentdate and _starttime:
        conn = mysql.connect()
        cursor = conn.cursor()
        sql = (_appointmentID,_pid,_eid,_appointmentdate,_starttime,_endtime,_appointmenttype,_appointmentstatus,_roomnumber,_invoiceid)
        cursor.execute('insert into appointment values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', sql)
        conn.commit()
        return redirect('/viewappointments3')
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'}), {"Refresh": "2; /patientlogin"}


if __name__ == "__main__":
	app.run()