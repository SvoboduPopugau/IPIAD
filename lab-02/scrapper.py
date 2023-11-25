from selenium import webdriver
from selenium.webdriver.common.by import By

# Создаем экземпляр драйвера (например, ChromeDriver)
driver = webdriver.Chrome()

# Открываем веб-страницу
driver.get("https://mail.ru/")

# Находим элемент по его CSS-селектору
element = driver.find_element(By.CSS_SELECTOR, "[title='Нефть марки Brent']")

# Получаем текст из найденного элемента
element_text = element.text

# Выводим текст элемента
print("Нефть марки Brent:", element_text)

# Закрываем браузер
driver.quit()
