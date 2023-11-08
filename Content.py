class Content:

    def __init__(self,originalContent) -> None:
        self.ContentMasterData = originalContent
        self.itemsTable= self.ContentMasterData.set_index('ItemId')
        self.features = list(self.itemsTable.columns)
        