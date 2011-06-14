from setuptools import setup, find_packages

setup(
    name='django-celery-haystack-index',
    packages=find_packages(),
    include_package_data=True,
    description='Celery Haystack SearchIndex',
    long_description=open('README.md').read(),
    zip_safe=False, # because we're including media that Django needs
)

