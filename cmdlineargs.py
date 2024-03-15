import sys # gives access to command line args


def main(args):
   #c-style "main/entrypoint" function
  if len(args) <= 0:
    print("hello")
    return
  print("hello,", args[0])
  for arg in args:
    print(arg)


if __name__ == "__main__":
  main(sys.argv[1:])
  