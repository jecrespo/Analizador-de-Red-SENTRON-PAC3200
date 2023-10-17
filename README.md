# Sentron PAC3200 Datalog with Python

In this project you will learn how to get and storage the data from the multimeter Siemens Sentron PAC3200 by modbus TCP with Python.

You need to have your Sentron PAC3200 connected to the network and with the correct IP direction. In a PC (working as a server) you will configure a Python task, executed every time interval, to read and get data from the Sentron multimeter. In this project, we store the data in a PostgreSQL server on the same PC, but you can do whatever you want with the data.

## Get started

In the [user manual](https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf) you can look the instructions to configure the multimeter. Importan:

* You must configure the device correctly, so that from the PC where you run the Python script you can access the IP address of the multimeter.
* You must set the device in Modbus mode.

Next, you need to edit the python script, to add the parameters of your multimeter, and select what data you need to recollect.

If you want, you can configure a local PostgreSQL to store the data. Also you can save it in csv files, other databases or in the cloud.

Finally, configure a programmed task on Windows to execute the Python Script every time interval you want.

### Configure the Sentron PAC3200

  1. Connect your multimeter to network by ethernet cable.
  2. You need to look up your network address (also your gateway and find some free IP address). You can use the command ``ipconfig`` on the CMD on your pc to find the network address and the gateway, and the software [Advanced IP Scanner](https://www.advanced-ip-scanner.com) to find a free IP address.
  3. Configure your multimeter. Go to comunication menu and set the next parameters:
     * **Dir. IP** : The free IP address you found. Something like _192.168.1.100_.
     * **Dir. IP** : The free IP address you found. Something like _192.168.1.100_.
     * **Subnet**: Depend of your network configuration. Ussually will be _255.255.255.0_.
     * **Gateway**: The direction you found with _ipconfig_ command. Something like _192.168.1.1_.
     * **Protocol**: _Modbus TCP_.
  4. You can test your connection from your PC with the command `ping "ip_direction"` (change "ip_direction" with the IP direction you set on your multimeter).

### PostgreSQL

#### *Optional

We use a PostgreSQL database to store the data. PostgreSQL is a open source database system, and its totally free to install in your server. You can donwload and see how to install it in the [oficial webpage](https://www.postgresql.org/).

Once you have your PostgreSQL database installed, you need to configurate the table where you will store the data. If in the future you want to add more devices, or you need to change what measurements save, we will use a table with the columns:

| column name | data type | example |
| ---: | :---: | :---: |
| **id** | serial | 1 |
| **datetime** | timestamp without time zone | '2021-12-12 09:10:15' |
| **device** | varying(20) | 'device_01' |
| **measurement** | varying(20) | 'voltage_ab' |
| **value** | real | 438.5 |

You can use this SQL code to create the table:

```sql
CREATE TABLE sentron_pac3200_measurements
(
    measurement_id serial NOT NULL,
    datetime timestamp without time zone NOT NULL,
    device character varying(20) NOT NULL,
    measurement character varying(20) NOT NULL,
    value real NOT NULL,
    PRIMARY KEY (measurement_id)
);

COMMENT ON TABLE sentron_pac3200_measurements
    IS 'Energy measurements from Siemens Sentron PAC3200 multimeters';
```

### Python enviroment

You have two alternatives. You can download and install Python in your PC, and install the libraries for all users, or create a specific virtual enviroment for this project (recomended).

If you want to install the libraries manually, you can find the dependencies [here](requirements.txt).

#### Install Python

First, go and download Python from the [oficial webpage](https://www.python.org/downloads/release/python-3108/). We use the version 3.10.8.

<details>

<summary> Optional: Virtual Enviroment</summary>

#### Virtual enviroment

Now you need to install Virtual Enviroment. Go to a terminal (CMD) and write the command `pip install virtualenv`.

Once you have venv installed, download this project to your PC, and in the same folder, open a terminal and make a venv with the command `python venv env`.

</details>

#### Install dependencies

If you have a virtual env, activate the env from the terminal.

Now, write the command `pip install -r requirements.txt` in the same folder where you download the content of the project. In the file requirements.txt you can find the neccesary libraries of the project.

### Config parameters

Now you are ready to config your parameters.

Open the file config.py and follow the instructions to add the parameters of your database and of your multimeters. You can add more than one multimeter.

Now, you can run the main.py file, and the project is working.

### Task scheduler

Now, we are going to schedule the python script. If you are on Windows, we have the tool Task Scheduler.

1. Open the tool, and in the right select "New task".
2. Write some name and description.
3. Add new trigger, in here:
   1. Choose "One time".
   2. In advanced configuration, set "repeat each" with the interval you want. For example, 10 minutes.
   3. Set "during" in "indifinitely".
4. Add new action, in here:
   1. Set "start new program".
   2. In program or script, select the executable of Python. If you have virtual env, select the executable of the venv, if not, select the global.
   3. In arguments, add the path to the main.py file. Add the path within "". For example, "C:\Users\User\Documents\SENTRON-PAC3200-Datalog\main.py".
5. Save all and acept.

The script will be executed automatically thanks to the task scheduler. As long as the PC is turned on, the script will be running in the background, saving the information from the multimeters.

## Links

Multimeter: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx

Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf

Product manual: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf

## Extras

> [!WARNING]
> This project only works with pymodbus in the version 2.5.3. Make sure you use that version. With recent versions doesn't work.

## Wanna help?

The project is completely functional, but right now it's hard to configure. If you want to help us, the main goal is make easiest to configure the project. Some ideas are:

- [ ] Make a User Interface.
- [ ] Make a installer to with all the necesary.
- [ ] Make a service to avoid program a task.