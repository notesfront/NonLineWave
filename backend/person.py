from collections import namedtuple
import sqlite3

class Person:
    def __init__(self, fname, lname, email, **kwargs):
        self._id=None
        self.userlname = lname
        self.userfname = fname
        self.email = email
        self._conn = sqlite3.connect('participant.db')
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.find_in_db()

    def find_in_db_old(self):
        if self._id is None:
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            existing_record = []
            for t_atr in attributes:
                print(t_atr)
                print(attributes[t_atr])

                cursor = self._conn.cursor()
                cursor.execute(f"SELECT * FROM Users WHERE ({t_atr}) = (?)",
                                (attributes[t_atr],))
                if cursor.fetchall()[0] in existing_record[:, 0]:
                    print('test')
                existing_record.append(cursor.fetchall())

            all_empty = all(not inner for inner in existing_record)
            
            if all_empty:
                print('пусто')
                self.add_in_db()
            else:
                print('не пусто')
                self.check_changes()

    def find_in_db(self):
        if self._id is None:
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
            fields = ', '.join(attributes.keys())
            placeholders = ', '.join(['?'] * len(attributes))
            values = tuple(attributes.values())
            # existing_record = []
            cursor = self._conn.cursor()
            cursor.execute(f"SELECT * FROM Users WHERE ({fields}) = ({placeholders})",
                            (values))
            existing_record = cursor.fetchall()
            print(len(existing_record))
            # if cursor.fetchall()[0] in existing_record[:, 0]:
            #     print('test')
            # existing_record.append(cursor.fetchall())

            # all_empty = all(not inner for inner in existing_record)
            
            # if all_empty:
            #     print('пусто')
            #     self.add_in_db()
            # else:
            #     print('не пусто')
            #     self.check_changes()


    # def add_in_db(self):
    
    #     attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    #     fields = ', '.join(attributes.keys())
    #     placeholders = ', '.join(['?'] * len(attributes))
    #     values = tuple(attributes.values())

    #     cursor = self._conn.cursor()
    #     insert_query = f"INSERT INTO Users ({fields}) VALUES ({placeholders})"
    #     cursor.execute(insert_query, values)
        
    #     self._conn.commit()

    # def check_changes():

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
        
    