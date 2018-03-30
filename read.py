fw= open('sample.txt','w')
fw.write("hello there i am the file you created\n")
fw.write("nice nioce great\n")
fw.close()

fr= open('sample.txt','r')
text= fr.read()
print(text)
fr.close()