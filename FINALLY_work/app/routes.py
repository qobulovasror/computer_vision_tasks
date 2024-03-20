from app import app
import glob
import os
import re
from werkzeug.utils import secure_filename
from app.img_routines import *
# from backend.models import User
from flask import request, redirect, render_template, url_for, send_file, send_from_directory
from app import app, ALLOWED_EXTENSIONS
from app.img_process.edit_img import change_contrast1, change_contrast2
import shutil

# IMG_FOLDER = os.path.join("static", "uploaded_files")

# app.config["UPLOAD_FOLDER"] = IMG_FOLDER


@app.route("/")
def landing():
    return render_template("index.html")


def remove_static_files(file_path):
    folder = 'app/static/'+file_path
    # for file in os.listdir(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

@app.route('/edit_kontrast', methods=['GET', 'POST'])
def edit_kontrast():
    remove_static_files('uploaded_files')
    remove_static_files('result_files')
    global INPUT_FILENAME
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            INPUT_FILENAME = filename
            try:
                working_directory = os.getcwd()
                file.save(working_directory + "/app/static/uploaded_files/" + filename)
                method = request.form.get('method')
                if method == 'method1' :
                    new_img = change_contrast1(INPUT_FILENAME, request.form.get('c'))
                    imgs = ['uploaded_files/'+INPUT_FILENAME, new_img]
                    comments = ['Orginal tasvir', 'Ishlangan tasvir']
                    return render_template('result.html', imgs=imgs, len=len(imgs), comments=comments)
                elif method == 'method2':
                    new_img = change_contrast2(INPUT_FILENAME, request.form.get('c'), request.form.get('gamma') )
                    imgs = ['uploaded_files/'+INPUT_FILENAME, new_img]
                    comments = ['Orginal tasvir', 'Ishlangan tasvir']
                    return render_template('result.html', imgs=imgs, len=len(imgs), comments=comments)
                else:
                    return render_template('error.html', message=e)

            except Exception as e :
                print(e)
                return render_template('error.html', message=e)
        return render_template('error.html', message="This img file is not supported.")
        # return redirect(url_for('result.html'))
                
    return render_template('editor1.html')


@app.route('/affin_transformation', methods=['GET', 'POST'])
def affin_transformation():
    global INPUT_FILENAME
    filemessage = "Upload an image..."
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            INPUT_FILENAME = filename
            try:
                working_directory = os.getcwd()
                file.save(working_directory + "/uploaded_files/" + filename)
            except FileNotFoundError :
                return 'Error, folder does not exist'

        return redirect(url_for('uploaded'))
                
    return render_template('editor2.html')







def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


image, slider = None, None
colors = []
width, height = 0, 0


def refresh_parameters(image_path):
    global image, slider, hue_angle, colors, width, height
    image = load_image(image_path)
    slider = get_default_slider()
    width, height = get_image_size(image)
    colors = get_dominant_colors(image_path)


# So preview refreshes with any new change
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response



# Image editing home
@app.route('/upload', methods=['GET', 'POST'])
def uploadimage():
    global INPUT_FILENAME
    remove_static_files()
    filemessage = "Upload an image..."
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        filename = secure_filename(file.filename)
        # if user does not select file, browser also submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            INPUT_FILENAME = filename
            try:
                working_directory = os.getcwd()
                file.save(working_directory + "/uploaded_files/" + filename)
            except FileNotFoundError :
                return 'Error, folder does not exist'

        return redirect(url_for('uploaded'))
            
            # file.save(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME))
            # dupe_image(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), 'copy')
            # refresh_parameters(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME))
                

    return render_template('upload.html', filemessage=filemessage)


# Actual Image editing code
@app.route('/uploaded', methods=['GET', 'POST'])
def uploaded():
    global image, slider

    if INPUT_FILENAME:
        if request.method == 'POST':
            # Nav
            original_button = request.form.get('original_button')
            download_button = request.form.get('download_button')
            # Sliders
            enhance_button = request.form.get('enhance_button')
            # Hue
            hue_button = request.form.get('hue_button')
            # Filters
            blur_button = request.form.get('blur_button')
            sharpen_button = request.form.get('sharpen_button')
            edge_button = request.form.get('edge_button')
            smooth_button = request.form.get('smooth_button')
            # Rotate/resize/crop
            rotate_button = request.form.get('rotate_button')
            resize_button = request.form.get('resize_button')
            crop_button = request.form.get('crop_button')

            if original_button:
                dupe_image(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), 'replace')
            if download_button:
                return send_file(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), as_attachment=True)

            if enhance_button:
                slider = {key: float(request.form.get(key)) for key, value in slider.items()}
                apply_enhancers(image, os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), slider)
            if hue_button:
                hue_angle = float(request.form.get('hue_angle'))
                apply_hue_shift(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), hue_angle)

            if blur_button:
                apply_blur(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), blur_button)
            elif sharpen_button:
                apply_sharpen(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), sharpen_button)
            elif edge_button:
                apply_edge_enhance(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), edge_button)
            elif smooth_button:
                apply_smooth(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), smooth_button)

            if rotate_button:
                angle = int(request.form.get('angle'))
                rotate_image(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), angle)
            elif resize_button:
                n_width = int(request.form.get('width'))
                n_height = int(request.form.get('height'))
                resize_image(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), n_width, n_height)
            elif crop_button:
                start_x = int(request.form.get('start_x'))
                start_y = int(request.form.get('start_y'))
                end_x = int(request.form.get('end_x'))
                end_y = int(request.form.get('end_y'))
                crop_image(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME), start_x, start_y, end_x, end_y)

            if any([original_button, hue_button, blur_button, sharpen_button, edge_button, smooth_button, rotate_button, resize_button, crop_button]):
                refresh_parameters(os.path.join(app.config['UPLOAD_FOLDER'], INPUT_FILENAME))

        return render_template('editor.html', slider=slider, colors=colors, width=width, height=height, filename=INPUT_FILENAME)
    else:
        return render_template('editor.html', slider=slider)


# @login_required
@app.route('/gallery')
def gallery():
    images = []
    # for root, dirs, files in os.walk(app.config['UPLOAD_FOLDER']):
    
    for file in os.listdir('uploaded_files'):
        if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
            images.append(file)
    # for (root, dirs, files) in os.walk('/uploaded_files/'):
        # print("1")
        # for file in files:
        #     if file.endswith(".png") or file.endswith(".jpg") or file.endswith(".jpeg"):
        #         images.append(file)

    return render_template('gallery.html', images=images, len=len(images))