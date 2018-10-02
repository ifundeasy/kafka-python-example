from setuptools import setup, find_packages

setup(
    name='kafka-python-example',
    version='0.1',
    description='this is description.',
    long_description='and this is very long description.',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Topic :: Text Processing :: Linguistic'
    ],
    keywords='your, words, order',
    url='https://github.com/rappresent/kafka-python-example',
    author='afa rappresent',
    author_email='mail.vudin@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'kafka-python', 'lz4'
    ],
    include_package_data=True,
    zip_safe=False
)