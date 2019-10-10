import os
import shutil

if __name__ == '__main__':
  currentDirectory = os.path.dirname(os.path.realpath(__file__))
  print("current directory: ", currentDirectory)
  problemNumber = input("enter Problem Number: ")
  volumeNumber = problemNumber[:-2]
  volumeName = "vol_" + ("0"*(3-len(volumeNumber)) + volumeNumber)
  volumePath = os.path.join(currentDirectory, volumeName)
  if not os.path.exists(volumePath):
    print("Could not find volume...", volumeName)
    exit(1)
  else:
    print("found volume...", volumeName)
  
  filePath = os.path.join(volumePath, problemNumber)
  print("filePath: ",filePath)
  if os.path.exists(filePath):
    shutil.move(filePath, filePath+"__solved")
  else:
    print("No such filePath...")
