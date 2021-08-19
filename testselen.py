from selenium import webdriver
import time
def login_and_find_all_shop(username,password):
    all=webdriver.Firefox()
    all.get('https://login.taobao.com/member/login.jhtml')
    all.find_element_by_id("fm-login-id").send_keys(username)
    all.find_element_by_id("fm-login-password").send_keys(password)
    all.find_elements_by_xpath("//button[@class='fm-button fm-submit password-login']")[0].click()
    time.sleep(15)
    all.find_elements_by_xpath("//ul[@id='J_SiteNavBdR']/li[@id='J_SiteNavFavor']")[0].click()
    time.sleep(1)
    all.find_elements_by_xpath("//div[@id='fav-tab-menu']/a[@class='shop-page ']")[0].click()
    status = True
    js='window.scrollTo(0,document.body.scrollHeight)'
    height=0
    while status:
        new_height =len(all.find_elements_by_xpath("//ul[@class='img-item-list J_FavList clearfix']/li"))
        # 每执行一次滚动条拖到最后，就进行一次参数校验，并且刷新页面高度
        if new_height > height:
            all.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            height = new_height
            time.sleep(1)
        else:
            # 当页面高度不再增加的时候，我们就认为已经是页面最底部，结束条件判断
            print("滚动条已经处于页面最下方!")
            all.execute_script('window.scrollTo(0, 0)')  # 把滚动条拖到页面顶部
            break
    shopurl=all.current_url
    shop=all.find_elements_by_xpath("//ul[@class='img-item-list J_FavList clearfix']/li")
    for i in range(len(shop)):
        shop[i]=shop[i].find_elements_by_xpath("//div[@class='shop-name']")
    print(all.get_cookies())
if __name__=="__main__":
    login_and_find_all_shop("18912872036","wwy000727")