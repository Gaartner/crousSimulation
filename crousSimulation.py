from selenium import webdriver

import time

def main():
    driver = webdriver.Chrome('/Users/lucsky/Downloads/chromedriver')
    driver.get('https://simulateur.lescrous.fr')

    input_3_59 = driver.find_element_by_id('input_3_59')
    input_3_26 = driver.find_element_by_id('input_3_26')
    input_3_25 = driver.find_element_by_id('input_3_25')
    choice_3_24_2 = driver.find_element_by_id('choice_3_24_2')
    choice_3_24_1 = driver.find_element_by_id('choice_3_24_1')
    choice_3_24_0 = driver.find_element_by_id('choice_3_24_0')

    choice = int(input("entrer 0: \"de 0 à 30 kilomètres\" entrer 1: \"de 30 à 249 kilomètres\" entrer 2: \"de 250 kilomètres et plus\" "))
    if choice == 1:
        choice_3_24_1.click()
    elif choice == 2:
        choice_3_24_2.click()
    else:
        choice_3_24_0.click()

    input_3_59.send_keys(input("le revenu brut global 2019 figurant sur l'avis fiscale 2020 \n detenu par la famille de l'etudiant:"))
    input_3_26.send_keys(input("nombre de frère et soeur:"))
    input_3_25.send_keys(input("nombre de frère et soeur dans l'enseignement superieur:"))

    submit = driver.find_element_by_id('gform_next_button_3_58')
    submit.click()
    time.sleep(15)


if __name__ == '__main__':
    main()
