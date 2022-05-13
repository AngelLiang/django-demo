from setuptools import setup, find_packages


setup(
    name='django-river-patch',
    version='0.1',
    author='Angel Liang',
    packages=find_packages(),
    install_requires=[
        "Django",
        'django-river',
        "django-tables2",
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
)
