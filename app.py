from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', title="Testimonials")

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        # Process booking
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Save to database or send an email, etc.
        return redirect(url_for('home'))
    return render_template('booking.html', title="Book a Meeting")

if __name__ == '__main__':
    app.run(debug=True)
