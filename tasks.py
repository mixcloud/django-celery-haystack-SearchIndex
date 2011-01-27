from django.db.models.loading import get_model

from haystack import site
from haystack.management.commands import update_index

from celery.task import Task, PeriodicTask
from celery.task.schedules import crontab

class SearchIndexUpdateTask(Task):
    name = "search.index.update"
    routing_key = 'search.index.update'
    default_retry_delay = 5 * 60
    max_retries = 1

    def run(self, app_name, model_name, pk, **kwargs):
        logger = self.get_logger(**kwargs)
        try:
            model_class = get_model(app_name, model_name)
            instance = model_class.objects.get(pk=pk)
            search_index = site.get_index(model_class)
            search_index.update_object(instance)
        except Exception, exc:
            logger.error(exc)
            self.retry([app_name, model_name, pk], kwargs, exc=exc)

class SearchIndexUpdateTask(PeriodicTask):
    routing_key = 'periodic.search.update_index'
    run_every = crontab(hour=4, minute=0)

    def run(self, **kwargs):
        logger = self.get_logger(**kwargs)
        logger.info("Starting update index")
        # Run the update_index management command
        update_index.Command().handle()
        logger.info("Finishing update index")

