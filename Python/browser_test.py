from splinter import Browser

browser = Browser()
browser.visit('https://www.google.com')
browser.fill('q', 'splinter - python acceptance testing for web applications')


button = browser.find_by_name('btnG')
button.click()

if browser.is_text_present('Splinter — Splinter 0.7.4 documentation', wait_time=10):
    print ('Yes, found it!!')
else:
    print('NOOOO, not found !!')
    
browser.quit()

# Note that btnG is the button beside the search bar, not the OK button.
# Using the OK button is much more complicated because it seems it is not visible immediately.
# I tried in many ways but did not manage to use the OK button.
    