import datetime

# You could replace these with inputs for more flexibility
num_posts = 3
post_folder = "./Content"
title = ""
description = ""
hash_tags = ""

# Best times to post
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

# Get videos

# Schedule videos w/ correct titles/descriptions/times

    # instagram
    
    # youtube

    # tiktok
    