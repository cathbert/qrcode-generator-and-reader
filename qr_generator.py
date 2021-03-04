# Import required modules
import qrcode


# Main function to hold the generator code
def main(data):
    # Customize qrcode version, box size and border
    code = qrcode.QRCode(version=2, box_size=15, border=5)

    # Add data to the code
    code.add_data(data)

    # Now create the code
    code.make(fit=True)

    # Generate the image
    img = code.make_image(fill='green', back_color='gold')

    # Save the image
    img.save('code_image.png')


if __name__ == '__main__':
    main("https://cartis-coding-hive.business.site")
