import hidebyparity as hbp

def main():
    WhatToDo = input("R parity(LSB),")
    image_path = 'image.png'  # put your image name here

    if WhatToDo == 'p':
        hideor = input("hide-h, decrypt-d")
        if hideor == 'h':
            message = input("input your message:") + '#####'  # add '#####' as the end of the message
            new_img = hbp.hide_message_in_image(image_path, message)
            new_img.save('new_image.png')
        elif hideor == 'd':
            message = hbp.retrieve_message_from_image('new_image.png')
            print('The hidden message is:', message)
            
if __name__ == "__main__":
    main()