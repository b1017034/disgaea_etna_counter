from setuptools import setup


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="disgaea_etna_counter",
    version="0.2.0",
    license="NYSL",
    description="エトナの避暑地に預けたコモン装備が39Lv(アイテム界29階)になるまでをカウント",
    author="b1017034",
    url="https://github.com/b1017034/disgaea_etna_counter/releases/tag/v0.2",
    install_requires=_requires_from_file('requirements.txt'),
)
