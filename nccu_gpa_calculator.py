from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd

driver=webdriver.Firefox()
#政大登陸網頁(打開inccu)
driver.get('https://i.nccu.edu.tw/Login.aspx')
sleep(3)
acc_input=driver.find_element(By.ID,"captcha_Login1_UserName")
acc_input.send_keys("108308036")
password_input=driver.find_element(By.ID,"captcha_Login1_Password")
password_input.send_keys("Ftoi567qqwrb")
login_button=driver.find_element(By.ID,"captcha_Login1_LoginButton")
login_button.send_keys(Keys.ENTER)
#inccu系統(打開我的全人)
sleep(5)
wholeman=driver.find_element(By.ID,"WidgetContainer817121_Widget817121_HyperLink1")
wholeman.send_keys(Keys.ENTER)
#我的全人(第二個網頁)(打開修課計畫)
sleep(6)
handles = driver.window_handles # 獲取所有窗口句柄
driver.switch_to.window(handles[1]) # 切換到第二個窗口
course_plan=driver.find_element(By.CLASS_NAME,"nav10")
course_plan.click()
#修課計畫(打開所有科目明細)(第三個頁面)
sleep(3)
all_detail=driver.find_element(By.CLASS_NAME,"left")
all_detail.click()
#所有科目明細(準備下載表格)
sleep(5)
handles = driver.window_handles # 獲取所有窗口句柄
driver.switch_to.window(handles[2]) # 切換到第三個窗口
html_data=driver.page_source
driver.quit()

dfs=[]
for i in range(5):
    df=pd.read_html(html_data)[i]
    dfs.append(df)

df_combined = pd.concat(dfs, axis=0, ignore_index=True)
df_combined.to_csv('%s.csv'%("政大所有課程清單"), index=False)
print("檔案建立完成")