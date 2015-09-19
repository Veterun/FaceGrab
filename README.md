# Facebook Image Grab: Grab everyone's Facebook profile image without login

Facebook *graph search* provides a very useful, however, a hidden way to get the full-size profile pictures of any user-id or username.

#### Note - No login/signup required to execute this script.

## Update : The library will work with user-ids only. It will not work with usernames. This is due to recent changes in Facebook API. Facebook has recently partially acknowledged this limitation in their API and have improved their API to prohibit profile picture request using the username of any user. However, this library still works for any user-id and thus serves its original purpose of getting bulk images for research purposes.

For example,
```
http://graph.facebook.com/picture?id=122&width=800
```
This url will redirect to the full-size profile image of the user-id "122". 

Similarly,
```
http://graph.facebook.com/picture?id=ankit&width=800 # This will not work now due to recent changes in the Facebook API
```
This url will redirect to the full-size profile image of the username "ankit".

This module written in python will provide a simple API or direct usage to fetch any number of full-size facebook profile images of users either mentioned as range of user-ids or a text file containing newline separated usernames. 

## Motivation

Since according to the facebook privacy policy, all of these full-size profile images are public, the script enables to obtain a huge dataset of random real images legally free of cost, especially for the purposes of research (Machine Learning, Image Processing), or maybe marketing or more. 

## Dependencies
The python modules are needed in order to use this library.
```
urllib
sys
os
datetime
json
```

## Usage
Clone the repository and use the following code.

Run the command directly from the console with command line arguments to the file fb_image.py. The command line arguments are explained as:

```
fb_image.py [filename] # This will only work if the given text file name has only user-ids and not any usernames. This is due to recent changes in the Facebook API.
fb_image.py [id1] [id2]

```
where id1 and id2 defines the range of userids whose images are to be fetched.
For example,

```sh
$ python fb_image.py example.txt # This will only work if the given text file name has only user-ids and not any usernames. This is due to recent changes in the Facebook API.
$ python fb_image.py 12 16
```
#### OR

```python
import fb_image as fb
fb.get_profile_of_id(12,16)
fb.get_profile_of_file("example.txt") # This will only work if the given text file name has only user-ids and not any usernames. This is due to recent changes in the Facebook API.
```
The above code will obtain and save the profile images of the mentioned usersids (12-16) or usernames mentioned in "example.txt" file".

#### OR

Use example.py available with the repository.
```sh
$ python example.py
```

## API
```python
import fb_image as fb
```
Import the module in your main file.
#### fb.get_profile_of_id(id1, id2)
Function to get profile images of userids from id1 to id2.
#### fb.get_profile_of_file(filename)
Function for get profile images of userids or usernames specified in the given file (usernames and userids are to be separated using newline). This will only work if the given text file name has only user-ids and not any usernames. This is due to recent changes in the Facebook API.

#### id1 is the starting userid, Type: Integer.
#### id2 is the ending userid, Type: Integer.
#### filename is the text file containing userids and usernames separated by newline, Type: String.


## Contributors

#### Author: Ankit Aggarwal

If anybody is interested in working on developing this library, fork and feel free to get in touch with me.

## License

[MIT License](https://github.com/ankitaggarwal011/facebook-image-fetcher/blob/master/LICENSE)
