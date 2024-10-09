import datetime
import os
import shutil

from youtube import upload_video

# You could replace these with inputs for more flexibility
num_posts = 3
src_folder = "./Content"
used_folder = "./Content/Used"
title = ""
description = ""
tags = ""
category_id = ""

# Best times to post (This is not generic, obviously only works for 3 daily posts)
current_date = datetime.datetime.now()
day_of_week = current_date.day_of_week = current_date.strftime("%A")
match day_of_week:
    case "Monday":
        times_to_post = (6, 10, 22)
    case "Tuesday":
        times_to_post = (3, 4, 9)
    case "Wednesday":
        times_to_post = (7, 9, 23)
    case "Thursday":
        times_to_post = (9, 12, 19)
    case "Friday":
        times_to_post = (5, 14, 16)
    case "Saturday":
        times_to_post = (11, 19, 20)
    case _:  # default case (and Sunday)
        times_to_post = (8, 11, 16)

# Get videos and schedule w/ descirptions & times
mp4_files = [f for f in os.listdir(src_folder) if f.endswith('.mp4')]
mp4_files.sort()  # alphabetical

for i in range(0, num_posts):
    #get file path
    file = mp4_files[i]
    file_path = os.path.join(src_folder, file)
    # instagram
    
    # youtube
    upload_video(file_path, title, description, tags, category_id, times_to_post[i])
    # tiktok

    # move the file to the used folder
    shutil.move(file_path, os.path.join(used_folder, file))
    
