Species Properties
================

At the bottom of the PySSEM page, there is a button to add new species to the model. This button opens a flyout, which allows the user to enter a set of parameters that control the dynamics and propagation of the species.  
These options can also be used to model debris already present in the environment, turning the ‘Active’, ‘Maneuverable’, ‘Slotted’ toggles to [Off]. Additionally, for debris, the ‘PMD %’ can be adjusted accordingly.  

Behavioral Inputs
----------------

**Active**  

(Toggle On/Off) [Sink] This parameter controls whether the satellites of the selected species are modeled to perform station keeping to control against perturbations. This selection is controlled also by other factors.

Usage:
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 636–650  

.. code-block:: python

    # Active satellites are modeled to perform station keeping
    if species.active:
        dN_dt[i] += station_keeping_force


**Maneuverable**  

(Toggle On/Off) [Sink] This parameter controls whether the satellites of the selected species are modeled to maneuver to avoid collisions. The success of the maneuverability is determined by either probabilistic models or user-defined inputs.

Usage: 
File: `pyssem/utils/collisions/collisions.py`, Lines: 324–330  

.. code-block:: python

    # Maneuverable satellites avoid collisions
    if s1.maneuverable and s2.maneuverable:
        gammas[:, 0] *= s1.alpha_active * s2.alpha_active


**Delta t (years)**  

(Numeric Entry) [Sink] This input controls the amount of time that an active satellite stays ‘active’, if that satellite’s “Post Mission Disposal” attempt were to fail (based upon the PMD percentage).

Usage:  
File: `pyssem/utils/pmd/pmd.py`, Lines: 20–30  

.. code-block:: python

    # Delta t determines the rate of PMD decay
    for k in range(scen_properties.n_shells):
        Cpmddot[k, 0] = (-1 / species_properties.deltat) * species_properties.sym[k]


**PMD (%)**  

(Slider, numeric) PMD refers to “Post Mission Disposal”. The PMD percentage is the percentage of vehicles that are disposed of (by their simulated operators) after their mission ends. If a mission fails, this value determines the disposal rate.

Usage:  
File: `pyssem/utils/pmd/pmd.py`, Lines: 46–60  

.. code-block:: python

    # PMD percentage determines the disposal rate
    pmd_rate = species_properties.pmd_percentage * scen_properties.pmd_efficiency


**Alpha**  

(Numeric Entry) This value represents the failure rate of the maneuverable satellite to perform a collision avoidance maneuver with an inactive object.  

Values for Alpha range from [0] to [1], where [0 = perfect collision avoidance, 1 = none]. A value of 0.1 would mean that 1/10 collision avoidance maneuvers fail. If Alpha is unknown for the capability, a default value may be used.

Usage:  
File: `pyssem/utils/collisions/collisions.py`, Lines: 324–330  

.. code-block:: python

    # Alpha determines collision avoidance failure rate
    if s1.trackable and s2.maneuverable:
        gammas[:, 0] *= s2.alpha


**Alpha Active**  

(Numeric Entry) This value represents the failure rate of the maneuverable satellite to perform a collision avoidance maneuver with another active, maneuverable object.  

Values for Alpha Active range from [0] to [1], where [0 = perfect collision avoidance, 1 = none]. A value of 0.1 would mean that 1/10 collision avoidance maneuvers fail. If Alpha Active is unknown for the capability, a default value may be used.

Usage:  
File: `pyssem/utils/collisions/collisions.py`, Lines: 324–330  

.. code-block:: python

    # Alpha Active determines collision avoidance failure rate between active objects
    gammas[:, 0] *= s1.alpha_active * s2.alpha_active


**Slotted**  

(Toggle On/Off) [Sink] This toggle controls whether the satellite orbits within a ‘slot’ as part of a larger constellation within the species. Slotted orbits are those which are deconflicted with other satellites in the same constellation.

Usage:  
File: `pyssem/utils/collisions/collisions.py`, Lines: 324–330  

.. code-block:: python

    # Slotted satellites reduce collision risk
    if s1.slotted and s2.slotted:
        gammas[:, 0] *= min(s1.slotting_effectiveness, s2.slotting_effectiveness)


**Slotting Effectiveness**  

(Numeric Entry) [Sink] This value determines the effectiveness of slotting for those satellites in a ‘Slotted’ Species.  

Values for Slotting Effectiveness range from [1] to [0], where [1 = perfect slotting, 0 = no slotting].

Usage:  
File: `pyssem/utils/collisions/collisions.py`, Lines: 324–330  

.. code-block:: python

    # Slotting effectiveness reduces collision risk
    gammas[:, 0] *= min(s1.slotting_effectiveness, s2.slotting_effectiveness)


**Affected by Drag**  

(Toggle On/Off) This toggle controls whether the selected species of satellite is affected by drag. If toggled on, which is a more realistic option for a LEO scenario, the propagator will consider the drag force acting on the satellites.

Usage: 
File: `pyssem/utils/drag/drag.py`, Lines: 104–120  

.. code-block:: python

    # Drag force is applied to species affected by drag
    if species.drag_effected:
        drag_force = 0.5 * species.Cd * density * velocity**2 * species.area
        dN_dt[i] += drag_force
