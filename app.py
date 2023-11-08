from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import email_validator

app = Flask(__name__)

app.config['SECRET_KEY'] = 'ec73ac9659fa8192fa7ac32f20a1bbe10593ddaa1eb6a6a1ba898b08c80b1fff'

posts = [
    {
        'author': 'Abhishekt',
        'title': 'How to Not Die by A Shark',
        'content': 'Just don''t swim bruh',
        'date_posted': 'June 11, 2002'
    },

    {
        'author': 'Alan Turing',
        'title': 'How to Blend in with Straight People',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam maecenas sed enim ut sem viverra aliquet eget sit. Lectus quam id leo in vitae turpis massa. Augue interdum velit euismod in pellentesque massa placerat duis. Tellus rutrum tellus pellentesque eu tincidunt tortor. Risus feugiat in ante metus dictum at tempor. Dignissim convallis aenean et tortor at risus viverra adipiscing at. Maecenas ultricies mi eget mauris pharetra et ultrices neque ornare. Suspendisse faucibus interdum posuere lorem ipsum dolor sit amet. Libero justo laoreet sit amet cursus sit amet dictum. Mollis aliquam ut porttitor leo a diam sollicitudin tempor. A cras semper auctor neque vitae tempus quam pellentesque nec. Bibendum arcu vitae elementum curabitur vitae nunc sed. Nec feugiat in fermentum posuere urna. Imperdiet nulla malesuada pellentesque elit eget gravida cum sociis natoque. Egestas fringilla phasellus faucibus scelerisque eleifend. Cursus metus aliquam eleifend mi in nulla posuere sollicitudin. Lectus sit amet est placerat in egestas erat. Duis at consectetur lorem donec massa sapien faucibus et molestie. Enim nec dui nunc mattis. Ultricies leo integer malesuada nunc vel risus. Tellus in metus vulputate eu scelerisque. Rutrum tellus pellentesque eu tincidunt tortor aliquam nulla facilisi cras. Mauris sit amet massa vitae tortor condimentum lacinia quis. Vel turpis nunc eget lorem dolor. Eget nullam non nisi est sit amet. Ullamcorper dignissim cras tincidunt lobortis. Dignissim convallis aenean et tortor at. Quam viverra orci sagittis eu volutpat. In nisl nisi scelerisque eu. Ultrices dui sapien eget mi proin sed libero enim. Turpis egestas maecenas pharetra convallis posuere. Et leo duis ut diam quam nulla porttitor. Gravida dictum fusce ut placerat orci nulla pellentesque. Aenean sed adipiscing diam donec adipiscing tristique risus nec feugiat. Ac tortor dignissim convallis aenean et tortor at. Mi eget mauris pharetra et ultrices neque. Auctor urna nunc id cursus metus.',
        'date_posted': 'December 11, 1942'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Createed for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form, title='Register')


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form, title='Login')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
