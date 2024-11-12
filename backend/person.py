from collections import namedtuple
import sqlite3

class Person:
    def __init__(self, fname, lname, email, **kwargs):
        self.id=None
        self.userlname = lname
        self.userfname = fname
        self.email = email
        self.conn = sqlite3.connect('participant.db')
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.find_in_db()

    def find_in_db(self):
        if self.id is None:
            existing_record = []
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            del attributes['id']
            del attributes['conn']

            for atr in attributes:
                print(attributes[atr])
                cursor = self.conn.cursor()
                cursor.execute(f"SELECT * FROM Users WHERE ({str(atr)}) = (?)",
                                (attributes[atr],))
                existing_record.append(cursor.fetchone())


        # # print(self.userfname)
        # cursor = self.conn.cursor()
        # cursor.execute("SELECT * FROM Users WHERE (userfname, email) = (?,?)",
        #                 (self.userfname, self.email))
        # existing_record = cursor.fetchone()
        # # print(existing_record)
        # if existing_record is None:
        #     return False
        # else:
        #     self.id = existing_record[0]
        #     return True
        
    # def chk_change_in_db(self):
    #     print(1)

    def add_in_db(self):
        if not self.find_in_db():
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

            fields = ', '.join(attributes.keys())
            placeholders = ', '.join(['?'] * len(attributes))
            values = tuple(attributes.values())

            # print(fields)

            cursor = conn.cursor()
            insert_query = f"INSERT INTO Users ({fields}) VALUES ({placeholders})"
            cursor.execute(insert_query, values)
            
            self.conn.commit()
        # else:
        #     print(1)


    # def save_to_db(self, conn):
    #     print(self.__dict__.items())
    #     attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    #     fields = ', '.join(attributes.keys())
    #     placeholders = ', '.join(['?'] * len(attributes))
    #     values = tuple(attributes.values())

    #     cursor = conn.cursor()
    #     cursor.execute("SELECT * FROM Users WHERE ({fields}) = ({placeholders})",
    #                     (self.userfname, self.userlname))
    #     existing_record = cursor.fetchone()

    #     if existing_record is None:
    #         insert_query = f"INSERT INTO Users ({fields}) VALUES ({placeholders})"
    #         cursor.execute(insert_query, values)
    #         conn.commit()

    #     else:
    #         Row = namedtuple('Row', existing_record.keys())
    #         db_record = Row(*existing_record)
            
    #         changed_fields = {key: val for key, val in attributes.items() if getattr(db_record, key) != val}
    #         if changed_fields:
    #             update_placeholders = ', '.join([f"{field}=?" for field in changed_fields])
    #             update_values = list(changed_fields.values()) + [attributes['id']]
    #             update_query = f"UPDATE persons SET {update_placeholders} WHERE id = ?"
    #             cursor.execute(update_query, update_values)
    #             conn.commit()
        
    