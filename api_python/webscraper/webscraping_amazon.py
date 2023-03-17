from webscraper.webscraping_URLS import AMAZON
from selenium.webdriver.common.by import By
from webscraper.webscraping_setup import setup


driver = setup()
number_of_products = None

async def start_webscraping(product_name: str,number: int):
    number_of_products = number
    driver.get(AMAZON)
    search_input = driver.find_element(By.XPATH,"//div[@class='nav-search-field ']//input")
    search_input.send_keys(product_name)
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    product_cards = driver.find_elements(By.XPATH,"//div[contains(@cel_widget_id,'MAIN-SEARCH_RESULTS-')]//span[@data-component-type='s-product-image']")
    checkpoint_url = driver.current_url
    _navigate_to_products(driver, product_cards,checkpoint_url)
    price = driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']").text
    print(price)
        # driver.get(search_url)
    #//div[@id='corePriceDisplay_desktop_feature_div']//span[@class='a-offscreen']
    # await _get_data(driver)
    driver.close()

async def _navigate_to_products(product_cards,checkpoint_url,number,curr_number=0):
    if (curr_number < number_of_products):
        driver.get(checkpoint_url)
        _get_product_info(product_cards[curr_number])
        _navigate_to_products(product_cards,checkpoint_url)
    return

async def _get_product_info(product_card):
    ...
    
    
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
