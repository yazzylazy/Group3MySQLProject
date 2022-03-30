from wtforms import Form, StringField, SelectField
class PatientSearchForm(Form):
    choices = [('Ottawa', 'Ottawa'),
               ('Toronto', 'Toronto'),
               ('Montreal', 'Montreal')]
    select = SelectField('Search for patients by branch:', choices=choices)
    search = StringField('')