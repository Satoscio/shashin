import pyexiv2, re, argparse, os
from PIL import Image, ImageFont, ImageDraw

# Constants
COPYRIGHT = "© Satoscio" # change to your own liking
THEMES = {'dark', 'light'}

# Default theme values
t_r, t_g, t_b = 53, 58, 61		# Text color (R, G, B)
b_r, b_g, b_b = 255, 255, 255	# Background color (R, G, B)
angle = "angle.png"

# Parsing command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("file", help="Your photo.", type=str)
parser.add_argument("-c", "--theme", help="Set the final image\'s theme. (optional, default=light)", type=str)
parser.add_argument("-t", "--title", help="Add a title for your photo. (use quotation marks) (optional)", type=str)
args = parser.parse_args()

# Function to detect Japanese characters (Hiragana, Katakana and Kanji)
def isJP():
	jp = re.compile(r'[\u3040-\u30FF\u4E00-\u9FFF]')
	return len(jp.findall(title)) != 0

# Check if user provided a valid file
if os.path.isfile(args.file) and args.file:
	filename = args.file
else:
	raise Exception("No valid file was provided!")

# Check if a theme has been specified. If not, light is still default and active
if args.theme and args.theme.lower() in THEMES:
	if args.theme.lower() == "dark":
		t_r, t_g, t_b = 202, 197, 194
		b_r, b_g, b_b = 53, 58, 61
		angle = "angle-invert.png"

# Check if a title has been specified
if args.title:
	title = "\"" + args.title + "\""
else:
	title = ""


# EXIF evaluation
img = pyexiv2.Image(filename)
data = img.read_exif()
# Camera make
if data["Exif.Image.Make"].lower() == "canon":
	camera = data["Exif.Image.Model"]
else:
	camera = data["Exif.Image.Make"] + " " + data["Exif.Image.Model"]
# Prettifying camera names :)
camera = camera.replace("SONY ILCE-", "Sony Alpha ")
camera = camera.replace("SONY ILCA-", "Sony Alpha ")

# Lens model
lens_data = img.read_xmp()
if "Xmp.crs.LensProfileName" in lens_data.keys():
	# Regex to extract lens name
	lens_model = str(re.search(r'\((.+)\)', lens_data["Xmp.crs.LensProfileFilename"]).group(1))
	if "TAMRON" in lens_model:							# Tamron data is weird, okay?
		lens_model = lens_model[:(len(lens_model)-4)] 
	# lensdata = True // WIP FEATURE
else:
	lens_model = ""
	# lensdata = False // WIP FEATURE

# Shutter speed
exposure = eval(data["Exif.Photo.ExposureTime"])
if exposure < 1:
	exposure = "1/"+str(int(1 / eval(data["Exif.Photo.ExposureTime"])))
exposure = str(exposure) + "s"

# f-stop 
fstop = "f/" + str(eval(data["Exif.Photo.FNumber"]))
iso_speed = data["Exif.Photo.ISOSpeedRatings"]

# Exposure compensation
exp_comp = eval(data["Exif.Photo.ExposureBiasValue"])
if exp_comp > 0:
	exp_comp = "+" + str(exp_comp)
elif exp_comp == 0:
	exp_comp = "±" + str(exp_comp)

img.close()
img = Image.open(filename)


# Graphics
padding = int(((img.size[0]+img.size[1])/2)/8) # Average height and width and take 12.5%
size = tuple([s+padding for s in img.size])
layer = Image.new('RGB', size, (b_r, b_g, b_b))
layer.paste(img, tuple(map(lambda x:int((x[0]-x[1])/2), zip(size, img.size))))

# I think it rotates the corner or something
angle = Image.open(angle)
offset = int(padding/4)
resangle = angle.resize((int(padding/4), int(padding/4)), Image.Resampling.NEAREST)
layer.paste(resangle, (offset, offset), resangle)
resangle = resangle.transpose(Image.Transpose.ROTATE_90)
layer.paste(resangle, (offset, layer.size[1] - (offset*2)), resangle)
resangle = resangle.transpose(Image.Transpose.ROTATE_90)
layer.paste(resangle, (layer.size[0] - (offset*2), layer.size[1] - (offset*2)), resangle)
resangle = resangle.transpose(Image.Transpose.ROTATE_90)
layer.paste(resangle, (layer.size[0] - (offset*2), offset), resangle)

fontsize = int(padding/4)
lineheight = int(fontsize/3)
size = (size[0], size[1] + int(fontsize*3.5) + int(lineheight*3.5))
finalimg = Image.new('RGB', size, (b_r, b_g, b_b))
finalimg.paste(layer)

data1 = exposure + "   " + fstop + "   " + str(exp_comp) + "   "
data2 = "ISO "

textlayer = ImageDraw.Draw(finalimg)

# Font definitions
font_extralight = ImageFont.truetype("fonts/Poppins-ExtraLight.ttf", fontsize)
font_extralight_italic = ImageFont.truetype("fonts/Poppins-ExtraLightItalic.ttf", fontsize)
font_light300 = ImageFont.truetype("fonts/Poppins-Light.ttf", fontsize)
font_regular = ImageFont.truetype("fonts/Poppins-Regular.ttf", fontsize)
font_semibold = ImageFont.truetype("fonts/Poppins-SemiBold.ttf", fontsize)
font_japanese = ImageFont.truetype("fonts/MPLUS1p-Light.ttf", fontsize*0.9)

# Calculate text field length
text_data1_l = textlayer.textlength(data1, font_extralight)				# Data
text_iso_speed_l = textlayer.textlength(iso_speed, font_extralight)		# ISO value
text_data2_l = textlayer.textlength(data2, font_light300)				# ISO text
text_lens_l = textlayer.textlength(lens_model, font_regular)			# Lens
text_camera_l = textlayer.textlength(camera, font_semibold)				# Camera
text_data_l = text_data1_l + text_data2_l + text_iso_speed_l			# Combined data
text_copyright_l = textlayer.textlength(COPYRIGHT, font_extralight)		# Copyright
if isJP():																# Photo title
	font_temp =  font_japanese
else:
	font_temp =  font_extralight_italic
text_title_l = textlayer.textlength(title, font_temp)
	
h_text_pos = int(layer.size[0] * 0.1)

# Camera model
textlayer.text(
	(
		h_text_pos,										# Horizontal position
		layer.size[1] - fontsize + (1.5 * lineheight)	# Vertical position
	),
	camera,												# Text data
	(t_r, t_g, t_b),									# Text color RGB (0-255, 0-255, 0-255)
	font = font_semibold								# Font style/weight
)
# Lens model
textlayer.text(
	(
		h_text_pos,
		layer.size[1] + (2.5 * lineheight)
	),
	lens_model,	
	(t_r, t_g, t_b),
	font = font_regular
)
# SS, aperture, EV comp
textlayer.text(
	(
		h_text_pos,
		layer.size[1] + fontsize + (3.5 * lineheight)
	),
	data1,
	(t_r, t_g, t_b),
	font = font_extralight
)
# ISO text (Bold)
textlayer.text(
	(
		h_text_pos + text_data1_l,
		layer.size[1] + fontsize + (3.5 * lineheight)
	),
	data2,
	(t_r, t_g, t_b),
	font = font_light300
)
# ISO value
textlayer.text(
	(
		h_text_pos + text_data1_l + text_data2_l,
		layer.size[1] + fontsize + (3.5 * lineheight)
	),
	iso_speed,
	(t_r, t_g, t_b),
	font = font_extralight
)
# Photo title
if isJP():
	font_titolo = font_japanese
else:
	font_titolo = font_extralight_italic
textlayer.text(
	(
		layer.size[0] - text_title_l - int(0.1 * layer.size[0]),
		#layer.size[1] + (2.5 * lineheight)
        layer.size[1] - fontsize + (1.5 * lineheight)
	),
	title,
	(t_r, t_g, t_b),
	font = font_titolo
)
# Copyright
textlayer.text(
	(
		layer.size[0] - text_copyright_l - int(0.1 * layer.size[0]),
		layer.size[1] + fontsize + (3.5 * lineheight)
	),
	COPYRIGHT,
	(t_r, t_g, t_b),
	font = font_extralight
)

if filename[(len(filename)-4):].lower() == ".jpg":
	filename = filename[:(len(filename)-4)]

finalimg.save(filename + "-new.jpg")