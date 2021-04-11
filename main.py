# importing Flask and other modules
from flask import Flask, request, render_template
from google.cloud import vision
from google.cloud import storage
# Flask constructor
app = Flask(__name__)   
client = vision.ImageAnnotatorClient()
image = vision.Image()
# A decorator used to tell the application
# which URL is associated function

@app.route('/', methods =["GET", "POST"])
def gfg():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       global link
       link = request.form.get("url")
       return render_template("/index.html")

    return render_template("upload.html")

@app.route('/index.html', methods =["GET", "POST", "PUT"])
def detect_labels_uri():
    """Detects labels in the file located in Google Cloud Storage or on the
    Web."""
    output = ""
    uri = link
    image.source.image_uri = uri

    response = client.label_detection(image=image)
    labels = response.label_annotations
    print('Labels:')

    for label in labels:
        output += label.description + " "

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    return render_template("redirect.html")
if __name__=='__main__':
   app.run(debug = True)