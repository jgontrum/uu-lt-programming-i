from setuptools import setup

setup(
    name='arpabet',
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'ipa_file = arpabet.scripts:ipa_file'
        ]
    }
)
