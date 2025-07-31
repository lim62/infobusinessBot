from sqlite3 import connect

class Database():
    def __init__(self, name: str) -> None:
        self.conn = connect(name)
        self.cur = self.conn.cursor()
    
    def create_table(self, name: str, columns: dict) -> None:
        values: str = ', '.join(f'{column_name} {column_type}' for column_name, column_type in columns.items())
        query: str = f'CREATE TABLE IF NOT EXISTS {name} ({values})'
        self.cur.execute(query)
        self.conn.commit()
    
    def insert_data(self, name: str, data: dict) -> None:
        columns: str = ', '.join(data.keys())
        placeholders: str = ', '.join(['?' for _ in data.values()])
        query: str = f'INSERT INTO {name} ({columns}) VALUES ({placeholders})'
        self.cur.execute(query, tuple(data.values()))
        self.conn.commit()
    
    def update_data(self, name: str, new_data: dict, condition: dict) -> None:
        set_clause: str = ', '.join([f'{key} = ?' for key in new_data.keys()])
        where_clause: str = 'AND '.join([f'{key} = ?' for key in condition.keys()])
        params: tuple = tuple(list(new_data.values()) + list(condition.values()))
        query: str = f'UPDATE {name} SET {set_clause} WHERE {where_clause};'
        self.cur.execute(query, params)
        self.conn.commit()
    
    def get_data(self, name: str, condition: dict | None = None) -> list:
        query: str = f'SELECT * FROM {name}'
        params: tuple = ()
        if condition:
            where_clause = 'AND '.join([f'{key} = ?' for key in condition.keys()])
            query += f' WHERE {where_clause}'
            params = tuple(condition.values())
        self.cur.execute(query, params)
        return self.cur.fetchall()
    
    def delete_data(self, name: str, condition: dict | None = None) -> None:
        query: str = F'DELETE FROM {name}'
        params: tuple = ()
        if condition:
            where_clause = 'AND '.join([f'{key} = ?' for key in condition.keys()])
            query += f' WHERE {where_clause}'
            params = tuple(condition.values())
        self.cur.execute(query, params)
        self.conn.commit()
    
db = Database('app\database\mainDatabase.db')