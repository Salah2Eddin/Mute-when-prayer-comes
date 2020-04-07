# Mute when prayer comes
 Mutes your computer when prayer time comes

# How it is working:
 It uses an api provided by (https://aladhan.com) to get the prayer times \
 than it checks for prayers every half a minute \
 when there is a prayer it will mute your computer \
 for five minutes ( 300 second )

# Requirements:
1-requests library - to send POST and GET requests to APIs
>pip install requests

2-ipinfo library - if you will use the auto location script
>pip install ipinfo

3-pycaw library - controls sound
>pip install pycaw


# Note 
My api token for ipinfo is hardcoded .. so dont use it for something else.\
Just get yours from their site - it's free
>https://ipinfo.io

# License
>Do whatever you want with this script, i don't care

# Not using this anymore but just in case anybody needs this
The the scripts for the fake keyboard press - not using anymore:
>https://github.com/Paradoxis/Windows-Sound-Manager