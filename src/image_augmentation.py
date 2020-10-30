import os

path = "/Users/Terry/CompSci/Senior Project/asl_covid_classifier/covid-symptom-gestures"
categories = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
def rename_files():
  # Renames the 
  for cat in categories:
    dirpath = os.path.join(path, cat)
    print(dirpath)
    # classNum = categories.index(cat)
    imgNum = 0
    for img in os.listdir(dirpath):
      imgPath = os.path.join(dirpath, img)
      # print(imgPath)
      newImgPath = os.path.join(dirpath, str(imgNum)+'.jpg',)
      # print(newImgPath)
      os.rename(imgPath, newImgPath)
      imgNum+=1

rename_files()
