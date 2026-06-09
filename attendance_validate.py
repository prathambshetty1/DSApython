import re
def validate_attendance(emp_id,check_in,check_out):
    emp_pattern=r"^EMP\d+$"
    if not re.match(emp_pattern,emp_id):
        print("Invalid Employee ID! Format: EMP101")
        return
    time_pattern=r"^([01]\d|2[0-3]):([0-5]\d)$"
    if not re.match(time_pattern,check_in):
        print("Invalid check in time! Use HH:MM")
        return
    if not re.match(time_pattern,check_out):
        print("Invalid check out time! Use HH:MM")
        return
    in_hour,in_min=map(int,check_in.split(":"))
    out_hour,out_min=map(int,check_out.split(":"))
    in_minutes=in_hour*60+in_min
    out_minutes=out_hour*60+out_min
    if in_minutes>out_minutes:
        print("Check out time should be greater than check in time")
        return
    working_hours=(out_minutes-in_minutes)/60
    print("\nAttendance Record Valid")
    print("Employee ID: ",emp_id)
    print("Check-In time:",check_in)
    print("Check-Out time:",check_out)
    print("Working Hours:",working_hours)
    if working_hours<8:
        print("Half Day!")
    else:
        print("Full Day!")
validate_attendance("EMP1","02:55","12:56")