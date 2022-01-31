def Gini(listlist):
  answers = []
  weights = []
  totalweight = 0
  for i in range(len(listlist[0])):
    a = 0
    for j in range(len(listlist)):
      a+=listlist[j][i]
    weights.append(a)
    totalweight += a
    sum = 1
    for k in range(len(listlist)):
      sum-=(listlist[k][i]/a)**2
    answers.append(sum)
  final = 0
  for l in range(len(answers)):
    final += (weights[l]/totalweight)*answers[l]
  return final

# example driver code
listlist =[[1,8,1],[3,0,7]]
print(Gini(listlist))
