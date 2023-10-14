import bardapi
import os

token = '<ENTER OUR PERSONAL API TOKEN HERE>'

preset_prompt = 'You are Rajendra Singh the Water man of India, you specialize in water body cleanliness and focus on water restoration. Give all your answers in under 100 words. if someone asks you who you are tell them that you are Rajendra Singh the water man of India. Do not show the number of words in your output. you only answer questions related to your field of water bodies and thing related to it and noting else.'

scrapper = bardapi.core.Bard(token)


def get_info(input_text):
    preset_data = preset_prompt + '\n\n' + input_text

    response = scrapper.get_answer(preset_data)
    return response['content']


if __name__ == '__main__':
    inp = input("ENTER: ")
    get_info(inp)
