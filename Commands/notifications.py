from win10toast import ToastNotifier    
toaster = ToastNotifier()


def TestNotification():
    toaster.show_toast("Hello world!","Successful test!")