import os
import pandas as pd

def readTable(pPath, pSep='\t', pColNames=None):
    try:
        return pd.read_table(pPath, sep=pSep, names=pColNames)
    except IOError:
        raise Exception(pPath + 'not found')

def main():
    sectionPath = os.path.dirname( os.path.realpath(__file__) )
    dataPath = os.path.dirname(sectionPath) + "/data/"

    chipotleData = readTable(dataPath + 'chipotle.tsv')

    userColNames = ['ID', 'Age', 'Gender', 'Occupation', 'Revenue']
    userData = readTable(dataPath + 'user.txt', pSep='|', pColNames=userColNames)
    userData['newCol'] = userData.Occupation + userData.Gender

    imdbData = readTable(dataPath + 'imdb.csv', ',')

    print("First rows ( head(numRows) );")
    print("Specific column: (data[<colName>])")
    print( chipotleData['item_price'].head(2) )

    print("\nLast rows ( tail(numRows) );")
    print("Separate and change column names ( read_table(sep, header, names) ):")
    print( userData.tail(3) )
    print("\nJoin str columns in a new column(data.<newColName>):")
    print( userData.head(1) )

    print("\nNon object type's details:")
    print(imdbData.describe())
    print("\nObject type's details:")
    print( imdbData.describe(include=['object']) )
    print("\nRename all columns (data.columns):")
    print(imdbData.columns)
    imdbData.columns = ['StartRating', 'Title', 'ContentRating', 'Genre', 'Duration', 'ActorsList']
    print(imdbData.columns)
    print("\nRename specific column ( data.rename(columns={'<oldColName>':'<newColName>'}, inplace=True) )")
    print("(inplace to make the changes)")
    imdbData.rename(columns={'StartRating':'starRating'}, inplace=True)
    print(imdbData.columns)
    print("\nDrop columns and rows( data.drop('[<ColName1/index1>, <ColName2/index2>]', axis=1, inplace=True) )")
    print("(axis=1 --> columns, axis=0 --> rows)")
    imdbData.drop('Title', axis=1, inplace=True)
    print( imdbData.head(2) )
    imdbData.drop(0, axis=0, inplace=True)
    print( imdbData.head(2) )
    print("\nSort num values ( data.sort_values(['<ColName1>', '<ColName1>'], ascending=False) ):")
    print( imdbData.sort_values('Duration', ascending=False).tail(4) )
    print("\nSelect by data.duration <= 68:")
    print(imdbData[imdbData.Duration <= 68])

if __name__ == '__main__':
    main()
