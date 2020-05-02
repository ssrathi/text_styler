from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='text_styler',
    packages = ['text_styler'],
    version='1.0.0',
    author='Shyamsunder Rathi',
    author_email='shyam29@gmail.com',
    url='https://github.com/ssrathi/text_styler',
    download_url='https://github.com/ssrathi/text_styler/archive/1.0.0.tar.gz',
    description='Convert ASCII alphanumeric text to a random style using Unicode character normalization.',
    long_description=readme(),
    license='MIT',
    keywords=['unicode', 'text', 'styler', 'normalization'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Unicode',
        'Operating System :: OS Independent',
        'License :: MIT',
    ],
)