
----
## Project structure
    .
    ├── Moat_Automation
    ├   ├── src                             (source folder)
    │       ├── __init__.py
    │       ├── conftest.py             (pytest fixture, setUp/tearDown)
    │       |
    │       ├── pages                   (Page objects package)
    │       │   ├── __init__.py
    │       │   ├── base_page.py        (abstract page for all other pages)
    │       │   ├── moat_page.py       
    │       │   ├── search_resuklt_page.py       (example for other pages)
    │       │   └── ...
    │       │
    │       │
    │       └── tests                   (executable test scnearios package)
    │           ├── __init__.py
    │           ├── test_creative_count_on_serch_resultspage.py
    │           ├── test_moat_autocomplete.py
    │           └── test_random_brand.py
    │           └── test_verify_share_ad.py
    │
    ├── .gitignore
    ├── README.md                   (Project index)
    └──  requiremenets.txt           (list of dependencies, can be installed with `pip install -r requiremenets.txt`)


-----


## Instructions to run
Note: 
1.will need to have python 3.7, Pytest, selenium on machine
2.Need to have chromedriver in Path variables 
3.Need to have PYTHONPATH in systemvariables set to "C:\{YOUR dIR Name} \PycharmProjects\Moat_Automation" 

### Running with pytest only
Go to command promt 
go to "C:\{YOR DIR} \PycharmProjects\Moat_Automation"
run  pytest --disable-pytest-warnings
