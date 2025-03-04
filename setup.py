from setuptools import setup

setup(
    name="napari-dinosim",
    version="0.0.4",
    description="A simple plugin to use DinoSim in napari",
    author="Aitor Gonzalez-Marfil",
    author_email="aitorgacad@gmail.com",
    license="MIT",
    url="",
    packages=["napari_dinosim"],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.9",
    install_requires=[
        "numpy",
        "magicgui",
        "qtpy",
        "torch",
        "torchvision",
        "tqdm",
        "pillow",
        "matplotlib",
        "opencv-python",
        "tifffile",
        "napari",
    ],
    extras_require={
        "testing": [
            "tox",
            "pytest",
            "pytest-cov",
            "pytest-qt",
            "napari",
            "pyqt5",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: napari",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    entry_points={
        "napari.manifest": [
            "napari-dinosim = napari_dinosim:napari.yaml",
        ],
    },
)
