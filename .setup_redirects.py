#! /usr/bin/env python

# This Python script is for setting up all of the meta refresh redirects required for the relax website.

# Some base URLs.
url = 'http://www.nmr-relax.com'
url_wiki = 'http://wiki.nmr-relax.com/'

# The list of redirects to build.  The first element is the old page which will be turned into a redirect, the second is the new page the redirect points to.
redirects = [
    ['api/2.1/toc-test_suite.unit_tests._maths_fns.Test_rotation_matrix-module.html', '%s/api/2.1/toc-test_suite.unit_tests._maths_fns.test_rotation_matrix-module.html'%url],
    ['api/3.1/lib.dispersion.B14-module.html', '%s/api/3.2/lib.dispersion.b14-module.html'%url],
    ['linux_devel.html', '%s/'%url],
    ['manual/Citations.html', '%s/manual/Preface_citing_relax.html'%url],
    ['manual/Consistency_testing_script_mode_relaxation_data_lo.html', '%s/manual/Consistency_testing_script_mode_relaxation_data_loading.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interactio.html', '%s/manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interaction.html', '%s/manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'%url],
    ['manual/relax.html', '%s/manual/index.html'%url],
    ['osx_devel.html', '%s/'%url],
    ['scripts/code_validator', '%s/manual/Coding_conventions.html'%url],
    ['wiki/index.html', '%s/'%url_wiki],
]

# User function renamings.
redirects += [
    ['manual/calc.html', '%s/manual/minimise_calculate.html'%url],
    ['manual/dipole_pair_define.html', '%s/manual/interatom_define.html'%url],
    ['manual/dipole_pair_read_dist.html', '%s/manual/interatom_read_dist.html'%url],
    ['manual/dipole_pair_set_dist.html', '%s/manual/interatom_set_dist.html'%url],
    ['manual/dipole_pair_unit_vectors.html', '%s/manual/interatom_unit_vectors.html'%url],
    ['manual/exp_info_software_select.html', '%s/manual/bmrb_software_select.html'%url],
    ['manual/frame_order_cone_pdb.html', '%s/manual/frame_order_pdb_model.html'%url],
    ['manual/frq_set.html', '%s/manual/spectrometer_frequency.html'%url],
    ['manual/grid_search.html', '%s/manual/minimise_grid_search.html'%url],
    ['manual/interatomic_copy.html', '%s/manual/interatom_copy.html'%url],
    ['manual/interatomic_create.html', '%s/manual/interatom_define.html'%url],
    ['manual/minimise.html', '%s/manual/minimise_execute.html'%url],
    ['manual/molmol_macro_exec.html', '%s/manual/molmol_macro_run.html'%url],
    ['manual/molmol_write.html', '%s/manual/molmol_macro_write.html'%url],
    ['manual/n_state_model_set_domain.html', '%s/manual/align_tensor_set_domain.html'%url],
    ['manual/n_state_model_set_type.html', '%s/manual/align_tensor_reduction.html'%url],
    ['manual/noe_error.html', '%s/manual/spectrum_error_analysis.html'%url],
    ['manual/noe_read.html', '%s/manual/spectrum_read_intensities.html'%url],
    ['manual/pcs_centre.html', '%s/manual/paramag_centre.html'%url],
    ['manual/pdb.html', '%s/manual/structure_read_pdb.html'%url],
    ['manual/pdb_read.html', '%s/manual/structure_read_pdb.html'%url],
    ['manual/pdb_vectors.html', '%s/manual/structure_vectors.html'%url],
    ['manual/pdc_read.html', '%s/manual/bruker_read.html'%url],
    ['manual/pipe_list.html', '%s/manual/pipe_display.html'%url],
    ['manual/pymol_cmd.html', '%s/manual/pymol_command.html'%url],
    ['manual/pymol_macro_create.html', '%s/manual/pymol_macro_write.html'%url],
    ['manual/pymol_macro_exec.html', '%s/manual/pymol_macro_run.html'%url],
    ['manual/pymol_write.html', '%s/manual/pymol_macro_write.html'%url],
    ['manual/relax_data_frq.html', '%s/manual/spectrometer_frequency.html'%url],
    ['manual/relax_disp_cpmg_frq.html', '%s/manual/relax_disp_cpmg_setup.html'%url],
    ['manual/relax_disp_set_grid_r20_from_min_r2eff.html', '%s/manual/relax_disp_r20_from_min_r2eff.html'%url],
    ['manual/relax_fit_mean_and_error.html', '%s/manual/spectrum_error_analysis.html'%url],
    ['manual/relax_fit_read.html', '%s/manual/spectrum_read_intensities.html'%url],
    ['manual/structure_vectors.html', '%s/manual/interatom_unit_vectors.html'%url],
    ['manual/temperature.html', '%s/manual/spectrometer_temperature.html'%url]
]

# Loop over all redirects, automatically creating the webpage.
for old, new in redirects:
    # Open the old file for writing.
    file = open(old, 'w')

    # Add the contents.
    file.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">\n")
    file.write("<HTML>\n")
    file.write("<HEAD>\n")
    file.write("    <meta http-equiv=\"refresh\" content=\"0; url=%s\">\n" % new)
    file.write("</HEAD>\n")
    file.write("</HTML>\n")
