[app]

title = ALBADR
package.name = albadr
package.domain = org.albadr

author = ALBADR

source.dir = .

source.include_exts = py,png,jpg,jpeg,ttf,json,kv,txt,html,css

source.exclude_dirs = .git,.github,.venv,venv,__pycache__,backups,reports,.kivy,.buildozer,bin

version = 1.0.0

requirements = python3,kivy==2.3.1,kivymd==1.2.0,arabic-reshaper,python-bidi,reportlab,openpyxl

orientation = portrait
fullscreen = 0

android.permissions = READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE

android.api = 35
android.minapi = 23
android.ndk_api = 23

android.archs = arm64-v8a,armeabi-v7a

android.accept_sdk_license = True

p4a.bootstrap = sdl2


[buildozer]

log_level = 2
warn_on_root = 1
