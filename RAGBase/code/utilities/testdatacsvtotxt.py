import csv


with open('C:\\Users\\manabu.sekino\\Desktop\\helpfulRedditPosts.csv', encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        id = row[0]
        author = row[1]
        isOver18 = row[2]
        postUrl = row[3]
        subredddit = row[4]
        postTitle = row[5]
        hasPostBody = row[6]
        postBody = row[7]
        score= row[8]
        numComments = row[9]

        filename = f"helpfulRedditPosts/{id}.txt"
        filecontent = f"title:\n{postTitle}\n\ncontent:\n{postBody}\n\nurl:{postUrl}\nauthor:{author}\nsubreddit:{subredddit}\nscore:{score}\nnumComments:{numComments}\nisOver18:{isOver18}\nhasPostBody:{hasPostBody}"

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(filecontent)

        print(row)