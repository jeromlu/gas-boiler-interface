from setuptools import setup

requirements = [
    # TODO: put your package requirements here
]

setup(
    name='Gas boiler interface',
    version='0.0.1',
    description="PyQt5 GUI application to control and monitor Viessman gas boiler.",
    author="Luka",
    author_email='luka.jeromel1@gmail.com',
    url='https://github.com/jeromlu/Gas boiler interface',
    packages=['gas_boiler_interface', 'gas_boiler_interface.images',
              'gas_boiler_interface.tests'],
    package_data={'gas_boiler_interface.images': ['*.png']},
    entry_points={
        'console_scripts': [
            'CareVi=gas_boiler_interface.gas_boiler_app:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='Gas boiler interface',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
