from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import schedule
import datetime

e = datetime.datetime.now()

firstClass = "08:00"
secondClass = "09:00"
thirdClass = "10:15"
fourthClass = "11:15"
lab = "14:00"
Os = "https://meet.google.com/gmr-iikq-wvf"
Dbms = "https://meet.google.com/ofs-wezh-che"
Ss = "https://meet.google.com/dzv-bfje-vxy"
Coa = "https://meet.google.com/xmo-ftmk-fzo"
OSLab = ""
DBMSLab = ""
COALab = "https://meet.google.com/mjo-gdrc-fie"
emailid = "" # enter your email id here

password = "" # enter your password here
duration = 3300
day = (e.strftime("%a"))
url = "https://meet.google.com/pkw-txgr-hsz"


def join_os():
    bot(Os)
def join_dbms():
    bot(Dbms)
def join_ss():
    bot(Ss)
def join_coa():
    bot(Coa)
def join_os_lab():
    bot(OSLab)
def join_dbms_lab():
    bot(DBMSLab)
def join_coa_lab():
    bot(COALab)

def bot(url):
    opt= Options()
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
    })

    PATH = "enter path of downloaded chrome webdriver" # for example : home/computer/chromewebdriver
    driver = webdriver.Chrome(options = opt , executable_path = PATH)
    driver.maximize_window()
    driver.get("https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&_ga=2.244384962.692424018.1610134292-271021477.1610134292&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

    search = driver.find_element_by_id("identifierId")
    search.send_keys(emailid)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    search = driver.find_element_by_name("password")
    search.send_keys(password)
    search.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.get(url)
    mic = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div/div")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(mic).click(mic).perform()

    vid = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div/div")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(vid).click(vid).perform()

    join = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]")
    driver.implicitly_wait(10)
    ActionChains(driver).move_to_element(join).click(join).perform()

    time.sleep(duration)

    driver.quit()
    return 0

def monday():
    schedule.every().monday.at(firstClass).do(join_os)
    # schedule.every().monday.at(secondClass).do(joinMaths())
    schedule.every().monday.at(thirdClass).do(join_dbms)
    schedule.every().monday.at("17:05").do(join_coa_lab)
    schedule.every().monday.at(lab).do(join_os_lab)
    
def tuesday():
    # schedule.every().tuesday.at(firstClass).do()
    schedule.every().tuesday.at(secondClass).do(join_ss)
    schedule.every().tuesday.at(thirdClass).do(join_coa)
    schedule.every().tuesday.at(fourthClass).do(join_os)
    schedule.every().tuesday.at(lab).do(join_dbms_lab)

def wednesday():
    schedule.every().wednesday.at(firstClass).do(join_coa)
    schedule.every().wednesday.at(secondClass).do(join_os)

    # schedule.every().wednesday.at(thirdClass).do(joinPhysics())

    # schedule.every().wednesday.at(fourthClass).do(joinMaths())
    schedule.every().wednesday.at(lab).do(join_coa_lab)

def thursday():
    schedule.every().thursday.at(firstClass).do(join_dbms)
    schedule.every().thursday.at(secondClass).do(join_coa)
    # schedule.every().thursday.at(thirdClass).do(joinEnglish())
    schedule.every().thursday.at(fourthClass).do(join_ss)
    # schedule.every().thursday.at(fifthClass).do(joinBio())

def friday():
    schedule.every().thursday.at(firstClass).do(join_dbms)

    #schedule.every().thursday.at(secondClass).do(bot(Coa))

    # schedule.every().thursday.at(thirdClass).do(joinEnglish())

    print(day) 
    schedule.every().thursday.at(fourthClass).do(join_ss)

    # schedule.every().thursday.at(fifthClass).do(joinBio())


if day == "Mon":
    monday()
elif day=="Tue":
    tuesday()
elif day=="Wed":
    wednesday()
elif day=="Thu":
    thursday()
elif day=="Fri":
    friday()
else:
    print("It's holiday sir...")
print(day)
while True:
    schedule.run_pending()
    time.sleep(1)
