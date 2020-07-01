from flask_restful import Resource, Api, request
from package.model import conn


class ExportPatients(Resource):
    """It contain all the api carryign the activity with aand specific patient"""

    def get(self):
        """Api to retive all the patient from the database"""
        
        patientInput = request.request("get","/patient.html")
        pat_date1=patientInput['pat_date1']
        pat_date2=patientInput['pat_date2']
        patientInput= conn.execute("SELECT * from patient WHERE pat_date between pat_date1 =? AND pat_date2=?",(pat_date1,pat_date2)).fetchall()
        return patientInput



    def post(self):
        """api to add the patient in the database"""

        patientInput = request.get_json(force=True)

        pat_name=patientInput['pat_name']
        pat_disease=patientInput['pat_disease']
        pat_date=patientInput['pat_date']
        pat_address = patientInput['pat_address']
        pat_ph_no = patientInput['pat_ph_no']
        patientInput['pat_id']=conn.execute('''INSERT INTO patient(pat_name,pat_disease,pat_date,pat_address,pat_ph_no)
            VALUES(?,?,?,?,?)''', (pat_name,pat_disease,pat_date,pat_address,pat_ph_no)).lastrowid
        conn.commit()
        return patientInput

class ExportPatient(Resource):
    """It contains all apis doing activity with the single patient entity"""

    def get(self,id):
        """api to retrive details of the patient by it id"""

        patient = conn.execute("SELECT * FROM patient WHERE pat_id=?",(id)).fetchall()
        return patient

    def delete(self,id):
        """api to delete the patient by its id"""

        conn.execute("DELETE FROM patient WHERE pat_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the patient by it id"""

        patientInput = request.get_json(force=True)
        pat_name=patientInput['pat_name']
        pat_disease=patientInput['pat_disease']
        pat_date=patientInput['pat_date']
        pat_address = patientInput['pat_address']
        pat_ph_no = patientInput['pat_ph_no']
        conn.execute('''UPDATE patient SET pat_name=?,pat_disease=?,pat_date=?,pat_address=?,pat_ph_no=? WHERE pat_id=?''',
                     (pat_name,pat_disease,pat_date,pat_address,pat_ph_no,id)).fetchall()
        conn.commit()
        return patientInput
    
