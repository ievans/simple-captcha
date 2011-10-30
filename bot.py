#import captcha
from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import captcha

class bot:
    def __init__(self):
        self.zipCodes = '02139'

    def submitVote(self):
        captchaUrl, captchaKey = self.getCaptchaInfo()
        data = self.makeData('bleh@email.com', 'M', '1984', '12582', captchaUrl, captchaKey)
        print data
        #urllib.request(self.url)

    def getCaptchaInfo(self):
        page =urllib2.urlopen(self.pageUrl).read()
        soup = BeautifulSoup(page)
        captcha = soup.findAll('span', id='img-captcha')
        captchaURL = ('http://eventful.com/' + str(captcha[0])[36:79]).replace('&amp;', '&')
        captchaKey = soup.findAll('input', id='captcha_key')
        captchaKey = str(captchaKey[0])[65:160]
        return (captchaURL, captchaKey)

    def processCaptcha(self):
        pass
        
    def makeData(self, email, gender, yob, postalCode, captcha, captchaKey):
        reqData = [
            ('comsume_captcha','0'),
            ('logAction', 'email'),
            ('location', 'postal_code_id:{0}'.format(postalCode)),
            ('spid', self.spid),
            ('email', email),
            ('username', ''),
            ('password', ''),
            ('password2', ''),
            ('gender', gender),
            ('yob', yob),
            ('opt_partners','0'),
            ('postal_code', postalCode),
            ('country_id', ''),
            ('user_location', 'postal_code_id:{0}'.format(postalCode)),
            ('captcha', captcha),
            ('captcha_key', captchaKey),
            ('mobile1', ''),
            ('mobile2', ''),
            ('mobile3', ''),
            ('carrier', ''),
            ('skip_captcha', 'false'),
            ('state', 'email'),
            ('description', ''),
            ('sdid', ''),
            ('performer_int', '0'),
            ('is_competition', '1'),
            ('competition_name', 'hometownhero2011')
            ]
        return urllib.urlencode(reqData)

    def confirmEmail(self):
        pass
        
if __name__ == "__main__":
    voteBot = bot()
    voteBot.submitVote()
    
