Advanced Options
----------------
These parameters are able to be changed once the slider at the top right of the page is switched.

**Integrator Type**

(Text Entry) This value is the type of integrator that pySSEM uses to propagate the current state of the
model to the subsequent state of the model, over a time step (of size determined by the ‘Simulation
Duration’ and ‘Time Steps’ values).

The default value is [BDF].

Example usage:
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 561–576

.. code-block:: python

    from scipy.integrate import solve_ivp

    output = solve_ivp(
        self.population_shell_time_varying_density,
        [self.scen_times[0], self.scen_times[-1]],
        x0,
        args=(full_lambda_flattened, equations, self.scen_times),
        t_eval=self.scen_times,
        method=self.integrator  # Integrator type
    )


**Density Model**

(Text Entry) [Sink] This is the atmospheric density model that controls how pySSEM models the drag
effect against satellites in a species.

The default value is [static_exp_dens_func], which uses pre-computed density values at specific layers
to return atmospheric density for each bin altitude. These densities are returned to the Drag Function
for each species to find drag forces.

Example usage:
File: `pyssem/utils/drag/drag.py`, Lines: 104–120

.. code-block:: python

    from pyssem.utils.drag.drag import drag_func_exp

    upper_term, current_term = drag_func_exp(
        t, h, species, scen_properties
    )


**Launch Coefficient**

(Numeric Entry) [Source] In conjunction with the ‘Launch Function’ of each species, this gives pySSEM
the direction to add more satellites (or not) at each time step.

The default value is [0.1].

Additionally, the Space Environment Pathways (SEPs) influence the launch coefficient and future launch model.

Example usage:
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 688–698

.. code-block:: python

    # Used in the population_shell method to calculate launch rates
    increase = np.interp(t, times, full_lambda[i])
    dN_dt[i] += 0 if np.isnan(increase) else increase


**Impact Velocity (km/s)**

(Numeric Entry) [Sink] This is the assumed relative velocity of the two objects paired together for
collision calculation, and is held constant across the simulation.

The default value is [10] km/s. For reference, the active Iridium 33 satellite and the derelict Cosmos
2251 had a relative speed of approximately 11.7 km/s when they collided in 2009.

Example usage:
File: `pyssem/utils/simulation/scen_properties.py`, Lines: 102–107

.. code-block:: python

    if self.v_imp is not None:
            self.v_imp2 = self.v_imp * np.ones_like(self.V)  # impact velocity [km/s] Shell-wise
    else: 
        # Calculate v_imp for each orbital shell using the vis viva equation
        self.v_imp2 = np.sqrt(2 * self.mu / (self.HMid * 1000)) / 1000  # impact velocity [km/s] Shell-wise
    self.v_imp2 * 1000 * (24 * 3600 * 365.25)  # impact velocity [m/year]
