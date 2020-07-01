from flask_restful import Resource, Api, request
from package.model import conn




class Others(Resource):
    """It contain all the api carryign the activity with aand specific Other"""

    def get(self):
        """Api to retive all the Other from the database"""

        others = conn.execute("SELECT * FROM other ORDER BY oth_name ASC").fetchall()
        return others



    def post(self):
        """api to add the other in the database"""

        otherInput = request.get_json(force=True)
        oth_name=otherInput['oth_name']
        oth_role = otherInput['oth_role']
        oth_ph_no = otherInput['oth_ph_no']
        otherInput['oth_id']=conn.execute('''INSERT INTO other(oth_name,oth_role,oth_ph_no)
            VALUES(?,?,?)''', (oth_name, oth_role, oth_ph_no)).lastrowid
        conn.commit()
        return otherInput

class Other(Resource):
    """It contains all apis doing activity with the single Other entity"""

    def get(self,id):
        """api to retrive details of the other by it id"""

        other = conn.execute("SELECT * FROM other WHERE oth_id=?",(id,)).fetchall()
        return other

    def delete(self,id):
        """api to delete the other by its id"""

        conn.execute("DELETE FROM other WHERE oth_id=?",(id,))
        conn.commit()
        return {'msg': 'sucessfully deleted'}

    def put(self,id):
        """api to update the other by it id"""

        otherInput = request.get_json(force=True)
        oth_name=otherInput['oth_name']
        oth_role = otherInput['oth_role']
        oth_ph_no = otherInput['oth_ph_no']
        conn.execute("UPDATE other SET oth_name=?,oth_role=?,oth_ph_no=? WHERE oth_id=?",
                     (oth_name, oth_role, oth_ph_no,id))
        conn.commit()
        return otherInput
