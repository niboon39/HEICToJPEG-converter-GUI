from setuptools import setup, find_packages

setup(
    name='HeicToJpg',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'imageio',
        'imageio[ffmpeg]',
        'pillow',
        'tkinter'
    ],
    entry_points={
        'console_scripts': [
            'HeicToJpg=your_module:main_function',
        ],
    },
    author='Niboon',
    author_email='kokhing039@gmail.com',
    description='A simple HEIC to JPEG converter with a GUI',
    url='https://github.com/niboon39/HEICToJPEG-converter-GUI',
)
