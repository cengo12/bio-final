
# CENG460 - INTRODUCTION TO BIOINFORMATIC FINAL PROJECT

## Introduction

In this project our goal was to find all possible **Primer Designs** for PCR
(Polymerase Chain Reaction), based on predefined conditions in the project announcement. 

## Primer Conditions

- Length of a primer should be between 18 and 30 bases.
- G and C content of a primer should be between 40% and 60%.
- Primer must end with base G or C.
- Melting temperature(*Tm*) of a primer must be between 55°C and 65°C.  Also, forward primer and reverse primer's *Tm* should be within 5°C of each other.
- Runs of four bases should be avoided. (Such as: AAAA or TTTT)
- Runs of four dinucleotides should be avoided. (Such as: ATATATAT)
- Intra-primer homology should be avoided. It means that, no more than three bases and their complementaries should not exist.
- Inter-primer homology should be avoided. It means that forward primers and reverse primers should not have complementary sequences. 

## Application

This tool takes input either as NCBI ID and calls for gene sequence from NCBI Database, or as text input in fasta file format. Then all possible **forward primers gets listed in blue block** with their index numbers(locations) according to the gene sequence provided. Each forward primer in this block **can be clicked** to list all of their possible **reverse primers in the orange section**.

![image](https://github.com/cengo12/bio-final/blob/main/sample%20images/UIimage.png)

## Source Code

For the main logic of the primer finding, no external libraries or frameworks are used. Only Entrez API is used in order to get gene sequence from NCBI database with ID.

Main logic of this application is written in python, and can be found in app.py file which is located at ["./src/backend/app.py"](https://github.com/cengo12/bio-final/blob/main/src/backend/app.py). For the user interface, React Js library is used. Corresponding source code to React can be found inside "./src/frontend/". For establishing communication of "app.py" and "React Ui", Flask web framework is used as backend. Files for the flask is located at ".src/backend/" directory.

## Deployment

This project can be deployed to web as a web application, or as a local desktop app like the version in the releases.

For deploying a local version, pywebview is used. You can follow the steps, and examples from https://pywebview.flowrl.com/.
