from util import isOK, isReduce, isShift
from input import INPUT_STR
from grammar import GRAMMAR, TABLE_SLR
from stack import Stack, Queue
from transition_db import TransitionDB as DB

class AscendingAnalysis(DB):
  def __init__(self, INPUT_STR, S="0"):
    super().__init__()

    self.stack = Stack(999)
    self.stack.put("$")
    self.stack.put(str(S))

    self.input = Queue(999)
    for e in INPUT_STR:
      self.input.enqueue(e)
    
    self.symbol = Stack(999)

  def analysisLR(self):
    while True:
      top_stack = self.stack.list[self.stack.top]
      top_input = self.input.list[self.input.front]
      t_action = TABLE_SLR.get(f"{top_stack}, {top_input}")

      if isShift(t_action): 
        self.Shift(top_stack, top_input, t_action)
      elif isReduce(t_action):
        self.Reduce(top_stack, top_input, t_action)
      elif isOK(t_action):
        self.OK(top_stack, top_input, t_action)
        break
      else: 
        self.addDB(f"Erro {top_stack} -> {top_input}: {t_action}")
        exit(-1) 
        
  def Shift(self, top_stack, top_input, t_action):
    next_state = t_action[1:]

    self.addDB(f"Shift {top_stack} -> {top_input}: s{next_state}")

    self.stack.put(next_state)
    self.symbol.put(top_input)
    self.input.dequeue()
  
  def Reduce(self, top_stack, top_input, t_action):
    g_key = t_action[1:]
    g_prod = GRAMMAR.get(g_key)

    self.addDB(f"Reduce {top_stack} -> {top_input}: r{g_key} ({g_prod[0]} -> {g_prod[2:]})")

    new_symbol = g_prod[0]
    
    unstack_list = list(reversed(g_prod[2:]))
    for e in unstack_list:
      if e == self.symbol.list[self.symbol.top]:
        self.stack.get()
        self.symbol.get()
      else: exit(-1)

    self.symbol.put(new_symbol)

    # Transition
    top_stack = self.stack.list[self.stack.top]
    top_symbol = self.symbol.list[self.symbol.top] 

    if TABLE_SLR.get(f"{top_stack}, {top_symbol}"):
      new_status = TABLE_SLR.get(f"{top_stack}, {top_symbol}")
      self.stack.put(new_status)

  def OK(self, top_stack, top_input, t_action):
    self.addDB(f"OK {top_stack} -> {top_input}: {t_action}")

    self.stack.get()
  
  def addDB(self, action):
    DB.set(self, self.stack, self.symbol, self.input, action)
    DB.insertInto(self)

if __name__=="__main__":
  aa = AscendingAnalysis(INPUT_STR)
  aa.analysisLR()