

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

_ **Figure 1. Example of decompressing the RAR file** _

![](RackMultipart20231213-1-mrl30f_html_bdfed3649ab3e4c9.png)

Within the 2021 and 2022 folders we find a folder for each month of the year, with Excel files for each day. These files, although they have the ".xsl" extension, are essentially tables saved as html.

In addition to this type of files, there are also files in other formats or with another structure, whether accumulated daily or monthly. The Python Code has been developed for processing these different files.

### 5.1 DATA TRANSFORMATION

The Python script is designed for the end user to run the script and enter the base folder paths. This script is powered by secondary scripts that perform different actions. When running the main script, called master\_etl.py, it is necessary that the secondary scripts are stored in the same folder so that the main script does not fail when calling the others.

_ **Figure 2. Scripts required for the ETL** _

![](RackMultipart20231213-1-mrl30f_html_2cf7cae0bf472fa1.png)

The first path that is asked to enter in the script is the one that will contain all the base files. This folder can be renamed, as long as the contents are the same. The structure of the files within this folder must be as follows; if this is not met, the script will show an error.

_ **Figure 3. Contents of the main folder for feeding the ETL** _

![](RackMultipart20231213-1-mrl30f_html_b0fad902f906152d.png)

It is necessary that within this inputs folder the files shown and with the same name be in the root.

Under no circumstances should the name of the folders be modified.

For the annual folders, from 2021 onwards, the structure within them must be as follows:

_ **Figure 4. Structure within the annual folders for years after 2020** _

![](RackMultipart20231213-1-mrl30f_html_953f4478eed83029.png)

And inside each monthly folder you will find the daily files:

_ **Figure 5. Daily content within each monthly folder for data after 2020** _

![](RackMultipart20231213-1-mrl30f_html_ec9ec7a22c1d0eab.png)

In the case of folders for the years 2020 and earlier, the structure is as follows:

_ **Figure 6. Monthly conglomerate files within the folders for the years prior to 2021.** _

![](RackMultipart20231213-1-mrl30f_html_187b44ef3c392ff2.png)

As you will notice, in these years there are only monthly accruals.

When the script starts, a screen like the following will be displayed, just follow the steps and the ETL process will be finished:

_ **Figure 7. Python Script Terminal where the paths for the process are provided** _

![](RackMultipart20231213-1-mrl30f_html_91c1b545bed48e1a.png)

You yourself will notice the end of the process since the script indicates it.

In the folder you indicated to save the files, you will find the following:

_ **Figure 8. Normalized files after the end of the process** _

![](RackMultipart20231213-1-mrl30f_html_34d0dd2c07328204.png)

The files returned by the script are necessary for building the relational model in Power Bi, in addition to some others that are processed in Power Query. The following table shows different files that are needed for the dashboard, their origin and use.

_ **Table 1. Origin and description of the files that are uploaded to Power Bi.** _

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
  |
  |
  |

These files can be saved in different paths, but it is recommended to save all the files necessary for the dashboard within the same folder, for better organization. You can always query the source or source path of a query in Power Query by viewing the initial step in the Power Query step sequence.

_ **Figure 9. Example of the origin step for uploading files in Power Bi** _

![Shape2](RackMultipart20231213-1-mrl30f_html_1c47d5835df7af45.gif) ![Shape1](RackMultipart20231213-1-mrl30f_html_27b8bf2272ec589e.gif) ![](RackMultipart2023121 3-1-mrl30f_html_bcc0b34b7ca31eee.png)

_ **Figure 10. Relational model created in Power Bi** _

![](RackMultipart20231213-1-mrl30f_html_d7fc40676072f8cf.png)

## DELIVERABLES

### 6.1 SCRIPT

1. The main script used, plus secondary scripts that were used for function creation
2. Dashboard pbix file
3. Deployment in Power Bi services

### 6.2 DASHBOARD

The dashboard is divided into different sections



