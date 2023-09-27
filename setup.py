import setuptools

setuptools.setup(

    include_package_data = True,
    name="loan eligibility prediction",
    author_name = "Daram Nikhil",
    author_email = "nikhildaram51@gmail.com",
    description="loan_eligibility prediction app",
    packages = setuptools.find_packages(),
    install_requires =["pandas","flask"],
    long_description = "loan eligibility prediction project",
    classifiers = [
    
        "Programming language : : Python : : 3",
        "Operating System : : Linux"
        ]


)