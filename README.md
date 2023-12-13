

## UNDERSTANDING THE SITUATION

The Querétaro mobility agency has provided, from its databases, files that contain information related to daily and monthly public transportation upgrades. For decision making and for a broad vision of the general panorama of public transportation in the state of Querétaro, a summary of the most relevant metrics of the different bases is necessary through the creation of a dashboard that must be fed monthly with new data, which is why an automated process is needed to achieve this goal.

## AIM

Creation of an ETL in a Python script that processes the information to be able to upload it to Power Bi and create the interactive dashboard.

## SPECIFIC OBJECTIVES

- Development and maintenance of a Python script for the ETL process
- Creation of the relational model in Power Bi
- Creation of the dashboard cloud application in Power Bi Services

## SCOPE OF THE PROJECT

This project has the scope:

- The creation of code in the Python programming language for the standardization of source data, creating a summary of summary tables, as well as its monthly maintenance or when required.
- Creation of a relational model in Power Bi, as well as DAX measures for use in the dashboard.
- Deployment of the dashboard application in Power Bi services


## METHODOLOGY

### DATA EXTRACTION

Data extraction is done directly from the compressed file in RAR format that was provided.

Decompressing the file returns three folders, one for each year, containing the monthly accruals.




Within the 2021 and 2022 folders we find a folder for each month of the year, with Excel files for each day. These files, although they have the ".xsl" extension, are essentially tables saved as html.

In addition to this type of files, there are also files in other formats or with another structure, whether accumulated daily or monthly. The Python Code has been developed for processing these different files.

### 5.1 DATA TRANSFORMATION

The Python script is designed for the end user to run the script and enter the base folder paths. This script is powered by secondary scripts that perform different actions. When running the main script, called master\_etl.py, it is necessary that the secondary scripts are stored in the same folder so that the main script does not fail when calling the others.

The first path that is asked to enter in the script is the one that will contain all the base files. This folder can be renamed, as long as the contents are the same. The structure of the files within this folder must be as follows; if this is not met, the script will show an error.

_ ** Contents of the main folder for feeding the ETL** _

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/19f9b492-02dd-4d07-8382-57b9303a58de)


It is necessary that within this inputs folder the files shown and with the same name be in the root.

Under no circumstances should the name of the folders be modified.

For the annual folders, from 2021 onwards, the structure within them must be as follows:

_ **Structure within the annual folders for years after 2020** _

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/df4e4d62-62d6-4957-a217-4d5168bb9d4c)


And inside each monthly folder you will find the daily files:

_ ** Daily content within each monthly folder for data after 2020** _

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/fa1c8f1a-f746-4e59-913e-e916645db671)


In the case of folders for the years 2020 and earlier, the structure is as follows:

_ **Monthly conglomerate files within the folders for the years prior to 2021.** _

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/c4021c94-1e05-4886-8220-f291819e4947)


As you will notice, in these years there are only monthly accruals.

When the script starts, a screen like the following will be displayed, just follow the steps and the ETL process will be finished:

_ **Python Script Terminal where the paths for the process are provided** _
![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/6cde33cc-7241-4954-8f98-25601d7979b8)

You yourself will notice the end of the process since the script indicates it.

In the folder you indicated to save the files, you will find the following:

_ **Normalized files after the end of the process, inside the Outputs folder** _

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/77f26981-6084-4de7-98b0-88fa23425aa4)


The files returned by the script are necessary for building the relational model in Power Bi, in addition to some others that are processed in Power Query. The following table shows different files that are needed for the dashboard, their origin and use.

_ **Origin and description of the files that are uploaded to Power Bi.** _

| FILE | DESCRIPTION | ORIGIN / TREATMENT |
| --- | --- | --- |
| Projections\_AMEQ.csv | In this file you will find the projections made by the actuaries by route | This CSV format is reached through a script called: projection\_ameq2023.py Which is based on the file: 01. Projection\_AMEQ\_Jan2023 (2).xlsx |
| FACT\_accumulated\_DL\_v2.csv | This file is the accumulated total coming from the main ETL | Its origin is the python script called: master\_etl.py In power query no specific treatments are carried out |
| DIM\_concept.csv | Concept dimensional file for income table | Its source is the Python file master\_etl.py. In power query the concept "Fixed service cost" is filtered with ID 13 |
| FACT\_income\_costs.csv | Fact Table | Its origin is a .csv that was once provided, this one has the name: revenue\_costs.csv. This file, in turn, is fed to the main ETL to build a dimensional table and be mapped, the file that is responsible for this is: master\_etl.py |
| DIM\_patio\_base.csv | Dimensional table | Its origin is the master\_etl.py script, in power query empty strings are replaced with "Not specified" |
| 20\_9\_2023\_weighted\_without\_routes\_df(9).csv | Main file of the weighted base, in which you can find promotions and income. Used to compare the predictions of the models and also to compare the other base of promotions. (Settlement journal) | The csv file is generated from a script weighted\_9.py which is integrated into the main script master\_etl.py. Its origin is the file "weighted_rate (11 V20).xlsx" |
| Dim\_routes.csv | Dimensional file | No modifications are made in power query |
|

These files can be saved in different paths, but it is recommended to save all the files necessary for the dashboard within the same folder, for better organization. You can always query the source or source path of a query in Power Query by viewing the initial step in the Power Query step sequence.

_ **Relational model created in Power Bi** _
![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/d9e618ed-2ec4-4203-99e4-718b7b7bf138)


## DELIVERABLES

### 6.1 SCRIPT

1. The main script used, plus secondary scripts that were used for function creation
2. Dashboard pbix file
3. Deployment in Power Bi services

### 6.2 DASHBOARD

The dashboard is divided into different sections
![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/1dab5477-ab63-4f0c-867e-7089c63e09fd)

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/9935665b-fbaa-4afa-a13f-525a8da70f53)

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/4cffd573-5402-4c55-a2a6-efb966fcb4d8)

![image](https://github.com/Alchem1s7/AMEQ/assets/100399598/c0aac845-f08c-498c-be4e-7fb70f2a1a8b)






