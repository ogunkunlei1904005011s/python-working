import random

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize Chrome WebDriver

# Open a website in the first tab
profile_directory = r"C:\Users\user\Documents\all_profiles\Profile 19"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument(fr'user-data-dir={profile_directory}')

driver = webdriver.Chrome()



driver.get("https://www.google.com")


mail_list = ["61557917758359", "100082103536797", "marklother829@gmail.com"]
password_list = ["kaka123", "AkangBebek#2022", "Ameeralishah12"]


for mail, passw in zip(mail_list, password_list):

    # i want to auto post on facebook


    # for mail, passw in zip(mail_list, password_list):
    driver.get("https://www.facebook.com/")
    print('FACEBOOK OPENED...')

    time.sleep(555)

    time.sleep(8)

    # Now it will enter the mail to email input
    email = driver.find_element(By.XPATH, '//input[@id="email"]')
    time.sleep(random.randint(1, 4))

    actions = ActionChains(driver)

    # Now it will enter the mail to email input
    time.sleep(random.randint(1, 4))
    try:
        actions.move_to_element(email).click().key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(
            Keys.DELETE).perform()
    except:
        pass

    email.send_keys(mail)
    time.sleep(random.randint(1, 3))
    print('Email Entered...')
    # Now it will enter the password to password input
    time.sleep(random.randint(1, 3))
    password = driver.find_element(By.XPATH, '//input[@id="pass"]')
    time.sleep(random.randint(1, 4))
    password.send_keys(passw)
    time.sleep(random.randint(1, 5))
    print('Password Entered...')

    # Now it will click on the login button
    time.sleep(random.randint(1, 4))
    login = driver.find_element(By.XPATH, '//button[@type="submit"]')
    time.sleep(random.randint(1, 3))
    login.click()

    time.sleep(10)

    try:
        time.sleep(random.randint(3, 7))
        profile_name = driver.find_element(By.XPATH,
                                           '//a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h"]//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]').text
        print(profile_name)
    except:
        time.sleep(random.randint(5, 12))
        profile_name = driver.find_element(By.XPATH,
                                           '//a[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz x1lq5wgf xgqcy7u x30kzoy x9jhf4c x1lliihq"]//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h"]//span[@class="x1lliihq x6ikm8r x10wlt62 x1n2onr6"]').text
        print(profile_name)

    folder_path = r'C:\Users\user\PycharmProjects\auto_uploadonfacebook\videos'  # Replace this with the path of your folder
    videos = get_video_files(folder_path)
    for video in videos:
        print(video)

        driver.get("https://www.facebook.com/profile.php?")

        script = """
            // Using JavaScript to translate the website
            document.documentElement.setAttribute('lang', 'en'); // Replace 'en' with the language code for English
            """

        # Execute the JavaScript code
        driver.execute_script(script)
        time.sleep(3)

        time.sleep(random.randint(1, 4))

        # //span[text()='Photo/video']
        try:
            photo_video = driver.find_element(By.XPATH, "//span[text()='Photo/video']")
        except:
            time.sleep(4)
            photo_video = driver.find_element(By.XPATH, "//span[text()='Foto/video']")

        time.sleep(random.randint(1, 7))
        photo_video.click()
        time.sleep(random.randint(1, 5))

        # //input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]
        try:
            time.sleep(random.randint(1, 3))
            upload = driver.find_element(By.XPATH,
                                         '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
        except:
            time.sleep(random.randint(1, 3))
            upload = driver.find_element(By.XPATH,
                                         '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
        time.sleep(random.randint(1, 4))
        upload.send_keys(f'{video}')

        # //div[@aria-label="What's on your mind?"]//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]
        time.sleep(random.randint(2, 5))

        caption = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
        time.sleep(random.randint(1, 6))
        caption.send_keys(CAPTION)
        time.sleep(random.randint(1, 4))
        try:

            post = driver.find_element(By.XPATH, "//span[normalize-space()='Post']")
            time.sleep(random.randint(1, 5))
            post.click()
            time.sleep(random.randint(1, 4))

        except:
            time.sleep(4)
            post = driver.find_element(By.XPATH, "//span[normalize-space()='Kirim']")
            time.sleep(random.randint(1, 4))
            post.click()
            time.sleep(random.randint(1, 7))
        # Kirim

        print("video uploaded successfully...")
        time.sleep(random.randint(15, 25))

        all_fan_pages_list = []

        try:
            try:
                time.sleep(random.randint(3, 8))
                profile = driver.find_element(By.XPATH,
                                              "//*[name()='g' and contains(@mask,'url(#:Rqir')]//*[name()='image' and contains(@x,'0')]")
                time.sleep(random.randint(2, 5))
                profile.click()
                time.sleep(random.randint(1, 7))
            except:
                time.sleep(random.randint(3, 8))
                profile = driver.find_element(By.XPATH, "(//*[name()='image'])[1]")
                time.sleep(random.randint(1, 4))
                profile.click()
                time.sleep(random.randint(1, 4))
            try:
                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='See all profiles']")
                time.sleep(random.randint(1, 5))
                see_all_profiles.click()
            except:
                time.sleep(4)
                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='Lihat Semua Profil']")
                time.sleep(random.randint(1, 5))
                see_all_profiles.click()
            # Lihat Semua Profil
            # time.sleep(random.randint(3, 9))
            # see_all_profiles.click()
            time.sleep(random.randint(1, 5))
            pages_txt = driver.find_elements(By.XPATH,
                                             '//div[@data-visualcompletion="ignore-dynamic"]//div[@class="x78zum5 xdt5ytf xz62fqu x16ldp7u"]//div[@class="xu06os2 x1ok221b"]//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h"]')
            for page in pages_txt:
                page_text = page.text
                if page_text.strip():  # Check if the text is not an empty string
                    print(page_text)
                    all_fan_pages_list.append(page_text)

            pages_names_list = all_fan_pages_list[1:-1]
            print(pages_names_list)

        except Exception as e:
            print(e)

            profile = driver.find_element(By.XPATH, "(//*[name()='image'])[1]")
            time.sleep(random.randint(1, 4))
            profile.click()
            try:
                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='See all profiles']")
                time.sleep(random.randint(1, 3))
                see_all_profiles.click()
            except:
                time.sleep(4)
                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='Lihat Semua Profil']")
                time.sleep(random.randint(1, 5))
                see_all_profiles.click()
            see_all_profiles.click()
            time.sleep(random.randint(1, 6))
            pages_txt = driver.find_elements(By.XPATH,
                                             '//div[@data-visualcompletion="ignore-dynamic"]//div[@class="x78zum5 xdt5ytf xz62fqu x16ldp7u"]//div[@class="xu06os2 x1ok221b"]//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h"]')
            for page in pages_txt:
                page_text = page.text
                if page_text.strip():  # Check if the text is not an empty string
                    print(page_text)
                    all_fan_pages_list.append(page_text)
            print(all_fan_pages_list)
            pages_names_list = all_fan_pages_list[1:-1]

        if len(pages_names_list) != 0:
            print("pages names not equal to 0")
            for all_fb_pages in pages_names_list:
                driver.get("https://web.facebook.com/profile.php?")
                time.sleep(random.randint(1, 4))
                profile = driver.find_element(By.XPATH, "(//*[name()='image'])[1]")
                time.sleep(random.randint(1, 3))
                profile.click()

                # see all profiles
                try:
                    time.sleep(random.randint(1, 6))

                    see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='See all profiles']")
                    time.sleep(random.randint(1, 5))
                    see_all_profiles.click()
                except:
                    time.sleep(random.randint(1, 3))
                    time.sleep(4)
                    see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='Lihat Semua Profil']")
                    time.sleep(random.randint(1, 5))
                    see_all_profiles.click()

                # click on fan page

                time.sleep(random.randint(1, 5))

                page_btn = driver.find_element(By.XPATH,
                                               f"//div[@role='radio']//div[contains(@class,'x6s0dn4') and contains(@class,'x1q0q8m5')]//div[contains(@class,'x1qjc9v5')]//div//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h'][normalize-space()='{all_fb_pages}']")
                time.sleep(random.randint(2, 4))

                page_btn.click()
                print("SWITCH PAGE SUCCESSFULLY")
                time.sleep(random.randint(2, 6))
                driver.get("https://web.facebook.com/profile.php?")

                time.sleep(random.randint(1, 5))

                # //span[text()='Photo/video']
                try:
                    photo_video = driver.find_element(By.XPATH, "//span[text()='Photo/video']")
                except:
                    time.sleep(4)
                    photo_video = driver.find_element(By.XPATH, "//span[text()='Foto/video']")

                time.sleep(random.randint(1, 6))
                photo_video.click()
                time.sleep(random.randint(2, 4))

                # //input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]
                try:
                    time.sleep(random.randint(1, 3))
                    upload = driver.find_element(By.XPATH,
                                                 '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
                    time.sleep(random.randint(1, 5))
                    upload.send_keys(f'{video}')
                except:
                    time.sleep(random.randint(4, 10))
                    upload = driver.find_element(By.XPATH,
                                                 '//input[@accept="image/*,image/heif,image/heic,video/*,video/mp4,video/x-m4v,video/x-matroska,.mkv"]')
                    time.sleep(random.randint(3, 8))
                    upload.send_keys(f'{video}')

                # //div[@aria-label="What's on your mind?"]//p[@class="xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8"]
                time.sleep(random.randint(1, 4))

                caption = driver.find_element(By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
                time.sleep(random.randint(1, 3))
                caption.send_keys(CAPTION)
                time.sleep(random.randint(1, 4))
                try:
                    time.sleep(random.randint(1, 5))
                    post = driver.find_element(By.XPATH, "//span[normalize-space()='Post']")
                    time.sleep(random.randint(1, 4))
                    post.click()
                    time.sleep(random.randint(1, 4))

                except:
                    time.sleep(random.randint(1, 5))

                    post = driver.find_element(By.XPATH, "//span[normalize-space()='Kirim']")
                    time.sleep(random.randint(1, 5))
                    post.click()
                    time.sleep(random.randint(1, 5))
                # Kirim

                print("video uploaded successfully...")
                time.sleep(random.randint(15, 25))
            driver.get("https://web.facebook.com")
            time.sleep(random.randint(1, 5))
            profile = driver.find_element(By.XPATH, "(//*[name()='image'])[1]")
            time.sleep(random.randint(1, 5))
            profile.click()

            # see all profiles
            try:
                time.sleep(random.randint(3, 8))

                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='See all profiles']")
                time.sleep(random.randint(1, 5))
                see_all_profiles.click()
            except:
                time.sleep(random.randint(11, 20))

                time.sleep(4)
                see_all_profiles = driver.find_element(By.XPATH, "//span[normalize-space()='Lihat Semua Profil']")
                time.sleep(random.randint(3, 9))
                see_all_profiles.click()

            # click on fan page

            time.sleep(random.randint(1, 6))

            page_btn = driver.find_element(By.XPATH,
                                           f"//div[@role='radio']//div[contains(@class,'x6s0dn4') and contains(@class,'x1q0q8m5')]//div[contains(@class,'x1qjc9v5')]//div//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x3x7a5m x6prxxf xvq8zen xk50ysn xzsf02u x1yc453h'][normalize-space()='{profile_name}']")
            time.sleep(random.randint(2, 6))

            page_btn.click()
            print("SWITCH PAGE SUCCESSFULLY")
            print("SWITCH PAGE TO 1ST PROFILE SUCCESSFULLY")
            time.sleep(20)

    # logout setup

    driver.get("https://web.facebook.com")
    time.sleep(random.randint(2, 6))
    profile = driver.find_element(By.XPATH, "(//*[name()='image'])[1]")
    time.sleep(7)
    profile.click()

    time.sleep(random.randint(1, 7))

    # logout setup
    time.sleep(random.randint(3, 7))
    log_out_button = driver.find_element(By.XPATH, "//div[@data-nocookies='true']//i[@class='x1b0d499 xep6ejk']")
    time.sleep(random.randint(2, 6))
    log_out_button.click()
    print('LOGGED OUT...')

    time.sleep(random.randint(4, 7))


time.sleep(5555)

