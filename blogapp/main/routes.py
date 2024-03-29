from flask import render_template, request, Blueprint
from blogapp.models import Post

main = Blueprint('main', __name__)



@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Us')

@main.route('/search')
def search():
    query = request.args.get('query', '')
    # Perform a simple search in titles and content
    results = Post.query.filter((Post.title.contains(query)) | (Post.content.contains(query))).all()
    return render_template('search_results.html', results=results, query=query)

