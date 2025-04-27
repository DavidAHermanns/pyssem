Species Options
============

At the bottom of the PySSEM page, there is a button to add new species to the model. This button opens a flyout, which allows the user to enter a set of parameters that control the dynamics and propagation of the species. These options will be applied to every satellite in the created species.

Physical Properties Inputs
--------------------------

**Cd**

(Numeric Entry) [Sink] Coefficient of Drag. This parameter, along with the altitude shell of the satellite and size (radius/area/mass), determines how much of a force drag contributes to the modeled dynamics of the satellite. A larger Cd value indicates the satellite is more prone to atmospheric drag effects.

This value has historically been assumed to be ~2.2 for LEO satellites, but may be smaller or larger for certain species.

Usage:
File: `pyssem/utils/drag/drag.py`, Lines: 208–220

.. code-block:: python

    def JB2008_dens_func(t, h, density_data, date_mapping, nearest_altitude_mapping):
        # Cd is used in drag force calculations
        drag_force = 0.5 * Cd * density_values * velocity**2 * area
        return drag_force


**Mass (kg)**

(Numeric Entry) [Sink] This is the mass of the satellite. With the radius and area, this informs the drag calculation for satellites unable to station-keep against drag. The larger the mass, the slower the decay of the satellite’s orbit due to drag will occur.

Satellites and debris can vary in mass. Smallsats like a 1U CubeSat can measure around 2kg. SpaceX Starlink satellites are larger, ranging between 200kg to 1250kg depending on their versions. The International Space Station is the heaviest spacecraft currently in orbit, with a mass of approximately 450,000kg.

Usage:
File: `pyssem/utils/simulation/species_pair_class.py`, Lines: 57–65

.. code-block:: python

    # Mass is used in collision calculations to determine debris creation as the M1 and M2 values
    n_f_catastrophic = 0.1 * LC**(-1.71) * (M1 + M2)**0.75
    n_f_damaging = 0.1 * LC**(-1.71) * (min(M1, M2) * dv**2)**0.75


**Radius (m)**

(Numeric Entry) [Sink] This is the radius of the satellite. This is used to inform the area of the satellite if an area value was not provided by the user. An increased radius will increase the effect of drag on the satellite. Additionally, the radius of the satellite is used by the collision calculator in pySSEM to determine debris creation parameters in the case of a collision.

Usage:
File: `pyssem/utils/simulation/species_pair_class.py`, Lines: 102–110

.. code-block:: python

    # Radius is used to calculate the collision cross-section
    def collision_cross_section(radius1, radius2):
        # The effective collision cross-section is based on the radii of the two objects
        return np.pi * (radius1 + radius2)**2

    cross_section = collision_cross_section(species1.radius, species2.radius)


**Area (m²)**

(Numeric Entry) [Sink] This is the cross-sectional area of the satellite. An increased area will increase the effect of drag on the satellite. Additionally, the area of the satellite is used by the collision calculator in pySSEM to determine debris creation parameters in the case of a collision.

Usage:
File: `pyssem/utils/drag/drag.py`, Lines: 208–220

.. code-block:: python

    # Area is used in drag force calculations
    drag_force = 0.5 * Cd * density_values * velocity**2 * area
    return drag_force

