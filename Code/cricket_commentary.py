from BeautifulSoup import BeautifulSoup, SoupStrainer
import urllib
import twitter
import time

def postMessageToTwitter(message):
    try:
        api = twitter.Api('username', password = 'pwd') #set username and password here
        api.PostUpdate(message[0:139]);
        print 'sent message', message
    except:
        print 'failed to connect to twitter'
        
    return message

def getCommentaryURL():

    try:
        doc = urllib.urlopen('http://cricket.plusmo.com/cricket/wap');
    except:
        time.sleep(60)
        print 'failed to fetch http://cricket.plusmo.com/cricket/wap.. will try again'
        try:
            doc = urllib.urlopen('http://cricket.plusmo.com/cricket/wap');
        except:
            print 'again failed.. shutting down'
            sys.exit()
        
    links = SoupStrainer('a')
    tags = [tag for tag in BeautifulSoup(doc, parseOnlyThese=links)]
    commentary_url = ''
    for tag in tags:
        if tag.contents[0].upper().find('INDIA') > -1:
            commentary_url= tag.get('href')
            break

    return commentary_url

def startSendingCommentary(prevComments = [], commentary_url = ''):
    if commentary_url == '':
        commentary_url = getCommentaryURL()
        if commentary_url == '':
            print 'No India Matches'
            sys.exit()

    postNewComments(prevComments, commentary_url)

def postNewComments(prevComments, commentary_url):

    if commentary_url != '':
        try:
            doc = urllib.urlopen('http://cricket.plusmo.com' + commentary_url);
        except:
            print 'failed to reach cricinfo'
            doc = ''
            
        soup = BeautifulSoup(doc)
        tags =  soup.findAll("div", { "class" : "detail" })
        duplicate =  'N'
        comments = []
        comments.extend(prevComments)

        for tag in tags:
            comment = ''
            for content in tag.contents:
                comment =  comment + str(content)

            comment = comment.replace('<br />', '')
            comment = comment.replace('<strong>', '*')
            comment = comment.replace('</strong>', '*')
            #print comment
            
            '''if nothing interesting happened, continue with next comment'''
            if (comment.find('OUT') == -1 and comment.find('FOUR') == -1 and comment.find('SIX') == -1 and comment.find('WIN') == -1 and comment.find('4 runs') == -1):
                continue;


                
            duplicate =  'N'
            for prevcomment in prevComments:
                if comment == prevcomment:
                    duplicate =  'Y'
                    break
            if duplicate == 'N':
                postMessageToTwitter(comment)

            comments.append(comment)
            
            if len(comments) > 7:
                comments.pop()

        prevComments = comments
    
        time.sleep(60) #fetch scores every min
    
        print 'fetch new scores..'
        postNewComments(prevComments, commentary_url)

startSendingCommentary();
