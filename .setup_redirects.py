#! /usr/bin/env python

# This Python script is for setting up all of the meta refresh redirects required for the relax website.

# Some base URLs.
url = 'http://www.nmr-relax.com'
url_wiki = 'http://wiki.nmr-relax.com/'

# Initialise the list of redirects to build.  The first element is the old page which will be turned into a redirect, the second is the new page the redirect points to.
redirects = []

# The main page redirects.
redirects += [
    ['linux_devel.html', '%s/'%url],
    ['osx_devel.html', '%s/'%url],
    ['scripts/code_validator', '%s/manual/Coding_conventions.html'%url],
    ['wiki/index.html', '%s/'%url_wiki]
]

# The API documentation redirects.
redirects += [
    ['api/2.1/toc-test_suite.unit_tests._maths_fns.Test_rotation_matrix-module.html', '%s/api/2.1/toc-test_suite.unit_tests._maths_fns.test_rotation_matrix-module.html'%url],
    ['api/3.1/lib.dispersion.B14-module.html', '%s/api/3.2/lib.dispersion.b14-module.html'%url]
]

# The HTML manual redirects.
redirects += [
    ['manual/Alphabetical_listing_user_functions.html', '%s/manual/Alphabetical_listing_of_user_functions.html'%url],
    ['manual/Becoming_committer.html', '%s/manual/Becoming_a_committer.html'%url],
    ['manual/Calculating_NOE.html', '%s/manual/Calculating_the_NOE.html'%url],
    ['manual/Citations.html', '%s/manual/Preface_citing_relax.html'%url],
    ['manual/clustered_relaxation_dispersion_analysis.html', '%s/manual/The_clustered_relaxation_dispersion_analysis.html'%url],
    ['manual/Comparison_dispersion_analysis_software.html', '%s/manual/Comparison_of_dispersion_analysis_software.html'%url],
    ['manual/Consistency_testing_script_mode_relaxation_data_lo.html', '%s/manual/Consistency_testing_script_mode_relaxation_data_loading.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_loading_data.html', '%s/manual/d_Auvergne_protocol_GUI_mode_loading_the_data.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interactio.html', '%s/manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interaction.html', '%s/manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'%url],
    ['manual/d_Auvergne_protocol_GUI_mode_setting_up_spin.html', '%s/manual/d_Auvergne_protocol_GUI_mode_setting_up_the_spin_systems.html'%url],
    ['manual/diffusion_seeded_paradigm.html', '%s/manual/The_diffusion_seeded_paradigm.html'%url],
    ['manual/Dispersion_script_mode_loading_data.html', '%s/manual/Dispersion_script_mode_loading_the_data.html'%url],
    ['manual/do_dispersion_features_yet_be_implemented.html', '%s/manual/To_do_dispersion_features_yet_to_be_implemented.html'%url],
    ['manual/DPL94_2_site_fast_exchange_R1_model.html', '%s/manual/The_DPL94_2_site_fast_exchange_R1_rho_model.html'%url],
    ['manual/full_B14_2_site_CPMG_model.html', '%s/manual/The_full_B14_2_site_CPMG_model.html'%url],
    ['manual/full_CR72_2_site_CPMG_model.html', '%s/manual/The_full_CR72_2_site_CPMG_model.html'%url],
    ['manual/full_NS_2_site_3D_CPMG_model.html', '%s/manual/The_full_NS_2_site_3D_CPMG_model.html'%url],
    ['manual/full_NS_2_site_star_CPMG_model.html', '%s/manual/The_full_NS_2_site_star_CPMG_model.html'%url],
    ['manual/GUI.html', '%s/manual/The_GUI.html'%url],
    ['manual/IT99_2_site_CPMG_model.html', '%s/manual/The_IT99_2_site_CPMG_model.html'%url],
    ['manual/J_w_mapping_script_mode_sample_script.html', '%s/manual/J_w_mapping_script_mode_the_sample_script.html'%url],
    ['manual/Keeping_branch_up_date_using_svnmerge_py.html', '%s/manual/Keeping_the_branch_up_to_date_using_svnmerge_py.html'%url],
    ['manual/LM63_2_site_fast_exchange_CPMG_model.html', '%s/manual/The_LM63_2_site_fast_exchange_CPMG_model.html'%url],
    ['manual/LM63_3_site_fast_exchange_CPMG_model.html', '%s/manual/The_LM63_3_site_fast_exchange_CPMG_model.html'%url],
    ['manual/M61_2_site_fast_exchange_R1_model.html', '%s/manual/The_M61_2_site_fast_exchange_R1_rho_model.html'%url],
    ['manual/methodology_Mandel_et_al_1995.html', '%s/manual/The_methodology_of_Mandel_et_al_1995.html'%url],
    ['manual/MMQ_CR72_model.html', '%s/manual/The_MMQ_CR72_model.html'%url],
    ['manual/model_free_models.html', '%s/manual/The_model_free_models.html'%url],
    ['manual/MP05_2_site_exchange_R1_model.html', '%s/manual/The_MP05_2_site_exchange_R1_rho_model.html'%url],
    ['manual/new_protocol_in_GUI.html', '%s/manual/The_new_protocol_in_the_GUI.html'%url],
    ['manual/node149.html', '%s/manual/Coding_conventions.html'%url],
    ['manual/NS_2_site_R1_model.html', '%s/manual/The_NS_2_site_R1_rho_model.html'%url],
    ['manual/NS_3_site_linear_R1_model.html', '%s/manual/The_NS_MMQ_3_site_linear_model.html'%url],
    ['manual/NS_3_site_R1_model.html', '%s/manual/The_NS_3_site_R1_rho_model.html'%url],
    ['manual/NS_MMQ_2_site_model.html', '%s/manual/The_NS_MMQ_2_site_model.html'%url],
    ['manual/NS_MMQ_3_site_linear_model.html', '%s/manual/NS_MMQ_3_site_linear_model.html'%url],
    ['manual/NS_MMQ_3_site_model.html', '%s/manual/The_NS_MMQ_3_site_model.html'%url],
    ['manual/prompt.html', '%s/manual/The_prompt.html'%url],
    ['manual/R2eff_model.html', '%s/manual/The_R2eff_model.html'%url],
    ['manual/reduced_B14_2_site_CPMG_model.html', '%s/manual/The_reduced_B14_2_site_CPMG_model.html'%url],
    ['manual/reduced_CR72_2_site_CPMG_model.html', '%s/manual/The_reduced_NS_2_site_star_CPMG_model.html'%url],
    ['manual/reduced_NS_2_site_3D_CPMG_model.html', '%s/manual/The_reduced_NS_2_site_3D_CPMG_model.html'%url],
    ['manual/reduced_NS_2_site_star_CPMG_model.html', '%s/manual/The_reduced_NS_2_site_star_CPMG_model.html'%url],
    ['manual/relax.html', '%s/manual/index.html'%url],
    ['manual/relax_data_model.html', '%s/manual/The_relax_data_model.html'%url],
    ['manual/relax_distribution_archives.html', '%s/manual/The_relax_distribution_archives.html'%url],
    ['manual/relax_user_manual.html', '%s/manual/index.html'%url],
    ['manual/Ri_prime_theta_Hessians.html', '%s/manual/The_Ri_theta_Hessians.html'%url],
    ['manual/TAP03_2_site_exchange_R1_model.html', '%s/manual/The_TAP03_2_site_exchange_R1_rho_model.html'%url],
    ['manual/Temperature_control_calibration.html', '%s/manual/Temperature_control_and_calibration.html'%url],
    ['manual/TP02_2_site_exchange_R1_model.html', '%s/manual/The_TP02_2_site_exchange_R1_rho_model.html'%url],
    ['manual/TSMFK01_2_site_CPMG_model.html', '%s/manual/The_TSMFK01_2_site_CPMG_model.html'%url],
    ['manual/Tutorial_adding_relaxation_dispersion_models.html', '%s/manual/Tutorial_for_adding_relaxation_dispersion_models.html'%url],
]

# HTML manual user function renamings.
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
    ['manual/init_data.html', '%s/manual/reset.html'%url],
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
