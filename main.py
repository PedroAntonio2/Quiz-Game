sheet = [["What is the name of the current United States President(2024)?", "What is the name of the capital of Brazil?", "6 + 4 * 6/(2+4) is"],
        [["Donald Trump","Barack Obama","Joe Biden","Bolsonaro"], ["Brazilia","Lisbon","Washington", "São Paulo"], ["5","8","11","10"]]]

correct_sequence = ["C", "A", "D"]

for p in range(len(sheet[0])):
  response = " "
  print("---------------------------------------------------------------------")
  print(sheet[0][p])
  print(f"""A) {sheet[1][p][0]}
B) {sheet[1][p][1]}
C) {sheet[1][p][2]}
D) {sheet[1][p][3]}
Your response is(A,B,C or D): """)
  while response not in ["A", "B", "C", "D"]:
    response = input().upper()
  if response == correct_sequence[p]:
    print("Congratulations! You have answered correctly")
  else:
    print("You did not answer correctly")
