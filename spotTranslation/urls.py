#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin

import spotTranslation.views
#personCenter.html

urlpatterns=[
    url(r'^index',spotTranslation.views.getindex,name="getindex"),
    url(r'^spot',spotTranslation.views.getspot,name="getspot"),
    url(r'^history',spotTranslation.views.gethistory,name="gethistory"),
    url(r'^register',spotTranslation.views.getregisger,name="getregister"),
    url(r'^login',spotTranslation.views.getlogin,name="getlogin"),
    url(r'^collection',spotTranslation.views.getcollection,name="getcollection"),
    url(r'^personCenter',spotTranslation.views.getPersonCenter,name="getPersonCenter"),
    url(r'^text_translation',spotTranslation.views.get_text_translation,name="get_text_translation"),
    url(r'^image_translation',spotTranslation.views.get_image_translation,name="get_image_translation"),
    url(r'^user_register',spotTranslation.views.get_user_register,name="get_user_register"),
    url(r'^user_login',spotTranslation.views.get_user_login,name="get_user_login"),
    url(r'^sight_info',spotTranslation.views.get_sight_info,name="get_sight_info"),
    url(r'^add_collection',spotTranslation.views.get_add_collection,name="get_add_collection"),
    url(r'^get_collection',spotTranslation.views.get_show_collection,name="get_show_collection"),


]

