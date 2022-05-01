import csv
import ast

class RawMovieReview:
  # TODO: delete member field
  sampleDictionaryList = []

  def __init__(self, file_name="samples.csv"):
    self.file_name = file_name
    sampleDictionaryList = self.__readCsv(file_name)
    self.sampleDictionaryList = sampleDictionaryList

  def __readCsv(self, file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')

        sampleDictionaryList = []

        for row in readCSV:
            # "{'movie': '니 부모 얼굴이 보고 싶다', 'sentense': '뭔지 ', score: '10' }, ... , {...}"
            for movie in row:
                sampleDictionaryList.append(ast.literal_eval(movie))

        return sampleDictionaryList

  def _getSampleTupleList(self):
      sampleTemp = self.sampleDictionaryList[:]

      tupleList = []
      for sample in sampleTemp:
          tuple = (sample['movie'], sample['sentense'], sample['score'])
          tupleList.append(tuple)

      return tupleList

  def __len__(self):
    return len(self.sampleDictionaryList)



