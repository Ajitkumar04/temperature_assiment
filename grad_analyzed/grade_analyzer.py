def process_scores(students):
  averages={}
  for name,marks in students.items():
    avg=round(sum(marks)/len(marks),2)
    averages[name]=avg
  return averages


def classify_grades(averages):
  final_result={}
  for name,avg in averages.items():                                                                                                                                                                                                                      
    if avg>=90:
      grade="A"
    elif avg>=75:
      grade="B"
    elif avg>=60:
      grade="C"
    else:
      grade="F"
    final_result[name]=(avg,grade)
  return final_result

def generate_report(classified, passing_avg=70):
  print("=====student grade report=====")
  total_students=len(classified)
  passed=0
  for name,(avg,grade) in classified.items():
    if avg >= passing_avg :
      status="pass"
      passed +=1
    else :
      status="fail"
    print(f"{name.capitalize()}|avg:{avg:2f}|grade:{grade}|status:{status}")
    failed=total_students-passed
  print("="*35)
  print(f"total students:{total_students}")
  print(f"passed:{passed}")
  print(f"failed:{failed}")
    
students ={"Alice":[80,90,70],
           "bob" :[60,90,80],
           "clara":[90,95,98]}
avg_result =process_scores(students)
grade_result = classify_grades(avg_result)
report =generate_report(grade_result)
print(report)

