import csv
import ast

class RawMovieReview:
  # TODO: delete member field
  sampleDictionaryList = []

  def __init__(self, file_name="samples.csv"):
    self.file_name = file_name
    self.__readCsv(file_name)

  def __readCsv(self, file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        self.__parse(readCSV)

  def __parse(self, csv):
    for row in csv:
        # "{'movie': '니 부모 얼굴이 보고 싶다', 'sentense': '뭔지 ', score: '10' }, ... , {...}"
        for movie in row:
            # TODO: except movie without sentense
            self.sampleDictionaryList.append(ast.literal_eval(movie))

  def _getSampleTupleList(self):
      sampleTemp = self.sampleDictionaryList[:]

      tupleList = []
      for sample in sampleTemp:
          tuple = (sample['movie'], sample['sentense'], sample['score'])
          tupleList.append(tuple)

      return tupleList

  def __len__(self):
    return len(self.sampleDictionaryList)



