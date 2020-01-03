import glob, os
from PIL import Image, ImageDraw, ImageFont

# filepaths
fp_lavoro = "png/"
fp_in = fp_lavoro + "*.png"
fp_out = "gif/render.gif"

def makePNG(msg, filename):
    W, H = (600, 400)
    myFont = ImageFont.truetype("font/Roboto-Black.ttf", size=45)
    im = Image.new("RGBA", (W, H), "black")
    draw = ImageDraw.Draw(im)
    w, h = draw.textsize(msg, font=myFont)
    # draw.text(((W-w)/2, (H-h)/2), msg, font=myFont, fill="yellow", align='center')
    draw.text(((W-w)/2, (H-20)/2), msg, font=myFont, fill="yellow", align='center')
    im.save(str(filename)+".png", "PNG")

testo_completo = "This is a test".upper()
testo_completo = testo_completo.replace('  ',' ')
parole = [x.strip() for x in testo_completo.split(' ')]

files = glob.glob(fp_in)
for f in files:
    os.remove(f)

cont = 0
for parola in parole:
    makePNG(parola, "png/" + str(cont).zfill(3))
    cont += 1

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0) # 200 = 300 parole minuto, 150 sono 400 p/m
