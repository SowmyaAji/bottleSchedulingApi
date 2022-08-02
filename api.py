# from bottle import request, response
# from bottle import post, get, put, delete
# from datetime import datetime, timedelta

# current = datetime(2022, 1, 1) # arbitrary start day
# spacing = 15
# time_lst = [f'{current + timedelta(minutes=m):%I:%M %p}' for m in range(0, (24 * 60), spacing)]

# doctors = []
# doc_schedules = []
# booked_appointments = []



# @post('/doctors')
# def create_doctor():
#     '''Handles doctor creation'''
#     data = request.json()
#     if data not in doctors:
#         doctors.append(data)
#         return { "status": 200, "msg" : f"Successfully added doctor { data['doctor_id'] }"}
        
# @get('/doctors')
# def get_all_doctors():
#     return {"Available doctors": doctors }

# @post('/schedule')
# def create_schedule():
#     data = request.json()
#     start = time_lst.index(data['start_time'])
#     end = time_lst.index(data['end_time'])
#     time_slots = time_lst[start:end]
#     date_available = data['date_available']
#     doc_schedules.append({"doctor_id": data['doctor_id'], "date_available" : date_available, "time_slots:": time_slots })
    
# @delete('/schedule/<id>')
# def update_schedule(id):
#     for schedule in doc_schedules:
#         if schedule["doctor_id"] == id:
#             doc_schedules.remove(schedule)
#             break


# @get('/schedule/<id>')
# def get_doctor_schedule(id):
#     try:
#         for schedule in doc_schedules:
#             if id == schedule['doctor_id']:
#                 return schedule
#     except Exception as e:
#         return { "error": e,  "msg" : f'we cannot find a doctor with id { id }', "available_doctors": doctors }

# @post('/appointment')
# def create_appointment():
#     data = request.json()
#     doc_id = data["doctor_id"]
#     required_slot = data["required_slot"]
#     required_date = data["required_date"]
#     formatted_date =datetime.datetime.strptime(required_date, format)
#     if (formatted_date - datetime.now()) > timedelta(hours=24):
#         for schedule in doc_schedules:
#             if doc_id == schedule['doctor_id'] and required_date == schedule['date_available'] and required_slot in schedule["time_slots"]:
#                 schedule['time_slots'].remove(required_slot)
#                 booked_appointments.append({ "doctor" : doc_id, "patient": data['patient_id'], "appointment_date": required_date, "appointment_time": required_slot })
#                 return { "status": "appointment confirmed", "date": required_date, "time" : required_slot }
#             else:
#                 return { "status": "appointment not available for that time, please book another date or time", "availability": [ i for i in doc_schedules if i['doctor_id'] == doc_id]}
#     else:
#         return { 'status': "Sorry you need to book your appointment at least 24 hours in advance. Please book another date or time",  "availability": [ i for i in doc_schedules if i['doctor_id'] == doc_id] }
