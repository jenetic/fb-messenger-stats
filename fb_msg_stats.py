import json

# Prints the number of words sent by each person
def TotalWordCount(chatfiles):
  wordcount_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for msg in data["messages"]:
      if msg["sender_name"] not in wordcount_dict:
        wordcount_dict[msg["sender_name"]] = 0
      if msg["sender_name"]:
        try:
          wordcount = len(msg["content"].split(" "))
          wordcount_dict[msg["sender_name"]] += wordcount
        except:
          pass
    for senders in data["participants"]:
      for msg in data["messages"]:
        if senders["name"] not in wordcount_dict:
          wordcount_dict[senders["name"]] = 0
  # Adds up everyone's word count
  totalword_counter = 0
  for x in wordcount_dict:
      totalword_counter += wordcount_dict[x]

  print(str(totalword_counter) + ' WORDS SENT')
  # Sorts by who sent the most words
  for key, value in sorted(wordcount_dict.items(), key = lambda x: x[1], reverse = True): 
    print(str(key) + ": " + str(value)) 

# Prints the number of messages sent by each person
def TotalMessageCount(chatfiles):
  msgcount_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for msg in data["messages"]:
      if msg["sender_name"]: # Note: if you leave the group, it counts as a message
        if msg["sender_name"] in msgcount_dict:
          msgcount_dict[msg["sender_name"]] += 1
        else:
          msgcount_dict[msg["sender_name"]] = 1
    for senders in data["participants"]:
      for msg in data["messages"]:
        if senders["name"] not in msgcount_dict:
          msgcount_dict[senders["name"]] = 0
  
  totalmsg_counter = 0
  for x in msgcount_dict:
    totalmsg_counter += msgcount_dict[x]
  
  print(str(totalmsg_counter) + ' MESSAGES SENT')
  hightolow = sorted(msgcount_dict.items(), key = lambda x: x[1], reverse = True)
  for key, value in hightolow:
    print(str(key) + ": " + str(value)) 

# Prints the average message length of each person
def AveMessageLength(chatfiles):
  wordcount_dict = {}
  msgcount_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for msg in data["messages"]:
      if msg["sender_name"] not in wordcount_dict:
        wordcount_dict[msg["sender_name"]] = 0
      if msg["sender_name"] not in msgcount_dict:
        msgcount_dict[msg["sender_name"]] = 0
      # word count
      if msg["sender_name"]:
        try:
          wordcount = len(msg["content"].split(" "))
          wordcount_dict[msg["sender_name"]] += wordcount
        except:
          pass
      # msg count
      if msg["sender_name"]:
        if msg["sender_name"] in msgcount_dict:
          msgcount_dict[msg["sender_name"]] += 1
        else:
          msgcount_dict[msg["sender_name"]] = 1
    # accounts for ppl who sent no messages			
    for senders in data["participants"]:
      for msg in data["messages"]:
        if senders["name"] not in wordcount_dict:
          wordcount_dict[senders["name"]] = 0
        if senders["name"] not in msgcount_dict:
          msgcount_dict[senders["name"]] = 0	

  # Divides number of words by number of messages
  ave = {}
  for key, dividend in wordcount_dict.items():
    try:
      ave[key] = round(dividend/msgcount_dict.get(key, 1), 2) #rounds to 2 decimal places
    except:
      ave[key] = 0 # prevents division by 0 error

  print('AVERAGE NUMBER OF WORDS PER MESSAGE')
  for key, value in sorted(ave.items(), key = lambda x: x[1], reverse = True):
    print(str(key) + ": " + str(value))

# Prints number of pictures sent by each person
def TotalPictureCount(chatfiles):
  pictcount_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for msg in data["messages"]:
      if msg["sender_name"]:
        try:
          if msg["photos"]:
            for uri in msg["photos"]:
              if uri["uri"]:
                if msg["sender_name"] in pictcount_dict:
                  pictcount_dict[msg["sender_name"]] += 1
                else:
                  pictcount_dict[msg["sender_name"]] = 1
        except:
          pass
    for senders in data["participants"]:
      for msg in data["messages"]:
        if senders["name"] not in pictcount_dict:
          pictcount_dict[senders["name"]] = 0
  
  totalpict_counter = 0
  for x in pictcount_dict:
    totalpict_counter += pictcount_dict[x]
  
  print(str(totalpict_counter) + ' PICTURES SENT')
  for key, value in sorted(pictcount_dict.items(), key = lambda x: x[1], reverse = True):
    print(str(key) + ": " + str(value))

# Prints number of videos sent by each person 
def TotalVideoCount(chatfiles):
  vidcount_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for msg in data["messages"]:
      if msg["sender_name"]:
        try:
          if msg["videos"]:
            for uri in msg["videos"]:
              if uri["uri"]:
                if msg["sender_name"] in vidcount_dict:
                  vidcount_dict[msg["sender_name"]] += 1
                else:
                  vidcount_dict[msg["sender_name"]] = 1
        except:
          pass
    for senders in data["participants"]:
      for msg in data["messages"]:
        if senders["name"] not in vidcount_dict:
          vidcount_dict[senders["name"]] = 0
  totalvid_counter = 0
  for x in vidcount_dict:
    totalvid_counter += vidcount_dict[x]

  print(str(totalvid_counter) + ' VIDEOS SENT')
  for key, value in sorted(vidcount_dict.items(), key = lambda x: x[1], reverse = True):
    print(str(key) + ": " + str(value))

# Prints number and list of people who left the chat
def LeftTheChat(chatfiles):
  leftchat_dict = {}
  for p in chatfiles:
    data = json.load(open(p))
    for sender in data["participants"]:
      leftchat_dict[sender["name"]] = "still in chat"	
    for msg in data["messages"]:
      if msg["sender_name"] not in leftchat_dict:
        leftchat_dict[msg["sender_name"]] = "left chat" 
  
  # Counts number of ppl who left the chat
  leftchat_counter = 0 #
  for x in leftchat_dict:
    if leftchat_dict[x] == "left chat":
      leftchat_counter += 1

  print(str(leftchat_counter) + ' PEOPLE LEFT THE CHAT')
  for s in leftchat_dict:
    if leftchat_dict[s] == "left chat":
      print(s) 

# Prompts user for .json files of messages until user types 'done'
print()
print("FACEBOOK MESSENGER STATS\n")
print("Enter in JSON file paths of your Messenger chat. Most chats will only have one JSON file, but longer chats may have multiple. Type 'done' when you have inputted all files.")
print()

input_file = ""
chatfiles = []

while input_file != "done":
  input_file = input("File path: ")
  if input_file !=  "done":
    chatfiles.append(input_file)

# Run functions
with open(chatfiles[0]) as json_file:
  data = json.load(json_file)
print()
print("CHAT NAME: " + data["title"] + "\n")
TotalWordCount(chatfiles)
print()
TotalMessageCount(chatfiles)		
print()
TotalPictureCount(chatfiles)
print()
TotalVideoCount(chatfiles)
print()
AveMessageLength(chatfiles)
print()
LeftTheChat(chatfiles)
print()
