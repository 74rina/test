def caesar(strInputText, intKey):
   strResult=[]
   for char in strInputText:
      if(ord(char)+intKey<=ord('z')):
         strResult.append(chr(ord(char)+intKey))
      else:
         strResult.append(chr((ord('a')-1)+(ord(char)+intKey-ord('z'))))

   print('key: '+str(intKey)+'>'+''.join(strResult))


for i in range(1,26):
   caesar('erory fbqn ragre pnany',i)
