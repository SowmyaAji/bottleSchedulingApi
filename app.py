from datetime import datetime, timedelta
from bottle import post, get, put, delete, route
from bottle import request, response
from bottle import Bottle, route, run


current = datetime(2022, 1, 1)  # arbitrary start day
spacing = 15
time_lst = [
    f'{current + timedelta(minutes=m):%I:%M %p}' for m in range(0, (24 * 60), spacing)]


doctors = []
doc_schedules = []
booked_appointments = []


@get('/')
def index():
    return {"msg": "Hello to the Doctor Appointments App!"}


@post('/doctors')
def create_doctor():
    '''Handles doctor creation'''
    new_doctor = {"id": request.json.get("id")}
    if new_doctor not in doctors:
        doctors.append(new_doctor)
        return {"status": 200, "msg": f"Successfully added doctor { new_doctor }"}


@get('/doctors')
def get_all_doctors():
    return {"Available doctors": doctors}


@post('/schedule')
def create_schedule():
    start = time_lst.index(request.json.get("start_time"))
    end = time_lst.index(request.json.get("end_time"))
    print("start: ", start, "end: ", end)
    time_slots = time_lst[start:end]
    print("time slots: ", time_slots)
    date_available = request.json.get('date_available')
    day_schedule = {"doctor_id": request.json.get(
        'doctor_id'), "date_available": date_available, "time_slots": time_slots}
    doc_schedules.append(
        day_schedule)
    return {"status": 200, "msg": f"Successfully created schedule { day_schedule }"}


@delete('/schedule/<id>')
def delete_schedule(id):
    for schedule in doc_schedules:
        if schedule["doctor_id"] == id:
            doc_schedules.remove(schedule)
            break


@get('/schedule/<id>')
def get_doctor_schedule(id):
    schedules = []
    try:
        for schedule in doc_schedules:
            if schedule.get('doctor_id') == id:
                schedules.append(schedule)
        return {f'doctor { id }': schedules}
    except Exception as e:
        return {"error": e,  "msg": f'we cannot find a doctor with id { id }', "available_doctors": doctors}


@post('/appointment')
def create_appointment():
    data = request.json
    doc_id = data["doctor_id"]
    required_slot = data["required_slot"]
    required_date = data["required_date"]
    formatted_date = datetime.strptime(required_date, '%Y-%m-%d').date()
    print("Formatted date: ", formatted_date)
    today = datetime.now().date()
    print("Today: ", today)
    if (formatted_date - today) > timedelta(hours=24):
        print("yep")
        for schedule in doc_schedules:
            if doc_id == schedule['doctor_id'] and required_date == schedule['date_available'] and required_slot in schedule["time_slots"]:
                schedule['time_slots'].remove(required_slot)
                booked_appointments.append(
                    {"doctor": doc_id, "patient": data['patient_id'], "appointment_date": required_date, "appointment_time": required_slot})
                return {"status": "appointment confirmed", "date": required_date, "time": required_slot}
            else:
                return {"status": "appointment not available for that time, please book another date or time", "availability": doc_schedules}
    else:
        return {'status': "Sorry you need to book your appointment at least 24 hours in advance. Please book another date or time",  "availability": [i for i in doc_schedules if i['doctor_id'] == doc_id]}


if __name__ == "__main__":
    run(reloader=True, debug=True)
