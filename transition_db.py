import sqlite3

class TransitionDB():
  def __init__(self):
    self.symbol = []
    self.stack = []
    self.input_str = []
    self.action = []

    self._con = sqlite3.connect("Transition Table")
    self.cursor = self._con.cursor()

    self._con.execute("""
      drop table if exists match;
    """).fetchall()

    self._con.execute("""
      create table if not exists match (
        stack varchar(255), 
        symbol varchar(255), 
        input varchar(255), 
        action varchar(255)
      );
    """).fetchall()
  
  def insertInto(self):
    try:
      self.cursor.execute(f"""
        insert into match (stack, symbol, input, action) values 
        ("{self.stack}", "{self.symbol}", "{self.input_str}", "{self.action}");
      """)
      self._con.commit()
    except sqlite3.Error as erro:
      print(f"Error: {erro}") 
  
  def set(self, stack, symbol, input_str, action):
    self.symbol = symbol
    self.stack = stack
    self.input_str = input_str
    self.action = action