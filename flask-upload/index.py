# Flask program to Ask a user to upload the image.
# Then image will be converted to numpy array and shown in webpage.
# Again the numpy array converted to image file and save in localdisc with newname.

from flask import *
from PIL import Image
from numpy import asarray
from werkzeug.utils import secure_filename
import os
from numpy import *

# setting up upload folder and file formats
UPLOAD_FOLDER = 'C:/Users/rahul/OneDrive/Desktop/flask-upload/static/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def upload():
    return render_template("file_upload_form.html")


@app.route('/success', methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        image = Image.open(
            UPLOAD_FOLDER + "/" + str(request.files['file'].filename))
    # converting image to array
        data = asarray(image)

    # converting array to image and saving a converted image with new name
        Image.fromarray(data).save(os.path.join(
            app.config['UPLOAD_FOLDER'], "dup_" + str(request.files['file'].filename)))

        picture_dir = "".join(UPLOAD_FOLDER + "/" + "dup_" +
                              str(request.files['file'].filename))

        filename2 = "uploads/dup_" + str(request.files['file'].filename)

        return render_template("success.html", array=data, pic=picture_dir,
                               filename=filename2)


if __name__ == '__main__':
    app.run(debug=True)
