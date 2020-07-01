from flask_restful import Resource, Api, request
from package.model import conn




class Medicines(Resource):
    """It contain all the api carryign the activity with aand specific medicine"""

    def get(self):
        """Api to retive all the medicine from the database"""

        medicines = conn.execute("SELECT * FROM medicine ORDER BY med_name ASC").fetchall()
        return medicines



    def post(self):
        """api to add the medicine in the database"""

        medicineInput = request.get_json(force=True)
        med_name = medicineInput['med_name']
        med_power = medicineInput['med_power']
        med_brand = medicineInput['med_brand']
        med_mfg = medicineInput['med_mfg']
        med_exp = medicineInput['med_exp']
        med_quan = medicineInput['med_quan']
        medicineInput['med_id']=conn.execute('''INSERT INTO medicine(med_name,med_power, med_brand,med_mfg,med_exp,med_quan)
            VALUES(?,?,?,?,?,?)''', (med_name,med_power,med_brand,med_mfg,med_exp,med_quan)).lastrowid
        conn.commit()
        return medicineInput

class Medicine(Resource):
    """It contains all apis doing activity with the single medicine entity"""

    def get(self,id):
        """api to retrive details of the medicine by it id"""

        medicine = conn.execute("SELECT * FROM medicine WHERE med_id=?",(id)).fetchall()
        return medicine

    def delete(self,id):
        """api to delete the medicine by its id"""

        conn.execute("DELETE FROM medicine WHERE med_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the medicine by it id"""

        medicineInput = request.get_json(force=True)
        med_name = medicineInput['med_name']
        med_power = medicineInput['med_power']
        med_brand = medicineInput['med_brand']
        med_mfg = medicineInput['med_mfg']
        med_exp = medicineInput['med_exp']
        med_quan = medicineInput['med_quan']
        conn.execute('''UPDATE medicine SET med_name=?,med_power=?,med_brand=?,med_mfg=?,med_exp=?,med_quan=?''',
                     (med_name,med_power,med_brand,med_mfg,med_exp,med_quan,id)).fetchall()
        conn.commit()
        return medicineInput

class Medicine(Resource):
    """It contains all apis doing activity with the single medicine entity"""

    def get(self,id):
        """api to retrive details of the medicine by it id"""

        medicine = conn.execute("SELECT * FROM medicine WHERE med_id=?",(id)).fetchall()
        return medicine
