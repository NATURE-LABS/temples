from PIL import Image
import requests
import matplotlib.pyplot as plt

imgurl = [ 
"https://blessingsonthenet.com/img/uploads/aim_bn_1300525731.jpg",
"https://www.templepurohit.com/wp-content/uploads/2016/04/Meenakshi-Amman-temple-madurai-Tamil-Nadu.jpg",
"https://1.bp.blogspot.com/-YjNRZoeRfjY/XuEEjk0zhnI/AAAAAAAACTs/QiJG1xtFwIwVAICG0g_mhFblY5yoblxnwCK4BGAsYHg/s592/3.png",
"https://1.bp.blogspot.com/-tDdOwOovckE/XuEFNrhieqI/AAAAAAAACUA/tT-b5afa1QYJua4kRkPPHDfhJVQnII2SACK4BGAsYHg/s585/1.png",
"https://1.bp.blogspot.com/-B0YtQOp2SFA/XuEGLM-YMGI/AAAAAAAACVI/C0XMMi6qbNYWVhkR6MczDsxato5qK0IRgCK4BGAsYHg/s792/5.png",
"https://media.istockphoto.com/photos/sri-meenakshi-temple-picture-id174441358?s=612x612",
 "https://media.istockphoto.com/photos/madurai-temple-picture-id614963888?s=612x612",
 ]

def templeimage(timg):

    for i in (imgurl):
        if (i):
            print (timg)
            response = requests.get(i, stream=True)
            img = Image.open(response.raw)

            plt.imshow(img)
            plt.show(block=False)
            plt.pause(3)
            plt.close()

timg = "Madurai Meenakshi"
templeimage(timg)