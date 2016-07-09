
from hub3.views import *

class Command(NoArgsCommand):
    help = "Describe the Command Here"
    def handle_noargs(self, **options):

        try:
            # create_users(10)
            multi_thread_listener()
        except Exception as e:
            print '[error at python command]'
            print e
