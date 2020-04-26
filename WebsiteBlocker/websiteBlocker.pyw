import time
from datetime import datetime as dt

#path_for_host_file = r"C:\Windows\System32\drivers\etc\hosts"
path_for_host_file = r"C:\Users\GINNI\AppData\Local\Programs\Python\Python37-32\Scripts\WebsiteBlocker\hosts"

redirect = "120.0.0.1"
website_list = ["www.facebook.com","facebook.com"]

# Script will keep checking and add the website blocking list to host file whenever time is from 8.a.m to 4 a.m
#WE need to open the hosts file and write to it.
while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) > dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(path_for_host_file,"r+") as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    print("nothing to do")
                    pass
                else:
                    file.write(redirect + " " + website+"\n")
                    print("Add the list to content")
        print("Working hours")
    # We need to open the hosts file and check if it has list of blocked websites.
    # Read the file line by line and see if the list of websites does not exist in that line,
    # then we keep on writing line by line.But we put the cursor on top before writing,
    # So that our new file content gets written first.And rest we can truncate.
    # But if it exists, then we move the pointer to start of file and do the same thing again
    # (write the file until that list of website comes)

    else:
        with open(path_for_host_file, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("non working hours")
    time.sleep(5)


