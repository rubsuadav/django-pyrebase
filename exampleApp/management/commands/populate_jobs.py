from django.core.management.base import BaseCommand
from ...firebase import firestore
from ...scrapping import scrapp_jobs
from tqdm import tqdm
from colorama import Fore, Style


class Command(BaseCommand):
    help = 'Populate database firestore'

    def handle(self, *args, **options):
        jobs = scrapp_jobs()
        with tqdm(total=len(jobs), desc='Populating database') as pbar:
            for i, job in enumerate(jobs):
                firestore.collection(u'jobs').add(job)
                pbar.update(1)

                # Calcute % completed
                percent_complete = (i + 1) / len(jobs) * 100

                # Change the color of the progress bar according to the percentage completed
                if 0 <= percent_complete <= 25:
                    color = Fore.RED
                elif 25 < percent_complete <= 50:
                    color = Fore.YELLOW
                elif 50 < percent_complete <= 75:
                    color = Fore.GREEN
                else:
                    color = Fore.BLUE

                # Update the style of the description bar
                pbar.set_description(
                    f'{color}Populating database{Style.RESET_ALL}')

        self.stdout.write(self.style.SUCCESS(
            '\n Successfully populated database'))
