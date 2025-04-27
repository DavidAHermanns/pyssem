Species Functions
================

**Launch Function**  

(Text Entry) [Source] This value controls how new satellites of this species are launched into the modeled space environment. In conjunction with the ‘Launch Coefficient’, this gives pySSEM the direction for satellite launches.  

The options available for Launch Function are either [launch_func_constant] for constant launches at the rate of the launch coefficient, or [launch_func_null] for no launches for this species (such as debris).

**Impact of SEPs**:  
The SEPs define the future launch model (FLM), which determines the launch rates and distributions over time. The `launch_func_constant` function uses the launch rates derived from the SEP to assign a constant launch rate to each shell. For example, in scenarios like SEP 3 M (Space Winter), the launch rates may decrease over time, directly affecting the behavior of this function.

Usage: 
File: `pyssem/utils/launch/launch.py`, Lines: 69–79  

.. code-block:: python

    def launch_func_constant(t, h, species_properties, scen_properties):
        # Assign a constant launch rate to each shell
        Lambdadot = Matrix(scen_properties.n_shells, 1, lambda i, j: species_properties.lambda_constant)
        # Convert the Matrix of symbolic expressions to a list
        Lambdadot_list = [Lambdadot[i] for i in range(scen_properties.n_shells)]
        return Lambdadot_list


**PMD Function**  

(Text Entry) [Sink] This value controls the modeling of how satellites are disposed. In conjunction with the ‘PMD %’, this gives pySSEM the direction to dispose of satellites at each time step.  

The options available for PMD Function are either [pmd_func_sat] for PMD-enabled satellites, [pmd_func_derelict] for those satellites with PMD attempts that have been assumed to have already failed, or other custom-defined functions.

**Impact of SEPs**:  
The SEPs influence the PMD success rate by defining the sustainability efforts in each scenario. For example, in SEP 5 H (Commercial-driven Development with High Sustainability Effort), the PMD percentage and efficiency are likely higher, leading to more successful satellite disposals. Conversely, in SEP 4 (Strategic Rivalry), sustainability efforts are lower, reducing PMD success rates.

Usage:
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 245–260  

.. code-block:: python

    def pmd_func_sat(t, h, species_properties, scen_properties):
        # Calculate PMD success rate based on PMD percentage
        pmd_rate = species_properties.pmd_percentage * scen_properties.pmd_efficiency
        return pmd_rate


**Drag Function**  

(Text Entry) [Sink] This value is used to support pySSEM in drag force calculation.  

The options available for Drag Function are either [drag_func_exp] for satellites that experience drag, or [drag_func_none] for those that don’t.

Usage:  
File: `pyssem/utils/drag/drag.py`, Lines: 208–220  

.. code-block:: python

    def drag_func_exp(t, h, species_properties, scen_properties):
        # Calculate drag force based on atmospheric density and satellite properties
        drag_force = 0.5 * species_properties.Cd * scen_properties.density_model(h) * species_properties.velocity**2 * species_properties.area
        return drag_force
