from constants import currency_quotation_link as const
from utils.get_quotation import get_currency_quotation
from utils.notification_manager import set_notification
from winotify import audio


class Runner:

    @staticmethod
    def run():
        quotation = get_currency_quotation(const.LINK_CURRENCY_QUOTATION)
        windows_notification = set_notification(app_id='Quotation Query',
                                                title='USD Current value',
                                                message_notification=quotation,
                                                sound_duration='short')

        windows_notification.set_audio(audio.Reminder, loop=False)
        windows_notification.show()

