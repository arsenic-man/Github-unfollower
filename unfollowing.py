from selenium import webdriver

firefox = webdriver.Firefox(executable_path="./geckodriver")


def finnish(a):
    if a == 0:
        print("You don't have any following")
    elif a == 1:
        print("Unfollowed successfully !!!")




def unfollow(username, unfollow_num):

    a = "https://github.com/"+username+"?tab=following"
    firefox.get(a)

    unfollow_button = firefox.find_elements_by_xpath("//input[@value='Unfollow']")

    if len(unfollow_button) == 0:
        finnish(0)
    elif unfollow_num <= len(unfollow_button):
        b = unfollow_num
    else:
        b = len(unfollow_button)
    for i in range(0, b):

        unfollow_button[i].click()
        c = str(i+1) + " accounts unfollowed and " + str(b-i-1) + " following remaining and you have " +\
            str(len(unfollow_button)-i-1) + " following at all"
        print(c)

    finnish(1)



def start():
    firefox.get("https://github.com/login")
    enter = input("press Enter button after Log-in to your Github account ")
    username = input("Enter your username : ")
    unfollow_num = int(input("Number of unfollowing (type 0 for all) : "))
    unfollow(username, unfollow_num)


start()
