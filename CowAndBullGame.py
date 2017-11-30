import sys





def guess(word):
  p = 0
  cow = 0
  bull = 0
  unique = []
  secret = ""
  for j in range(0, len(secret)):
    if(secret[j] not in unique):
	  unique.append(secret[j]) 

  for x in range(0, len(word)):
    #print "\n", x
    if(word[x] == secret[x]):
      bull = bull + 1
    else:
	  if(word[x] in unique):
	    cow = cow + 1
  print "bull = ",  bull,"cow = " , cow

  if(bull != 5):
    getWord(word)
		

def getWord(word):
  word = raw_input('Guess a 5 letter word. exit to quit\n')
  #print word
  if word == "exit":
    print '\nexiting....'
	#quit()
  if len(word) == 5:
    #print '\nlen word is fine'
    guess(word)
  else:
	print '\nPlease choose guess a 5 letter word. Re-enter'
	getWord(word)
	
def main():
  #print '\nstart'
  getWord('a')
 
if __name__ == '__main__':
  main()
