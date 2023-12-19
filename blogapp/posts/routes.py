from flask import Blueprint, render_template, redirect, request, url_for, flash, abort
from flask_login import current_user, login_required
from blogapp.models import Post, Comment
from blogapp import db
from blogapp.posts.forms import PostForm, CommentForm


posts = Blueprint('posts', __name__)

@posts.route('/posts/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content  = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form = form, legend = 'What is on your mind today?')

@posts.route("/post/<int:post_id>", methods=['GET', 'POST'])
@login_required
def post(post_id):
    post = Post.query.get_or_404(post_id)
    comments = Comment.query.filter_by(post_id=post.id).all()
    comment_form = CommentForm()

    if request.method == 'POST' and comment_form.validate_on_submit():
        text = comment_form.text.data

        new_comment = Comment(author=current_user, text=text, post=post)
        db.session.add(new_comment)
        db.session.commit()

        flash('Your comment has been added!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))

    return render_template('post.html', title=post.title, post=post, comments=comments, comment_form=comment_form)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash(f'Your post has been successfully updated!', 'success')
        return redirect(url_for('posts.post', post_id = post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form = form, legend = 'Update Post')

@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if current_user != post.author:
        abort(404)

    Comment.query.filter_by(post_id=post.id).delete()
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post has been deleted', 'success')
    return redirect(url_for('main.home'))
