def isReduce(cell):
  if cell is None: return False
  elif cell[0] == "r": return True
  return False

def isShift(cell):
  if cell is None: return False
  elif cell[0] == "s": return True
  return False

def isOK(cell):
  if cell is None: return False
  elif cell == "OK": return True
  return False