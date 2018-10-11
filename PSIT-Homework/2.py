# Name : Panjamapon Karnasuta Student ID : 61070367
def main():
  for i in range(1,2):
      # first_name input
      first_name = input("first_name : ")
      # last_name input
      last_name = input("last_name : ")

      # name = [] is array of first & last name
      name = []

      # insert first & last name to array
      name.append(first_name)
      name.append(last_name)

      # print first & last name before swap
      print("\nBefore")
      print(" ".join(name))
      print("____________")

      # swap from last_name to be first_name
      print("\nAfter")
      print(" ".join(name[::-i]))
main()