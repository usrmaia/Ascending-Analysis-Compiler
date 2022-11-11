GRAMMAR = {
  # key: A -> Exp => [A, ->, Exp]
  "1": ["E", "->", "E", "+", "T"],
  "2": ["E", "->", "T"],
  "3": ["T", "->", "T", "*", "F"],
  "4": ["T", "->", "F"],
  "5": ["F", "->", "(", "E", ")"],
  "6": ["F", "->", "id"],
}

TABLE_SLR = {
  # Action
  "0, id": "s5",
  "0, (": "s4",

  "1, +": "s6",
  "1, $": "OK",

  "2, +": "r2",
  "2, *": "s7",
  "2, )": "r2",
  "2, $": "r2",

  "3, +": "r4",
  "3, *": "r4",
  "3, )": "r4",
  "3, $": "r4",

  "4, id": "s5",
  "4, (": "s4",

  "5, +": "r6",
  "5, *": "r6",
  "5, )": "r6",
  "5, $": "r6",

  "6, id": "s5",
  "6, (": "s4",

  "7, id": "s5",
  "7, (": "s4",

  "8, +": "s6",
  "8, )": "s11",

  "9, +": "r1",
  "9, *": "s7",
  "9, )": "r1",
  "9, $": "r1",

  "10, +": "r3",
  "10, *": "r3",
  "10, )": "r3",
  "10, $": "r3",

  "11, +": "r5",
  "11, *": "r5",
  "11, )": "r5",
  "11, $": "r5",

  # Transitions
  "0, E": "1",
  "0, T": "2",
  "0, F": "3",

  "4, E": "8",
  "4, T": "2",
  "4, F": "3",

  "6, T": "9",
  "6, F": "3",

  "7, F": "10",
}

"""
E'→ E
E → E+T | T
T → T*F | F
F → (E) | id
"""

grammar = {
  "E": [["E", "+", "T"], ["T"]],
  "T": [["T", "*", "F"], ["F"]],
  "F": [["(", "E", ")"], ["id"]],
}

grammar_point = {
  "E": [["E", "+", "T"], ["T"]],
  "T": [["T", "*", "F"], ["F"]],
  "F": [["(", "E", ")"], ["id"]],
}

grammar = [
  {"E": ["E", "+", "T"]},
  {"E": ["T"]},
  {"T": ["T", "*", "F"]},
  {"T": ["F"]},
  {"F": ["(", "E", ")"]},
  {"F": ["id"]},
]

def new_s(grammar, key_s):
  new_grammar = [
    {f"{key_s}'": [f"{key_s}"]}
  ]
  new_grammar.extend(grammar)

  return new_grammar

def lr_point(grammar): 
  new_grammar = []
  for i, dictionary in enumerate(grammar):
    key = dictionary.keys()
    key = list(key)
    key = key[0]
    print(i, key)

    print(grammar[i][key])
    for y in range(0, len(grammar[i][key]) + 1):
      left_point = grammar[i][key][:y]
      #if not left_point: left_point = ""

      right_point = grammar[i][key][y:]
      
      new_grammar.extend([{
        f"{key}": [left_point, ".", right_point]
      }])
  
  return new_grammar

def simpleLR0():
  g = new_s(grammar, "E")
  g = lr_point(g)
  
  print("grammar point")
  for e in g:
    print(e)

if __name__=="__main__":
  simpleLR0()