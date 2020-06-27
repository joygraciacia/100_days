#schema-- where DB tables are created and maintained 
# we need three tables:
# 1. todolist
import sqlite3 

class Schema:
	def __init__(self):
		self.conn = sqlite3.connect('todo.db')
		self.create_user_table()
		self.create_to_do_table()
	def create_to_do_table(self):
		query = """
		CREATE TABLE IF NOT EXISTS "Todo" (
			id INTEGER PRIMARY KEY,
			title TEXT, 
			description TEXT,
			_is_done boolean,
			_is_deleted boolean,
			CreatedOn Date DEFAULT CURRENT_DATE,
			DueDate Date,
			UserId INTEGER FOREIGNKEY REFERENCES User(_id)
		);
		"""
		self.conn.execute(query)
	def create_user_table(self):
		query = """
		CREATE TABLE IF NOT EXISTS "user"(
			_id INTEGER PRIMARY KEY AUTOINCREMENT,
			Name TEXT NOT NULL,
			Email TEXT,			
			CreatedOn Date default CURRENT_DATE
		)
		"""
		self.conn.execute(query)


class ToDoModel:
	TABLENAME = "TODO"
	def __init__(self):
		self.conn = sqlite3.connect('todo.db')
    def create(self, text, description):
        query = f'insert into {TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'
        
        result = self.conn.execute(query)
        return result
	def delete(self, item_id):
		query = f"UPDATE {self.TABLENAME} " \
				f"SET _is_deleted = {1}" \
				f"WHERE id = {item_id}"
		result = self.conn.execute(query)
		return result

	def update

