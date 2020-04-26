"""ReEntryApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
# auth_views used for password reset and change
from django.contrib.auth import views as auth_views
from django.urls import path
from NewEra import views

urlpatterns = [
    # Admin site (likely will be unused by admins)
    path('admin/', admin.site.urls), # Django Server route for entity management (avail to staff & superusers)

    # General routes
    path('', views.home, name='Home'),  # All users
    path('login/', views.login, name='Login'),  # Visitors (anyone not logged in) only
    path('logout/', views.logout, name='Logout'),   # Staff (SOWs) and superuser (admin) only
    path('about/', views.about, name='About'),  # All users

    # Dashboard (previously Manage Users)
    path('manage_users/', views.manage_users, name='Manage Users'), # Superuser only

    # User actions
    path('users/<int:id>/edit', views.edit_user, name='Edit User'), # Staff only
    path('users/<int:id>/delete', views.delete_user, name='Delete User'),   # Staff only

    # Resource actions
    path('resources/', views.resources, name='Resources'),  # All users
    path('resources/new/', views.create_resource, name='Create Resource'),  # Superusers only
    path('resources/<int:id>', views.get_resource, name='Show Resource'),   # All users
    path('resources/<int:id>/edit/', views.edit_resource, name='Edit Resource'),    # Superusers only
    path('resources/<int:id>/delete/', views.delete_resource, name='Delete Resource'),  # Superusers only

    # Resource image action
    path('image/<int:id>', views.get_resource_image, name='Image'), # All users

    # Tag actions
    path('tags/', views.tags, name='Tags'), # Superusers only
    path('tags/new', views.create_tag, name='Create Tag'),  # Superusers only
    path('tags/<int:id>/edit/', views.edit_tag, name='Edit Tag'),   # Superusers only
    path('tags/<int:id>/delete/', views.delete_tag, name='Delete Tag'), # Superusers only

    # Referral actions
    path('referrals/', views.referrals, name='Referrals'),  # Staff and superusers only
    path('create_referral/', views.create_referral, name='Create Referral'),    # Staff and superusers only
    path('referrals/<int:id>/', views.get_referral, name='Show Referral'),  # Staff and superusers only
    path('referrals/<int:id>/edit/', views.edit_referral_notes, name='Edit Referral Notes'),    # Staff and superusers only
    
    # Case load actions
    path('case_load/', views.case_load, name='Case Load'),  # Staff and superusers only
    path('case_load/<int:id>', views.get_case_load_user, name='Show Case Load User'),   # Staff and superusers only
    path('case_load/<int:id>/edit/', views.edit_case_load_user, name='Edit Case Load User'),    # Staff and superusers only
    path('case_load/<int:id>/delete/', views.delete_case_load_user, name='Delete Case Load User'),  # Staff and superusers only
    
    # Resource data export action
    path('export', views.export_data, name='Export Data'),  # Superusers only
    path('resetViews', views.resetViews, name='Reset Views'),   # Superusers only

    # https://www.youtube.com/watch?v=qjlZWBbX7-o
    # https://www.youtube.com/watch?v=sFPcd6myZrY
    # Password change
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name='NewEra/password_change.html'), name='password_change'),   # Staff only
    path('change_password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='NewEra/password_change_done.html'), name='password_change_done'),    # Staff only

    # Password reset
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='NewEra/password_reset.html'), name='reset_password'),   # All users
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name='NewEra/password_reset_done.html'), name='password_reset_done'),    # All users
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='NewEra/password_reset_form.html'), name='password_reset_confirm'),   # Emailed user only
    path('reset_password/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='NewEra/password_reset_complete.html'), name='password_reset_complete'),    # Emailed user only
]
