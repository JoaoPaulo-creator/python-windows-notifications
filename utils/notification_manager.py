from winotify import Notification


def set_notification(app_id: str, title: str, message_notification, sound_duration: str):
    notification = Notification(app_id=app_id,
                                title=title,
                                msg=message_notification,
                                duration=sound_duration)

    return notification
