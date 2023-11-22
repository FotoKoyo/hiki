from plyer import notification

def show_notification(title, message):
    notification.notify(title=title,
                        message=message,
                        timeout=5,
                        app_icon='pictures\Stock_Helper.ico')
    
show_notification('Stock Helper','Продукты!')