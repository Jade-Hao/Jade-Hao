#Jade Hao
#Project 2 Part II
from PIL import Image
import math

def copyImage(inputImage, imageWidth, imageHeight):
    copyImageOutput = Image.new('RGB', (imageWidth, imageHeight), 'white')

    for i in range(imageWidth):
        for j in range(imageHeight):
            pixelColors = inputImage.getpixel((i, j))
            copyImageOutput.putpixel((i, j), pixelColors)

    copyImageOutput.save("/Users/jadehao/Desktop/copy_usfca_logo.png") #saves copied image to desktop

def flipVertical(image_flip): #flips image
    try:
        image = Image.open(image_flip) #opens image
        width, height = image.size #gets image width and height
        flipped_image = Image.new("RGB", (width, height)) #assigns the flipped image new width and height vaules

        for y in range(height):
            for x in range(width):
                pixel = image.getpixel((x, height - y - 1))
                flipped_image.putpixel((x, y), pixel)

        flipped_image.save('verticalflip.png')
        print("Image has been successfully saved!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def findPattern(image_secret):
    image = Image.open(image_secret)
    pixels=image.load()

    for r in range(image.size[0]): #r= rows- this loops through each row in image
        for c in range(image.size[1]): #c= colums- this loops through each coloum in image
            picture_pixels=image.getpixel((r,c)) #finds the pixels at each location (within rows and colums)
            if picture_pixels[0]==255: #checks if the vaule of red in the picture(max red)
                pixels[r,c]=(0,0,0) #sets it to black
    image.save('mystery_solved.png')
    print("Image has been successfully saved!")

def makeGrayscale(image_grey): # Convert the image to grayscale
    image=Image.open(image_grey)
    grayscale_image = Image.new('L', image.size)  # 'L' mode=grayscale

    for x in range(image.width): #Goes through each row
        for y in range(image.height): #Each colum
            old_pixel = image.getpixel((x, y)) 
            red, green, blue = old_pixel
            gray_value = int(0.30 * red + 0.59 * green + 0.11 * blue)
            grayscale_image.putpixel((x, y), gray_value)
    grayscale_image.save("grayscale.png")
    print("Image has been successfully saved!")

def rotate_image(image_rotate):
    image = Image.open(image_rotate)
    width, height = image.size
    rotated_image = Image.new("RGB", (height, width)) #Creates a blank image(Switches to new dimesions)
    
    for x in range(width):
        for y in range(height):
            # Get the pixel at the current position in the original image
            pixel = image.getpixel((x, y))
            
            # Paste the pixel into the rotated image with swapped coordinates
            rotated_image.putpixel((y, width - x - 1), pixel)

    rotated_image.save('rotate.png')
    print("Image has been successfully saved!")

def swapCorners(image_corner):
    image = Image.open(image_corner)
    width, height = image.size
    corner_image = Image.new('RGB', (width, height))

    for x in range(width):
        for y in range(height):#calculates new positions for swapping corners
            new_x, new_y = x, y #creates a new x and y (rows/colums)

            if x >= width // 2:
                new_x -= width // 2 #subtract and equal to
            else:
                new_x += width // 2
            if y >= height // 2:
                new_y -= height // 2
            else:
                new_y += height // 2

            # copy pixels from the original image to the new image
            pixel = image.getpixel((x, y))
            corner_image.putpixel((new_x, new_y), pixel)

    corner_image.save('cornerswap.png')
    print("Image has been successfully saved!")

def blur(image_blur):
    image = Image.open(image_blur)
    width, height = image.size 
    blurred_image = Image.new("RGB", (width, height))
    
    #used to define the 3x3 to sharpen 
    sharpen_filter = [[1, 1, 1], [1, 1, 1],[1, 1, 1] ]
    
    for x in range(width):
        for y in range(height): #accumulator for the sum of red/green/blue pixels
            red_sum = 0 
            green_sum = 0
            blue_sum = 0
            count = 0
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    neighbor_x = x + i #calculate the coordinates of the neighboring pixel
                    neighbor_y = y + j
                    
                    #looks if the neighboring pixels are in area
                    if 0 <= neighbor_x < width and 0 <= neighbor_y < height:
                        neighbor_pixel = image.getpixel((neighbor_x, neighbor_y))
                        red, green, blue = neighbor_pixel
                        red_sum += red
                        green_sum += green
                        blue_sum += blue
                        count += 1

            red_avg = red_sum // count #calculates average of red, green and blue
            green_avg = green_sum // count
            blue_avg = blue_sum // count
            
        
            blurred_image.putpixel((x, y), (red_avg, green_avg, blue_avg)) #sets the vaules
    
    blurred_image.save('blurred.png')
    print("Your image was saved successfully!")

def convolution(image, kernel): #used kernel to redefine blur in order to sharpen the image
    width, height = image.size
    new_image = Image.new("RGB", (width, height))

    kernel_width, kernel_height = len(kernel[0]), len(kernel) #gets the lenght of the 3x3
    pad = kernel_width // 2 #refers to the 3x3 area for bluring

    for x in range(pad, width - pad): #burling the image
        for y in range(pad, height - pad):
            red_sum = green_sum = blue_sum = 0
            for i in range(-pad, pad + 1):
                for j in range(-pad, pad + 1):
                    pixel = image.getpixel((x + i, y + j))
                    red_sum += pixel[0] * kernel[i + pad][j + pad]
                    green_sum += pixel[1] * kernel[i + pad][j + pad]
                    blue_sum += pixel[2] * kernel[i + pad][j + pad]
            new_image.putpixel((x, y), (int(red_sum), int(green_sum), int(blue_sum)))

    return new_image  #returns the blurred image

def sharpenImage(image, amount=1.0):
    kernel = [[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]  # sharpening kernel

    blurred_image = convolution(image, [[1 / 9] * 3] * 3)  # used the def statement above to get blur

    width, height = image.size
    sharpened_image = image.copy() #copies the image to use to sharpen

    for x in range(width):
        for y in range(height):
            pixel_original = image.getpixel((x, y))
            pixel_blurred = blurred_image.getpixel((x, y))

            sharpened_red = int(pixel_original[0] + (pixel_original[0] - pixel_blurred[0]) * amount) #amount=1.0 to sharpen
            sharpened_green = int(pixel_original[1] + (pixel_original[1] - pixel_blurred[1]) * amount)
            sharpened_blue = int(pixel_original[2] + (pixel_original[2] - pixel_blurred[2]) * amount)
            sharpened_image.putpixel((x, y), (sharpened_red, sharpened_green, sharpened_blue)) #sharpens each individual pixel

    sharpened_image.save('sharpen.png')
    print("Your image was saved successfully!")

def sobel_operator(image):
    width, height = image.size

    sobel_x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]] #rows
    sobel_y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]] #colums

    result_image = Image.new('RGB', (width, height))

    for x in range(1, width - 1): 
        for y in range(1, height - 1):
            pixel_red_x = sum(sobel_x[i][j] * image.getpixel((x + i - 1, y + j - 1))[0] 
                for i in range(3) for j in range(3)) #since it is a 3x3
            pixel_red_y = sum(sobel_y[i][j] * image.getpixel((x + i - 1, y + j - 1))[0] 
                for i in range(3) for j in range(3)
            )
            magnitude_red = int((pixel_red_x**2 + pixel_red_y**2)**0.5) #** means to the power of
            #looks for magnitutde for each red, green, and blue pixel for each row and colum
            pixel_green_x = sum(sobel_x[i][j] * image.getpixel((x + i - 1, y + j - 1))[1] 
                for i in range(3) for j in range(3))
            pixel_green_y = sum(sobel_y[i][j] * image.getpixel((x + i - 1, y + j - 1))[1] 
                for i in range(3) for j in range(3))
            magnitude_green = int((pixel_green_x**2 + pixel_green_y**2)**0.5)

            pixel_blue_x = sum(sobel_x[i][j] * image.getpixel((x + i - 1, y + j - 1))[2] 
                for i in range(3) for j in range(3))
            pixel_blue_y = sum(sobel_y[i][j] * image.getpixel((x + i - 1, y + j - 1))[2] 
                for i in range(3) for j in range(3))
            magnitude_blue = int((pixel_blue_x**2 + pixel_blue_y**2)**0.5)

            result_image.putpixel((x, y), (magnitude_red, magnitude_green, magnitude_blue))

    return result_image #returns it to the edge detection

def edgedetection(image_sobel, output_image_path):
    image = Image.open(image_sobel)
    edge_image = sobel_operator(image)
    edge_image.save('sobel.png')
    print("Your image has been saved successfully!")

def scaleLarger(scaled_image, output_image_path, factor): #factor of 2
    with Image.open(scaled_image) as image:
        original_width, original_height = image.size 

        new_width = int(original_width * factor)
        new_height = int(original_height * factor)

        scaled_image = Image.new("RGB", (new_width, new_height))

        for y in range(new_height): #takes the rows and colums of the image and scales it bigger by the given factor
            for x in range(new_width): 
                original_x = int(x / factor)
                original_y = int(y / factor)
                pixel = image.getpixel((original_x, original_y)) 
                scaled_image.putpixel((x, y), pixel)

        scaled_image.save('scaled.png')
        print("Your image has successfully been saved!")

def display_menu(): #displays menu of options
    print("Menu:")
    print("1. Flip Image Vertically")
    print("2. Find Secret pattern")
    print("3. Turn photo black and white")
    print("4. Turn photo 90 degrees")
    print("5. Swaps the corners of the image")
    print("6. Blurs the image")
    print("7. Sharpens the image")
    print("8. Extract edge from image (Sobel)")
    print("9. Scale image larger")
    print("10. Exit")

def main():
    inputImage = Image.open('/Users/jadehao/Downloads/usfca_logo.png')
    imageWidth, imageHeight = inputImage.size
    copyImage(inputImage, imageWidth, imageHeight)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            image_flip = input("Please enter the image name you want to flip: ")
            flipVertical(image_flip)
        elif choice == "2":
            image_secret= input("Enter the image you want to decode: ")
            findPattern(image_secret)
        elif choice == "3":
            image_grey=input("Please enter image you want to make black and white: ")
            makeGrayscale(image_grey)
        elif choice == "4":
            image_rotate=input("Enter the image you want to rotate 90 degrees: ")
            rotate_image(image_rotate)
        elif choice == "5":
            image_corner=input("Please enter image to swap corners: ")
            swapCorners(image_corner)
        elif choice == "6":
            image_blur= input("Enter the image you want to blur: ")
            blur(image_blur)
        elif choice == "7":
            image = input_image_path = input("Please enter the image you want to sharpen: ")
            output_image_path = 'sharpen.png'
            amount = 1.5  # Adjust the amount to control the sharpening strength
            input_image = Image.open(input_image_path)
            sharpened_image = sharpenImage(input_image, amount=amount)
        elif choice == "8":
            image_sobel=input("Enter the image you want to remove the edge: ")
            edgedetection(image_sobel,"sobel.png")
        elif choice == "9":
            scaled_image=input("Please enter the image you want to make larger (by 2x): ")
            scaleLarger(scaled_image, "scaled.png", 2)
        elif choice == "10":
            print("Thank you! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()
