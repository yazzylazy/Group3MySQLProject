from flask import *
from flaskext.mysql import MySQL
from forms import PatientSearchForm

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


@app.route('/editpatients', methods=['GET', 'POST'])
def patientinfo():
    search = PatientSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('patientinfo.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = db_session.query(Ottawa)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)



@app.route('/logout')
def logout():
    return redirect('/')


@app.route("/receptionistlogin")
def receptionistlogin():
    return render_template('receptionistlogin.html')

@app.route("/")
def main():
	return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/validatelogin',methods=['POST'])
def validatelogin():
    # read the posted values from the UI
    _name = request.form['username']
    _password = request.form['password'] 
    # validate the received values
    if _name and _password:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('login',(_name,_password))
        data = cursor.fetchall()
        if str(data[0]) == "(1, 'Patient')":
            conn.commit()
            _role = 'Patient'
            return json.dumps({'message':'Patient signed in successfully !'})
        elif str(data[0]) == "(1, 'Dentist')":
            conn.commit()
            _role = 'Dentist'
            return json.dumps({'message':'Dentist signed in successfully !'})
        elif str(data[0]) == "(1, 'Receptionist')":
            conn.commit()
            _role = 'Receptionist'
            return redirect('/receptionistlogin')
        else:
            return json.dumps({'error':'Please ensure your are inputting the correct username and password (case sensitive)!'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


@app.route('/api/signup',methods=['POST'])
def signUp():
    # read the posted values from the UI
    _name = request.form['inputName']
    _role = request.form['inputRole']
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
    	data = cursor.fetchall()
    	if len(data) == 0:
    		conn.commit()
    		return json.dumps({'message':'User created successfully !'})
    	else:
    		return json.dumps({'error':str(data[0])})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


if __name__ == "__main__":
	app.run()