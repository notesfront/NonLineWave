from collections import namedtuple

class Person:
    def __init__(self, fname, lname, email, **kwargs):
        self.userlname = lname
        self.userfname = fname
        self.email = email
        for key, value in kwargs.items():
            setattr(self, key, value)

    def find_in_db(self, conn):

        print(self.userfname)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Users WHERE (userfname, email) = (?,?)",
                        (self.userfname, self.email))
        existing_record = cursor.fetchone()
        if existing_record is None:
            return False
        else:
            self.id = existing_record[0]
            return True


    def add_in_db(self, conn):
        if not self.find_in_db(conn):
            attributes = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

            fields = ', '.join(attributes.keys())
            placeholders = ', '.join(['?'] * len(attributes))
            values = tuple(attributes.values())

            print(fields)

            cursor = conn.cursor()
            insert_query = f"INSERT INTO Users ({fields}) VALUES ({placeholders})"
            cursor.execute(insert_query, values)
            # cursor.execute("CREATE UNIQUE INDEX idx_unique_name_email ON users (userlname, email)")
            conn.commit()
        # else:
        #     p


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
        
    