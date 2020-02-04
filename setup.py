from distutils.core import setup

def main():

    setup(
        name = 'followname',
        packages=['followname'],
        package_dir = {'':'src'},
        version = open('VERSION.txt').read().strip(),
        author='Stuart Lynne',
        author_email='stuart.lynne@gmail.com',
        url='http://github.com/six8/pyfollowname',
        download_url='http://github.com/stuartlynne/pyfollowname',
        license='MIT',
        keywords=['tail', 'follow'],
        description='Python tail is a simple implementation of GNU tail --follow=name.',
        classifiers = [
            "Programming Language :: Python",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Developers",
            "Intended Audience :: System Administrators",
            "Operating System :: POSIX",
            "License :: OSI Approved :: MIT License",
            "Natural Language :: English",
            'Topic :: System :: Logging',
            'Topic :: Text Processing',
            "Topic :: Software Development :: Libraries :: Python Modules",
            "Topic :: System :: System Shells",
            "Topic :: System :: Systems Administration",
        ],
        long_description=open('README.rst').read(),
        entry_points = {
            'console_scripts': [
                'followname = followname:main',
            ],
        },
    )

if __name__ == '__main__':
    main()
