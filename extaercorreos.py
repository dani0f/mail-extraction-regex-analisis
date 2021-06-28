import imaplib
import re
from regex import getRegexId

host = 'imap.gmail.com'
imap = imaplib.IMAP4_SSL(host)
imap.login('mail@gmail.com', 'pass')
imap.select('Inbox')
mails = ["info@buscalibre.com","promotion@aliexpress.com","contacto@email.easy.cl","antonia.e@integramedica.cl","noreply@cl.needishmail.com"]

arrayDataMails = []
arrayRegex= []
for c in range(len(mails)):
    typ, data = imap.search(None,'FROM', mails[c])
    arrayData= data[0].split()
    idArray = []
    firstArray = []
    penArray = []
    utcArray = []
    fromArray = []
    mailArray = []
    for i in range(41):
        num = arrayData[i]
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (MESSAGE-ID)])')
        messageId= data[0][1].decode()
        messageId = messageId.split("<")[1].replace(">","").strip()
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Date)])')
        messageUTC= data[0][1].decode()   
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (From)])')
        messageFrom= data[0][1].decode().replace("From:","").strip()
        messageMail= messageFrom.split("<")[1][:-1].strip()
        typ, data = imap.fetch(num, '(BODY[HEADER.FIELDS (Received)])')
        messageReceived= data[0][1].decode().split("Received: ")
        messageFirst = messageReceived[len(messageReceived)-1].strip()
        messagePen = messageReceived[1].strip()
        if('+' in messageFirst):
            messageUTC = "+"+messageFirst.split("+")[1].strip()        
        else:
            numUTC = len(messageFirst.split("-"))
            messageUTC = "-"+messageFirst.split("-")[numUTC-1].strip() 
        messageUTC = messageUTC[0:5] + " (UTC)"

        f = open ("res.txt", "a")
        f.write("------------------Correo numero"+str(i)+"--------------------------\n")
        f.write("MessageId: "+messageId+"\n")
        f.write("Primer received: "+messageFirst.strip()+"\n")
        f.write("Penultimo received: "+messagePen.strip()+"\n")
        f.write("UTC: "+messageUTC+"\n")
        f.write("From: "+messageFrom+"\n")
        f.write("Mail: "+messageMail+"\n")
        f.close()

        idArray.append(messageId)
        firstArray.append(messageFirst)
        penArray.append(messagePen)
        utcArray.append(messageUTC)
        fromArray.append(messageFrom)
        mailArray.append(messageMail)
    arrayRegex.append([getRegexId(idArray),getRegexId(firstArray),getRegexId(penArray),getRegexId(utcArray),getRegexId(fromArray),getRegexId(mailArray)])
imap.close()

for i in range(len(arrayRegex)):
    f = open ("resRegex.txt", "a")
    f.write("---------------Correo numero "+str(i)+"----------------------\n")
    f.write("MessageId: " + arrayRegex[i][0]+"\n")
    f.write("Primer received: "+ arrayRegex[i][1]+"\n")
    f.write("Penultimo received: " + arrayRegex[i][2]+"\n")
    f.write("UTC: " + arrayRegex[i][3]+"\n")
    f.write("From: " + arrayRegex[i][4]+"\n")
    f.write("Mail:" +arrayRegex[i][5]+"\n")
    f.close()



