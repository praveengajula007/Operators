import sys
type = sys.argv[1]

if type == "t2.micro":
    print("charge two dollars a day")
elif type == "t2.medium":
      print("charge four dollars a day")
elif type == "t2.xlarge":
      print("charge eight dollars a day")
else:
     print("Provide valid instance type")


