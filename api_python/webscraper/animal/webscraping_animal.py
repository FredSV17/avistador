from api.api_models.animal import AnimalModel
from db.animal_table_manage.animal_table import insert_one
from webscraper.webscraping_URLS import ANIMAL_WEBURL, AMAZON
from selenium.webdriver.common.by import By
from webscraper.webscraping_setup import setup

async def start_webscraping(product_name: str):
    driver = setup()
    driver.get(AMAZON)
    search_input = driver.find_element(By.XPATH,"//div[@class='nav-search-field ']//input")
    search_input.send_keys(product_name)
    search_url = driver.current_url
    driver.find_element(By.XPATH,"//input[@id='nav-search-submit-button']").click()
    product_cards = driver.find_elements(By.XPATH,"//div[contains(@cel_widget_id,'MAIN-SEARCH_RESULTS-')]")
    for element in product_cards:
        element.click()
        price = driver.find_element(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']").text
        print(price)
        driver.get(search_url)
    #//div[@id='corePriceDisplay_desktop_feature_div']//span[@class='a-offscreen']
    # await _get_data(driver)
    driver.close()


# async def _get_data(driver):
        
#         div_results = driver.find_elements(By.XPATH,"//div[@class='container']")
#         for div_result in div_results:
#             animal_list = div_result.text.upper().split('\n')
#             [await insert_one(AnimalModel(name = animal)) for animal in animal_list]


## driver.find_elements(By.XPATH,"//span[@id='productTitle']")


## //div[contains(@cel_widget_id,'MAIN-SEARCH_RESULTS-')]

## Preço produto (página de detalhes)
## driver.find_elements(By.XPATH,"//span[@class='a-price aok-align-center reinventPricePriceToPayMargin priceToPay']")

## Detalhes produto (nome)
## //div[@id='productOverview_feature_div']//table//tr//td[@class='a-span3']

## Detalhes produto (detalhes)
## //div[@id='productOverview_feature_div']//table//tr//td[@class='a-span9']

## Detalhes técnicos (nome)
## //table[@id='productDetails_techSpec_section_1']//tr//th
 
## Detalhes técnicos (detalhes)
## //table[@id='productDetails_techSpec_section_1']//tr//td