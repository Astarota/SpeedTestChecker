from selenium.webdriver.common.by import By

class SpeedPageLocators:
	go_btn=(By.CSS_SELECTOR,".js-start-test")
	download_speed=(By.CSS_SELECTOR, ".download-speed")
	upload_speed=(By.CSS_SELECTOR,".upload-speed")
	close_btn=(By.CSS_SELECTOR,"#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div.desktop-app-prompt-modal > div > div > div:nth-child(4) > a")
	fail_message=(By.CSS_SELECTOR,"#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div > div > div > h2")
	close_fail_btn=(By.CSS_SELECTOR,"#container > div > div.main-content > div > div > div > div.pure-u-custom-speedtest > div.speedtest-container.main-row > div.main-view > div > div > div > a")