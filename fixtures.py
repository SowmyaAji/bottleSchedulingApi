# post request to create doctor
{ "doctor_id": 1 } # we can add whatever we want, first name, last name,speciality etc, but for now we only need an id

# get request to see doctor schedule
/doctors/1 # successful
/doctors/2 # error message

# post request to create appointment
{ "doctor_id": 1, "required_date": 2022-08-01, "required_slot": "09:00 AM" }