import fb_image as fb
fb.get_profile_of_id(12,16)
fb.get_profile_of_file("example.txt") # This will only work if the given text file name has only user-ids and not any usernames. This is due to recent changes in the Facebook API.
