"""An example compas_fea package use for truss elements."""

from compas_fea.cad import rhino

from compas_fea.structure import ElementProperties
from compas_fea.structure import GeneralStep
from compas_fea.structure import GravityLoad
from compas_fea.structure import PinnedDisplacement
from compas_fea.structure import PointLoad
from compas_fea.structure import Steel
from compas_fea.structure import Structure
from compas_fea.structure import TrussSection


__author__     = ['Andrew Liew <liew@arch.ethz.ch>']
__copyright__  = 'Copyright 2017, BLOCK Research Group - ETH Zurich'
__license__    = 'MIT License'
__email__      = 'liew@arch.ethz.ch'


# Create empty Structure object

mdl = Structure(name='truss_frame', path='C:/Temp/')

# Add truss elements

layers = ['elset_main', 'elset_diag', 'elset_stays']
rhino.add_nodes_elements_from_layers(mdl, element_type='TrussElement', layers=layers)

# Add node and element sets

layers.extend(['nset_pins', 'nset_load_v', 'nset_load_h'])
rhino.add_sets_from_layers(mdl, layers=layers)

# Add materials

mdl.add_material(Steel(name='mat_steel', fy=355))

# Add sections

mdl.add_section(TrussSection(name='sec_main', A=0.0200))
mdl.add_section(TrussSection(name='sec_diag', A=0.0050))
mdl.add_section(TrussSection(name='sec_stays', A=0.0010))

# Add element properties

ep1 = ElementProperties(material='mat_steel', section='sec_main', elsets='elset_main')
ep2 = ElementProperties(material='mat_steel', section='sec_diag', elsets='elset_diag')
ep3 = ElementProperties(material='mat_steel', section='sec_stays', elsets='elset_stays')
mdl.add_element_properties(ep1, name='ep_main')
mdl.add_element_properties(ep2, name='ep_diag')
mdl.add_element_properties(ep3, name='ep_stays')

# Add loads

mdl.add_load(PointLoad(name='load_pl_v', nodes='nset_load_v', z=-250000))
mdl.add_load(PointLoad(name='load_pl_h', nodes='nset_load_h', x=500000))
mdl.add_load(GravityLoad(name='load_gravity', elements='elset_all'))

# Add displacements

mdl.add_displacement(PinnedDisplacement(name='disp_pinned', nodes='nset_pins'))

# Add steps

loads = ['load_pl_v', 'load_pl_h', 'load_gravity']
mdl.add_step(GeneralStep(name='step_bc', displacements=['disp_pinned']))
mdl.add_step(GeneralStep(name='step_loads', loads=loads, factor=1.5))
mdl.set_steps_order(['step_bc', 'step_loads'])

# Structure summary

mdl.summary()

# Run and extract data

mdl.analyse_and_extract(software='abaqus', fields={'U': 'all', 'S': 'all'})

# Plot displacements

rhino.plot_data(mdl, step='step_loads', field='U', component='magnitude', radius=0.1, scale=10)
rhino.plot_data(mdl, step='step_loads', field='U', component='U1', radius=0.1)
rhino.plot_data(mdl, step='step_loads', field='U', component='U3', radius=0.1)

# Plot stress

rhino.plot_data(mdl, step='step_loads', field='S', component='mises', iptype='max', radius=0.1)