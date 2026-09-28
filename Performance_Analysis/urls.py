"""
URL configuration for Performance_Analysis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from app.views import *


urlpatterns = [

    path('', home),

    # =====================================================
    # LOGIN
    # =====================================================

    path('student-login/', student_login),

    path('staff-login/', staff_login),

    path('admin-login/', admin_login),

    path(
        'logout/',
        logout_view,
        name="logout_view"
    ),


    # =====================================================
    # ADMIN DASHBOARD
    # =====================================================

    path(
        'admin-dashboard/',
        admin_dashboard,
        name="admin-dashboard"
    ),


    # =====================================================
    # STUDENT MANAGEMENT
    # =====================================================

    path(
        "admin-dashboard/student/",
        student_page,
        name="admin-student"
    ),

    path(
        "admin-dashboard/student/add-student/",
        add_student_page,
        name="add-student"
    ),

    path(
        "admin-dashboard/student/delete/<rollno>/",
        delete_student,
        name="delete_student"
    ),

    path(
        "admin-dashboard/student/update/<rollno>/",
        update_student,
        name="update_student"
    ),


    # =====================================================
    # STAFF MANAGEMENT
    # =====================================================

    path(
        "admin-dashboard/staff/",
        admin_staff_page,
        name="admin_staff_page"
    ),

    path(
        "admin-dashboard/staff/add-staff/",
        add_staff,
        name="add_staff"
    ),

    path(
        "admin-dashboard/staff/delete/<id>/",
        delete_staff,
        name="delete_staff"
    ),

    path(
        "admin-dashboard/staff/update/<id>/",
        update_staff,
        name="update_staff"
    ),


    # =====================================================
    # SUBJECT MANAGEMENT
    # =====================================================

    path(
        "admin-dashboard/subject/",
        subject_page,
        name="subject_page"
    ),

    path(
        "admin-dashboard/subject/add-subject/",
        add_subject,
        name="add_subject"
    ),

    path(
        "admin-dashboard/subject/delete/<id>/",
        delete_subject,
        name="delete_subject"
    ),

    path(
        "admin-dashboard/subject/update/<id>/",
        update_subject,
        name="update_subject"
    ),


    # =====================================================
    # STAFF DASHBOARD / MARK ENTRY
    # =====================================================

    path(
        "staff-dashboard/",
        staff_dashboard,
        name="staff_dashboard"
    ),

    path(
        "student-mark-entry/",
        mark_entry,
        name="mark_entry"
    ),


    # =====================================================
    # STUDENT DASHBOARD
    # =====================================================

    path(
        "student-dashboard/",
        student_dashboard,
        name="student_dashboard"
    ),

    path(
        "leader-board/",
        leaderboard,
        name="leaderboard"
    ),


    # =====================================================
    # ADMIN MARK ENTRY
    # =====================================================

    path(
        "admin-dashboard/mark-entry/",
        admin_mark_entry,
        name="admin_mark_entry"
    ),


    # =====================================================
    # REPORTS
    # =====================================================

    path(
        "admin-dashboard/reports/student-report/",
        student_report,
        name="student_report"
    ),


    # =====================================================
    # DEMO
    # =====================================================

    path(
        "rashid/",
        demo,
        name="demo"
    ),


    # =====================================================
    # DJANGO ADMIN
    # =====================================================

    path(
        'admin/',
        admin.site.urls
    ),

]