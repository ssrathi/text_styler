import setuptools

def readme():
    with open('README.md') as f:
        return f.read()

setuptools.setup(
    name='unicode_text_styler',
    packages = setuptools.find_packages(),
    version='1.0.0',
    author='Shyamsunder Rathi',
    author_email='shyam29@gmail.com',
    url='https://github.com/ssrathi/text_styler',
    download_url='https://github.com/ssrathi/text_styler/archive/1.0.0.tar.gz',
    description='Convert ASCII alphanumeric text to a random style using Unicode character normalization.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=['unicode', 'text', 'styler', 'normalization'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    python_requires='>=3',
)
