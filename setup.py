from setuptools import setup
 
setup(
    name = 'flash_auth',
    packages = ['flash_auth'],
    version = '0.0.1',
    description = 'Flask Authentication.',
    author='Analytics UFCG',
    author_email='fabio.silva@ccc.ufcg.edu.br',
    url='https://sites.google.com/a/computacao.ufcg.edu.br/analytics/home',
    include_package_data=True,
    install_requires=[
        "Flask",
        "itsdangerous",
        "Jinja2",
        "MarkupSafe",
        "Werkzeug",
    ],
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX :: Linux',
        'Development Status :: 1 - Planning',
        'Environment :: Flask',
        'License :: GNU Public License v3.0',
        'Intended Audience :: Science/Research'
    ]
)
