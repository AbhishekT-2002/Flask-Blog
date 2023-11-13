from flask import render_template, url_for, flash, redirect, request
from blogapp import app, db, bcrypt
from blogapp.forms import RegistrationForm, LoginForm
from blogapp.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


posts = [
    {
        'author': 'Abhishekt',
        'title': 'How to Not Die by A Shark',
        'content': 'Just don''t swim bruh',
        'date_posted': 'June 11, 2002'
    },

    {
        'author': 'Alex Johnson',
        'title': 'The Power of Positive Thinking',
        'content': 'Discover how cultivating a positive mindset can impact your life. From fostering resilience to attracting success, explore the benefits of maintaining an optimistic outlook.',
        'date_posted': 'November 15, 2023'
    },

    {
        'author': 'Emily Turner',
        'title': 'Exploring Hidden Gems: Off-the-Beaten-Path Travel Destinations',
        'content': 'Escape the ordinary and embark on a journey to lesser-known travel destinations. Uncover the charm of hidden gems that promise unique experiences and unforgettable memories.',
        'date_posted': 'October 8, 2023'
    },

    {
        'author': 'Chris Anderson',
        'title': 'The Science Behind Healthy Habits',
        'content': 'Dive into the scientific principles that contribute to forming and maintaining healthy habits. Learn how understanding the brain''s mechanisms can empower you to make positive lifestyle changes.',
        'date_posted': 'September 25, 2023'
    },

    {
        'author': 'Mia Rodriguez',
        'title': 'Culinary Adventures: Exploring World Cuisines in Your Kitchen',
        'content': 'Embark on a culinary journey without leaving your home. Explore diverse world cuisines, try new recipes, and elevate your cooking skills to create delicious meals from around the globe.',
        'date_posted': 'August 12, 2023'
    },

    {
        'author': 'Ryan Foster',
        'title': 'Mindfulness Meditation: A Guide to Inner Peace',
        'content': 'Learn the art of mindfulness meditation and its profound impact on mental well-being. Discover practical tips and techniques to incorporate mindfulness into your daily routine.',
        'date_posted': 'July 29, 2023'
    },

    {
        'author': 'Sophie Clark',
        'title': 'The Joy of Reading: Building a Lifelong Reading Habit',
        'content': 'Unlock the joy of reading and cultivate a lifelong reading habit. Explore book recommendations, tips for creating a reading-friendly environment, and the benefits of regular reading.',
        'date_posted': 'June 5, 2023'
    },

    {
        'author': 'Daniel White',
        'title': 'Mastering the Art of Time Management',
        'content': 'Efficiently manage your time with practical strategies and techniques. From prioritization to overcoming procrastination, discover the keys to mastering the art of time management.',
        'date_posted': 'May 20, 2023'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account Created, You can now Log in!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(
                'Login Unsuccessful. Please check email and password and try again', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='My Account')