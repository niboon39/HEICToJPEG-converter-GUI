from setuptools import setup, find_packages

setup(
    name='heic_to_jpeg_converter',
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
            'heic_to_jpeg_converter=your_module:main_function',
        ],
    },
    author='Niboon',
    author_email='kokhing039@gmail.com',
    description='A simple HEIC to JPEG converter with a GUI',
    url='https://github.com/niboon39/Codewars/tree/main/Convert_HeicToJpg',
)
