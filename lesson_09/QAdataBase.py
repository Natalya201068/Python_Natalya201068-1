from sqlalchemy import create_engine, text


class QAdataBase:
    __scripts = {
        "select": text("SELECT * FROM subject"),
        "insert_new": text(
            "INSERT INTO subject (\"subject_id\", \"subject_title\") values"
            "(:new_id, :title)"),
        "get_max_id": text("SELECT MAX(\"subject_id\") FROM subject"),
        "delete by title": text(
            "DELETE FROM subject WHERE (\"subject_title\")"
            " = :title_to_delete RETURNING *"),
        "update_new": text(
            "UPDATE subject SET subject_title = :new_title WHERE "
            "subject_id = :new_id RETURNING *"),
        "select_by_title": text(
            "SELECT * FROM subject WHERE (\"subject_title\") = :title")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_subjects(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete_by_title(self, title):
        conn = self.__db.connect()
        conn.execute(
            self.__scripts["delete by title"], {"title_to_delete": title})
        conn.commit()
        conn.close()

    def get_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["get_max_id"])
        max_id = result.scalar()
        conn.close()
        return max_id

    def insert_subject(self, title):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        result.mappings().all()
        res = conn.execute(self.__scripts["get_max_id"])
        max_id = res.scalar()
        new_id = max_id + 1
        conn.execute(self.__scripts["insert_new"],
                     {"new_id": new_id, "title": title})
        conn.commit()
        conn.close()

    def update_subject(self, title, new_title):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        result.mappings().all()
        res = conn.execute(self.__scripts["get_max_id"])
        max_id = res.scalar()
        new_id = max_id + 1
        conn.execute(self.__scripts["insert_new"],
                     {"new_id": new_id, "title": title})
        result = conn.execute(self.__scripts["update_new"],
                              {"new_id": new_id, "new_title": new_title})
        updated = result.mappings().first()
        conn.commit()
        conn.close()
        return updated

    def get_subject_by_title(self, title):
        conn = self.__db.connect()
        result = conn.execute(
            self.__scripts["select_by_title"], {"title": title})
        rows = result.mappings().all()
        conn.close()
        return rows

    def delete(self, title):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        result.mappings().all()
        res = conn.execute(self.__scripts["get_max_id"])
        max_id = res.scalar()
        new_id = max_id + 1
        conn.execute(self.__scripts["insert_new"],
                     {"new_id": new_id, "title": title})
        conn.execute(
            self.__scripts["delete by title"], {"title_to_delete": title})
        deleted = result.mappings().first()
        conn.commit()
        conn.close()
        return deleted
