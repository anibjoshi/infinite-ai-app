import os
from newspaper import Article

link_path = '../data/links/'
data_path = '../data/scraped-data/'

dir_list = os.listdir(link_path)
for file in dir_list:
    file_path = os.path.join(link_path,file)
    file_name = os.path.splitext(file)[0]

    scraped_dir = os.path.join(data_path,file_name)
    if not os.path.exists(scraped_dir):
        os.makedirs(scraped_dir)

    f = open(file_path, 'r')
    article_urls = f.readlines()

    for url in article_urls:
        # Instantiate a Newspaper3k Article object
        print(url)
        try:
            article = Article(url)
            article.download()
            article.parse()

            f = open("".join([scraped_dir,"/",article.title[:20],".txt"]), "a")
            f.write(article.text)
            f.close()

            # Print the article title and text
            print("Title:", article.title)
            print("Text:", article.text)
            print("-----")
        except Exception as e:
            print (e)
            # print("An exception occurred while parsing article")