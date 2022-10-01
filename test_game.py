
import json

with open('tests.json') as json_file:
  data = json.load(json_file)
  # print1 = []
  all_rank = []
  all_name = []
  allpopp = [] 
  
  while True:

    oper = input("Do you want to play?\nChoose: game or rank or exit: ")
    if oper == "game":
      ism = input("Write your name here: ")
      print(f"Hello {ism}, Welcome to our Test!")
      
      
      all_information_about_score = []
      while True:
        if oper == "game":
          
          put = int(input("\nTo start test write -> 1 <-\nTo see your rank write -> 2 <-\nTo exit your acount write -> 3 <-\nWrite here: "))
          if put == 1:
            result = [True]
            abcd = "abcd"
            all_name.append(ism)
            for i in range(len(data)):
              if result[i] == True:
                values = data[i].get("question")
                print(values)
                values1 = data[i].get("answers")
                values1_f = [n.get("key") for n in values1]
                values1_j = [n.get("isTrue") for n in values1]
                for item in range(len(values1_f)):
                  print(f"{abcd[item]}: {values1_f[item]}")
                option = input("Choose answer: ")
                for n in range(len(values1_j)):
                  if option == abcd[n]:
                    values1_j1 = values1_j[n]
                    result.append(values1_j[n])
              
              else:
                break
            all_information_about_score.append(result)
          elif put == 2:
            a1 = []
            for all in all_information_about_score:
              a1.append(all[1:].count(True))
              print(f"{ism}'s score = {a1[-1]}")
          elif put == 3:
            break
        else:
          break
      for alll in all_information_about_score:
        all_rank.append(alll)

      popp = []
      for i in all_rank:
        popp.append(i[1:].count(True))

      name0 = []
      all_zip = zip(all_name, popp)
      all_tuple = dict(all_zip)
      for x, y in all_tuple.items():
        name0.append(f"{x} -- {y}")
      with open("user.json", "w") as fi:
        json.dump(name0, fi)

    elif oper == "rank":
      
      with open("user.json") as all_score_about_json:
        data1 = json.load(all_score_about_json)
        score = []
        for some in range(len(data1)):
          score.append(int(data1[some][::-1][:2][::-1]))
          
          
           
        name1 = sorted(score, reverse=True)
        for some1 in name1:
          for some2 in range(len(name1)):
            if str(some1) in data1[some2]:
              allpopp.append(data1[some2])
              print(data1[some2])

    else:
      print("GOOD BYE USER")
      break
  with open("user1.json", "a") as d:
    json.dump(allpopp, d)
