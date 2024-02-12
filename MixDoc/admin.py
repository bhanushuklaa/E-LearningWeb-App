from django.contrib import admin
from .models import Resume

# Register your models here.
from .models import *


class contactusAdmin(admin.ModelAdmin):
    list_display = ("fullname", "email", "number", "message")
    list_per_page = 4
    list_editable = ("email", "number", "message")
    search_fields = ("number",)
    list_filter = ("fullname",)


admin.site.register(contact, contactusAdmin)


class webcardAdmin(admin.ModelAdmin):
    list_display = ("id", "cardname", "cardpic", "cardlink")
    list_per_page = 4
    search_fields = ("id", "cardname")
    list_editable = ("cardname",)
    list_filter = ("cardpic",)


admin.site.register(webcard, webcardAdmin)


class youTubeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "video",
        "vtitle",
        "vdiscription",
        "vchannel",
        "vuploaded",
        "vlink",
    )


admin.site.register(youTube, youTubeAdmin)


class freeCardAdmin(admin.ModelAdmin):
    list_display = ("id", "freeicon", "freetitle", "freelink")
    list_per_page = 4
    search_fields = ("freetitle",)
    list_editable = (
        "freetitle",
        "freelink",
    )
    list_filter = ("freetitle",)


admin.site.register(freeCard, freeCardAdmin)


"""class videoGalleryAdmin(admin.ModelAdmin):
    list_display = ("youtubevideo","videotitle", "videodiscp", "videochannel", "videotime", "videolink")
admin.site.register(videoGallery,videoGalleryAdmin)"""


class osAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "os_img",
        "os_title",
        "os_discription",
        "os_moreinfo",
        "os_download",
    )
    list_per_page = 4
    list_editable = (
        "os_title",
        "os_discription",
        "os_download",
    )
    list_filter = ("os_title",)
    search_fields = ("os_title",)


admin.site.register(os, osAdmin)


class os1Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "os_img1",
        "os_title1",
        "os_discription1",
        "os_moreinfo1",
        "os_download1",
    )
    list_per_page = 4
    list_editable = (
        "os_title1",
        "os_discription1",
        "os_download1",
    )
    list_filter = ("os_title1",)
    search_fields = ("os_title1",)


admin.site.register(os1, os1Admin)


class os2Admin(admin.ModelAdmin):
    list_display = (
        "id",
        "os_img2",
        "os_title2",
        "os_discription2",
        "os_moreinfo2",
        "os_download2",
    )
    list_per_page = 4
    list_editable = (
        "os_title2",
        "os_discription2",
        "os_download2",
    )
    list_filter = ("os_title2",)
    search_fields = ("os_title2",)


admin.site.register(os2, os2Admin)


@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "dob",
        "gender",
        "locality",
        "city",
        "pin",
        "state",
        "mobile",
        "job_city",
        "skills",
        "projects",
        "intro",
        "qulification",
        "clg_name",
        "percentage",
        "profile_image",
        "my_file",
    ]
    list_per_page = 4
    list_filter = ("name",)
    search_fields = ("name",)
    list_editable = (
        "name",
        "locality",
        "city",
        "mobile",
        "job_city",
        "skills",
        "projects",
        "intro",
        "profile_image",
    )


class newscardAdmin(admin.ModelAdmin):
    list_display = ("id", "newsname", "newspic", "newslink")
    list_per_page = 4
    list_editable = (
        "newsname",
        "newslink",
    )
    list_filter = ("newsname",)
    search_fields = ("newsname",)


admin.site.register(newscard, newscardAdmin)


class newscard1Admin(admin.ModelAdmin):
    list_display = ("id", "newsname1", "newspic1", "newslink1")
    list_per_page = 4
    list_editable = (
        "newsname1",
        "newslink1",
    )
    list_filter = ("newsname1",)
    search_fields = ("newsname1",)


admin.site.register(newscard1, newscard1Admin)


class newscard2Admin(admin.ModelAdmin):
    list_display = ("id", "newspic2", "newsname2", "newslink2")
    list_per_page = 4
    list_editable = (
        "newsname2",
        "newslink2",
    )
    list_filter = ("newsname2",)
    search_fields = ("newsname2",)


admin.site.register(newscard2, newscard2Admin)


class newscard3Admin(admin.ModelAdmin):
    list_display = ("id", "newspic3", "newsname3", "newslink3")
    list_per_page = 4
    list_editable = (
        "newsname3",
        "newslink3",
    )
    list_filter = ("newsname3",)
    search_fields = ("newsname3",)


admin.site.register(newscard3, newscard3Admin)


class newscard4Admin(admin.ModelAdmin):
    list_display = ("id", "newspic4", "newsname4", "newslink4")
    list_per_page = 4
    list_editable = (
        "newsname4",
        "newslink4",
    )
    list_filter = ("newsname4",)
    search_fields = ("newsname4",)


admin.site.register(newscard4, newscard4Admin)


class templateResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "temp_pic", "temp_download")
    list_per_page = 4
    list_filter = ("temp_pic",)
    list_editable = (
        "temp_pic",
        "temp_download",
    )
    search_fields = ("temp_pic",)


admin.site.register(templateResume, templateResumeAdmin)
