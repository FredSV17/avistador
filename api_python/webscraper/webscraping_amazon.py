from webscraper.webscraping_URLS import AMAZON
from selenium.webdriver.common.by import By
from webscraper.webscraping_setup import setup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = setup()
number_of_products = None

async def start_webscraping(product_name: str,number: int):
    number_of_products = number
    driver.get(AMAZON)
    element_present = EC.presence_of_element_located((By.XPATH,"//div[@class='nav-search-field ']//input"))
    WebDriverWait(driver, timeout=100).until(element_present)
    search_input = driver.find_element(By.XPATH,"//div[@class='nav-search-field ']//input")
    search_input.send_keys(product_name)
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    checkpoint_url = driver.current_url
    await _navigate_to_products(driver,checkpoint_url,number)
    price = driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']").text
    print(price)
    # driver.get(search_url)
    #//div[@id='corePriceDisplay_desktop_feature_div']//span[@class='a-offscreen']
    # await _get_data(driver)
    driver.close()

async def _navigate_to_products(driver,checkpoint_url,number,curr_number=0):
    if (curr_number < number):
        driver.get(checkpoint_url)
        await _get_product_info(driver,curr_number)
        await _navigate_to_products(driver,checkpoint_url)
    return

async def _get_product_info(driver,curr_number):
    driver.find_elements(By.XPATH,"//span[@data-component-type='s-product-image']")[curr_number].click() #//div[contains(@cel_widget_id,'MAIN-SEARCH_RESULTS-')
    price = driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")
    print(price.text.replace('\n','.'))
    name = driver.find_element(By.XPATH,"//span[@id='productTitle']")
    print(name.text)
    if (driver.find_elements(By.XPATH,"//div[@id='poToggleButton']//span[@class='a-expander-prompt']")):
        driver.find_elements(By.XPATH,"//div[@id='poToggleButton']//span[@class='a-expander-prompt']")[0].click()

    detail_description = driver.find_elements(By.XPATH,"//div[@id='productOverview_feature_div']//table//tr//td[@class='a-span3']")
    products_details = driver.find_elements(By.XPATH,"//div[@id='productOverview_feature_div']//table//tr//td[@class='a-span9']")
    teste_products = [f"{d_desc.text}" for d_desc in detail_description]
    test = [f"{d_desc.text}: {p_det.text}" for d_desc,p_det in zip(detail_description, products_details)]
    print('\n'.join(test))

    techinical_detail_description = driver.find_elements(By.XPATH,"//table[@id='productDetails_techSpec_section_1']//tr//th")
    technical_details = driver.find_elements(By.XPATH,"//table[@id='productDetails_techSpec_section_1']//tr//td")
    test = [f"{d_desc.text}: {p_det.text} " for d_desc,p_det in zip(techinical_detail_description, technical_details)]
    print('\n'.join(test))

    
#teste = product_card.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")

# async def _get_data(driver):
    # Preço produto (página de detalhes)
    # driver.find_elements(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")

    # Detalhes produto (nome)
    # //div[@id='productOverview_feature_div']//table//tr//td[@class='a-span3']

    # Detalhes produto (detalhes)
    # //div[@id='productOverview_feature_div']//table//tr//td[@class='a-span9']

    # Detalhes técnicos (nome)
    # //table[@id='productDetails_techSpec_section_1']//tr//th
    
    # Detalhes técnicos (detalhes)
    # //table[@id='productDetails_techSpec_section_1']//tr//td


## driver.find_elements(By.XPATH,"//span[@id='productTitle']")


## //div[contains(@cel_widget_id,'MAIN-SEARCH_RESULTS-')]
