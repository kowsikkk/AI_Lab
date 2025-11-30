from textblob import TextBlob
print("Welcome all to This Sentiment Analysis Page ")
print("No matter what the lines number, all matters is the polarity!!")
user_i=input("Enter the desired passage : ")
analysis = TextBlob(user_i)
polarity = analysis.sentiment.polarity
print(f"The final results are here!")
print(f"The polarity of passage is : {polarity}")