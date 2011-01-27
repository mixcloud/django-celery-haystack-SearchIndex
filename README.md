django-haystack celery powered SearchIndex
==========================================

This is a simple queued SearchIndex implementation using celery to power the queue. This is not just a drop in Django app - but you can probably just copy the classes in and use them relatively quickly.

Some notes
----------

1. In general we don't put instances on the queue - only references to them - otherwise queues grow or instances have changed by the time they are taken off the queue.
2. Because we don't put instances on the queue, deletes have to be handled in line (otherwise the instance cannot be looked up when they are pulled off the queue). This is fine if there aren't many deletes in your system.

Dependencies
------------

Not sure why you'd be looking at this if you didn't already use these...but here you go:

 * django-haystack (https://github.com/toastdriven/django-haystack, http://haystacksearch.org/)
 * celery (https://github.com/ask/celery)
 * django-celery (https://github.com/ask/django-celery)
