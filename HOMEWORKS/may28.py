student_profile=("aryan", "grade 8", "section dv", 6)
studnet_name=student_profile[0]
print("first two details:", student_profile[0:2])
monday_subjects= {"math", "science","hindi", "sports", "history", "computer"}
tuesday_subjects={"math", "english", "music", "sports", "history","science" }
monday_subjects.add("library")
monday_subjects.discard("hindi")
all_subjects = monday_subjects.union(tuesday_subjects)
common_subjects=monday_subjects.intersection(tuesday_subjects)
print (monday_subjects)
print(tuesday_subjects)
print(all_subjects)
print(common_subjects)