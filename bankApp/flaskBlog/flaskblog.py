from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# THIS BOC IS CREATING AN OBJ THAT WILL REPRESENT THE WEB APP CALLED APP
app = Flask(__name__)

# THS SECRET KEY ALLOWS FOR THE WEB SITE TO REMEMBER THE USER'S LOG ON INFO
# IT ALSO MITIGATES OTHER DATABASE VULNERABILITIES
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# THIS BOC SIMULATES A BLOG BEING POSTING TO THE HOME PAGE
# AS THOUGH IT WAS INPUTTED BY A BLOGGER
# THE POSTS VAR REPRESENTS TWO DICTIONARIES CONTAINING KEY VALUE PAIRS
# THAT REPRESENTS PROPERTIES OF ONE BLOG POST
# EACH BLOG POST WILL HAVE THESE PROPERTIES
posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

# THIS BOC DEFINES THE ROUTES OF THE WEBSITE *** THIS IS CALLED A DECORATOR ***
# ROUTES ARE WHAT WE TYPE IN THE BROWSER TO GO TO DIFFERENT PAGES
# YOU CAN HAVE A ROUTE FOR THE HOME-PAGE, THE ABOUT PAGE AND OTHER PAGES
# WITHIN YOUR WEB SITE
# THIS ROUTE WILL DEFINE THE HOME PAGE
@app.route("/")
@app.route("/home")
# YOU CAN HAVE MULTIPLE ROUTES GOING TO THE SAME WEB PAGE
#BELOW IS A ROUTE ADDED SO IF THE USER APPEND "/home" AT THE END OF THE URL
# IT WILL GO TO THE SAME WEB PAGE AS THE USER JUST TYPING THE URL
# GLITCH.COM & GLITCH.COM/HOME WILL TAKE YOU TO THE SAME HOME-PAGE
# @app.route("/home")
def home():
    # THE RENDER_TAMPLE METHOD IS BEING USED TO GRAB THE home.html FILE
    # IN THE templates FOLDER AND RENDER IT INTO THIS PYTHON FILE WHEN EXECUTED
    # THE posts=posts  ALLOWS BLOGS TO BE PASSED TO THE TEMPLATE FILE.
    # THE FIRST posts IS A VAR ACTING LIKE AN ENTRY POINT INTO THE RESPECTIVE TEMPLATE FILE
    # THIS FIRST posts CAN BE ANY NAME, BUT THAT NAME WILL BE REF IN THE RESPECTIVE TEMPLATE FILE.
    # THE SECOND posts IS REFERENCING THE VAR IN THE ABOVE CODE THAT IS REPRESENTING THE 2 BLOG POST
        return render_template('home.html', posts=posts)

    
@app.route("/about")
def about():
    # THE RENDER_TAMPLE METHOD IS BEING USED TO GRAB THE about.html FILE
    # IN THE templates FOLDER AND RENDER IT INTO THIS PYTHON FILE WHEN EXECUTED
    return render_template('about.html', title='About')

# THIS ROUTE WAS ADDED TO SEND THE USER TO A PAGE SO THEY CAN REGISTER FOR A NEW ACCOUNT
# "INPUT EXPLAINATION FOR methods"
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # "INPUT EXPLAINATION FOR validating data"
    if form.validate_on_submit():
        # "INPUT EXPLAINATION FOR flash messages"
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


# THIS BOC ALLOWS THE PYTHON CODE TO RUN AND ACCEPT UPDATES TO THE FILE, AND LOAD THEM
# RIGHT AWAY. THIS PREVENTS THE MANUAL RESTARTING OF THE APP WHEN CHANGES ARE MADE TO THE
# SRC CODE. ALL YOU HAVE TO DO IS REFRESH THE BROWSER TO SEE THE UPDATED OUTPUT
if __name__ == '__main__':
    app.run(debug=True)

