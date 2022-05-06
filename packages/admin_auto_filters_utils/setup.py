from setuptools import setup


setup(
    name='admin_auto_filters_utils',  # 包名称
    version='0.1.0',  # 版本
    license='MIT',
    description='admin_auto_filters_utils',
    platforms='any',
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'django-autocomplete-light',
        'django-admin-autocomplete-filter',
    ],
)
