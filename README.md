# lets-blog

## Description
This is the blogging website, where we are supposed to create articles and people will read them. The project should contains the following minimum requirements

#### Frontend
- Good UI to attract peopl
- Mobile Friendly
- Header, Navigation and Footer
- Login and SignUp Page
- Search Option to search for the blogs

#### Backend
- Database to store all the information
- Login and SignUp
- Display Blogs along with the recent three blogs of the publisher
- Anyone can read the blog, but only authorized member can post it.

#### API
- Using GitHub API to display the details of Bellatrix Data on the About Us section of the Application
- Using GitHub API of the author to display a little information about them on the blog posts like, Location, Company, Number of Repos

## Set-up Guide

#### Clone the Project
```sh
git clone git@github.com:bellatrixdatacommunity/lets-blog.git
cd lets-blog
```

#### Make a new branch using following command
```sh
git checkout -b "<your-branch>"
```

#### Create a Virtual Environment and activate it
```sh
python -m venv venv
source venv/bin/activate
```

#### Installing Dependencies
```sh
python -m pip install -r requirements.txt
```

#### Makemigrations to the db
```sh
python manage.py makemigrations
python manage.py migrate
```

#### Starting the Server
```sh
python manage.py runserver
```

```txt
Code .... .... ....
.... Code .... ....
.... .... Code ....
.... .... .... Code
```

#### Stage your changes, commit, and push using the following commands
```sh
git add .
git commit -m "<commit message>"
git push origin "<your-branch>"
```

#### Deactivate your Virtual Environment
```sh
source deactivate
```


## Mentors


## Contributors


