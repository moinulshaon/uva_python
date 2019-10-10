import os

if __name__ == '__main__':
  currentDirectory = os.path.dirname(os.path.realpath(__file__))
  print("current directory: ", currentDirectory)
  problemNumber = input("enter Problem Number: ")
  volumeNumber = problemNumber[:-2]
  volumeName = "vol_" + ("0"*(3-len(volumeNumber)) + volumeNumber)
  volumePath = os.path.join(currentDirectory, volumeName)
  if not os.path.exists(volumePath):
    confirmation = input("The volume folder does not exists, the volume name will be {} do you want to create it?(y/n)".format(volumeName))
    if confirmation in ["yes","y","Y","YES"]:
      os.mkdir(volumePath)
    else:
      exit(0)
  else:
    print("found volume...", volumeName)
  
  filePath = os.path.join(volumePath, problemNumber)
  os.mkdir(filePath)

  fileNames = ["in.txt", problemNumber+".py"]
  for fileName in fileNames:
    open( os.path.join(filePath, fileName), "a+" ).close()
    print("created file: ", fileName)
