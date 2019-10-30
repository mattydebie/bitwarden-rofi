from setuptools import setup

setup(
    name="bwm",
    version="0.0.1",
    py_modules=["bwm"],
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        bwm=bwmenu:cli
    '''
)