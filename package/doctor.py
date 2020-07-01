from flask_restful import Resource, Api, request
from package.model import conn




class Doctors(Resource):
    """It contain all the api carryign the activity with aand specific doctor"""

    def get(self):
        """Api to retive all the doctor from the database"""

        doctors = conn.execute("SELECT * FROM doctor ORDER BY doc_name ASC").fetchall()
        return doctors



    def post(self):
        """api to add the doctor in the database"""

        doctorInput = request.get_json(force=True)
        doc_name=doctorInput['doc_name']
        doc_qual=doctorInput['doc_qual']
        doc_spec=doctorInput['doc_spec']
        doc_ph_no = doctorInput['doc_ph_no']
        doctorInput['doc_id']=conn.execute('''INSERT INTO doctor(doc_name,doc_qual,doc_spec,doc_ph_no)
            VALUES(?,?,?,?)''', (doc_name,doc_qual,doc_spec,doc_ph_no)).lastrowid
        conn.commit()
        return doctorInput

class Doctor(Resource):
    """It contains all apis doing activity with the single doctor entity"""

    def get(self,id):
        """api to retrive details of the doctor by it id"""

        doctor = conn.execute("SELECT * FROM doctor WHERE doc_id=?",(id)).fetchall()
        return doctor



    def delete(self,id):
        """api to delete the doctor by its id"""

        conn.execute("DELETE FROM doctor WHERE doc_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the doctor by it id"""

        doctorInput = request.get_json(force=True)
        doc_name=doctorInput['doc_name']
        doc_qual=doctorInput['doc_qual']
        doc_spec=doctorInput['doc_spec']
        doc_ph_no = doctorInput['doc_ph_no']
        conn.execute('''UPDATE doctor SET doc_name=?,doc_qual=?,doc_spec=?,doc_ph_no=? WHERE doc_id=?''',
                     (doc_name,doc_qual,doc_spec,doc_ph_no,id)).fetchall()
        conn.commit()
        return doctorInput
