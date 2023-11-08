class Ratings:
    """ This class handles the ratings files and treats it as a Python dictionary"""

    def __init__(self, originalRatings) -> None:
        self.RatingsMasterData = originalRatings
        self.MatrixUsersItems = self.RatingsMasterData.groupby(['UserId','ItemId'])['Rating'].sum()

    def getUsersItemsMatrix(self):
        return self.MatrixUsersItems
    
    def getRatingsData(self):
        return self.RatingsMasterData
        

