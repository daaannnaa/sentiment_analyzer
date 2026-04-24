from textblob import TextBlob

print ("Are you truly positive?")

user_text = input("Enter a statment and I'll analyze your text emotion:")

analysis = TextBlob(user_text)

if analysis.sentiment.polarity > 0:
   print("You're really positive! :)")
elif analysis.sentiment.polarity < 0:
   print("That statement was negative :(")
else:
  print ("You're neutral :|")
