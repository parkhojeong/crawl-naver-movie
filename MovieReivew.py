from RawMovieReview import RawMovieReview

class MovieReivew(RawMovieReview):
    def __init__(self, score_threadhold, file_name="samples.csv", ):
        super().__init__(file_name)
        self.score_threadhold = score_threadhold

    def __toTuple(self):
        sampleTupleList = super()._getSampleTupleList()[:]

        filteredSampleTuleList = []
        for sample in sampleTupleList:
            [_, sentense, score] = sample
            filteredSampleTuleList.append((sentense.strip(), int(score) >= self.score_threadhold, score))

        return filteredSampleTuleList
