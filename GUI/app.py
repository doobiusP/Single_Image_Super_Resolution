from flask import Flask, render_template, request, send_from_directory
from PIL import Image
import os
import pickle
from os.path import basename
from model import upscale_image  # Assuming upscale_image function is defined in model module

app = Flask(__name__, static_url_path='/static', static_folder='static')


UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Load the model from the saved file
model = pickle.load(open('model.pkl', 'rb'))

@app.template_filter('basename')
def get_basename(path):
    return basename(path)

def save_uploaded_image(file):
    if file:
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        return filepath
    return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if request.method == 'POST':
        uploaded_file = request.files.get('image')
        uploaded_image_path = save_uploaded_image(uploaded_file)
        print("Uploaded image path:", uploaded_image_path)  # Print the uploaded image path
        return render_template('index.html', uploaded_image_path=uploaded_image_path)

@app.route('/upscale', methods=['POST'])
def upscale():
    if request.method == 'POST':
        input_image_path = request.form.get('image_path')
        upscaled_image = upscale_image(model,input_image_path,return_image=True)  # Use the upscale_image function from your model directly
        upscaled_image_filename = 'upscaled_' + os.path.basename(input_image_path)
        upscaled_image_path = os.path.join(app.config['UPLOAD_FOLDER'], upscaled_image_filename)
        upscaled_image.save(upscaled_image_path)
        return render_template('index.html', uploaded_image_path=input_image_path, upscaled_image_path=upscaled_image_path)

@app.route('/download', methods=['GET'])
def download_image():
    filename = request.args.get('filename')
    print("Requested filename:", filename)
    
    # Normalize the filename
    filename = os.path.normpath(filename)
    
    
    if os.path.exists(filename):
        print("File exists, sending...")
    else:
        print("File does not exist.")
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)





if __name__ == '__main__':
    app.run(debug=True)
