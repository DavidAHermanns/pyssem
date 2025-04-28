Overall Scenario Properties
===================

**Overview**

This page provides a description of all properties that have an effect on the simulation of the entire scenario. These properties are static throughout the entire timespan of the scenario and do not change.

Inputs
-----------

**Start Date (DD/MM/YYYY)**

(Text Entry) This is the start date of your simulation, and must be entered in the DD/MM/YYYY format.
This parameter, when paired with the ‘Simulation Duration’ parameter, determines how far into the
future the simulation will model.

Usage: 
File: `pyssem/utils/handlers/datetime_helper.py`, Lines: 267–280  

.. code-block:: python

    # Convert start date to Julian Date for time calculations
    jd_start = date_to_jd(start_date.year, start_date.month, start_date.day)
    jd_end = jd_start + simulation_duration * 365.25


**Simulation Duration (years)**

(Numeric Entry) This field is the number of years, from your chosen ‘Start Date’, that your simulation will run.

Usage:   
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 156–170  

.. code-block:: python

    # Calculate scenario times based on simulation duration
    scen_times = np.linspace(0, simulation_duration, steps)
    scen_times_dates = calculate_scen_times_dates()


**Time Steps**

(Numeric Entry) This is the number of times that the SSEM calculates changes to the environment.
Propagation from time step to time step is the method by which the model advances forward in time.
The higher the entered number of time steps, the higher fidelity the model will be, but the longer it may
take to run. This entry is paired with the ‘Simulation Duration’ parameter.

As an example, if the duration is set to 100 years, and the number of time steps is 50, then each calculation of the environment will represent years of change

Usage:   
File: `pyssem/utils/launch/launch.py`, Lines: 379–390  

.. code-block:: python

    # Generate time steps for the simulation
    time_increment_per_step = simulation_duration / steps
    time_steps = [
        start_date + timedelta(days=365.25 * time_increment_per_step * i) 
        for i in range(steps + 1)
    ]


**Maximum Altitude (km)**

(Numeric Entry) This is the maximum altitude of the simulation, measured in kilometers. This altitude is
the top height of the highest shell in the simulation. Atmospheric drag is generally lower at higher
altitudes.

Usage: 
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 95–110  

.. code-block:: python

    # Define the altitude shells based on maximum altitude
    R0 = np.linspace(min_altitude, max_altitude, n_shells + 1)
    HMid = R0[:-1] + np.diff(R0) / 2  # Midpoint of the shells


**Minimum Altitude (km)**

(Numeric Entry) This is the minimum altitude of the simulation, measured in kilometers. This altitude is
the bottom of the lowest shell in the simulation. Atmospheric drag is generally higher at lower altitudes.

Usage:  
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 95–110  

.. code-block:: python

    # Define the altitude shells based on minimum altitude
    R0 = np.linspace(min_altitude, max_altitude, n_shells + 1)
    HMid = R0[:-1] + np.diff(R0) / 2  # Midpoint of the shells


**Number of Shells**

(Numeric Entry) This is the number of shells, or bins, that satellites can move between in the simulation.
The higher the number of shells, the smaller each shell will be (and the higher fidelity the model will be),
but the longer it may take to run. This entry is paired with the ‘Maximum Altitude’ and ‘Minimum Altitude’
parameters.

As an example, if the maximum altitude is 4000km, and the minimum is 500km, and the number of shells is set to 10, then each shell will span in altitude.

Usage:  
File: `pyssem/utils/collisions/collisions.py`, Lines: 226–240  

.. code-block:: python

    # Iterate over the number of shells to calculate collision probabilities
    for shell_index in range(n_shells):
        collision_probability = calculate_collision_probability(shell_index)
