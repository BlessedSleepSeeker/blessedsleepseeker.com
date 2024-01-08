# Project blessedsleepseeker.com

- [Project blessedsleepseeker.com](#project-blessedsleepseekercom)
  - [Genesis](#genesis)
  - [Frameworks](#frameworks)
  - [Features](#features)
    - [Painless Content Addition](#painless-content-addition)
    - [RSS Feed](#rss-feed)
    - [Translation](#translation)
    - [Black/White theme toggle](#blackwhite-theme-toggle)

My [personal blog](https://www.blessedsleepseeker.com/), developped with Django and Bootstrap.

## Genesis

The idea of having a blog appeared in my brain around June 2023, after I realized that I didn't really wanted to post my art on Twitter cause wtf is da Musk doing ? Thinking about alternative ways of storing my art, I quickly expanded the idea to centralise all my creative works in one place, and building my own blog seemed like the perfect solution. I would be in control of everything, from presentation to features, from the way the pixel-art is scaled to what you can download... Being in control comes with a cost, and it is time. After around 1.5 month of on and off work, totaling around ~60 hours of work, I released the blog to the public on October 17th !

## Frameworks

I use Django for the backend, and use the Django's template system with Bootstrap CSS for my front generation. I am using **Nginx** & **gunicorn** to put my blog on the internet. I followed [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-20-04).

## Features

### Painless Content Addition

Django has an awesome feature : the [*admin panel*](https://docs.djangoproject.com/en/5.0/ref/contrib/admin/). This is very useful, as all my **Blog** and **Art** posts are done **without even having to log in on the server**, I can just go to the website via Firefox, go to the admin panel and add the data there. All the "secondary" pages (FAQ, About Me, Friends and Contact) are all edited from the admin panel as well.

The remaining contents like Code or DIY Projects have hardcoded, dedicated HTML templates in the codebase.

### RSS Feed

I implemented multiples RSS feed ! [Django](https://docs.djangoproject.com/en/5.0/ref/contrib/syndication/) once again did all the [heavy lifting](blessedsleepseeker_com/rss/feeds.py) and I was left with putting data in my feeds.

### Translation

Django's [internationalization](https://docs.djangoproject.com/en/5.0/topics/i18n/translation/) features allowed me to translate easily (it was work tho) between english and french. You could add others languages rather easily if you wanted.

### Black/White theme toggle

Using Bootstrap's theme feature, I developped a small [script](blessedsleepseeker_com/templates/static/theme_switcher.js) allowing a user to switch to its prefered theme. Since my logo is a monochrome white on a transparent background, I created a black version and display the right one depending on which theme is selected.
