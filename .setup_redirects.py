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
    ['manual/calc.html', '%s/manual/minimise_calculate.html'%url],
    ['manual/grid_search.html', '%s/manual/minimise_grid_search.html'%url],
    ['manual/minimise.html', '%s/manual/minimise_execute.html'%url],
    ['osx_devel.html', '%s/'%url],
    ['scripts/code_validator', '%s/manual/Coding_conventions.html'%url],
    ['wiki/index.html', '%s/'%url_wiki],
]

# User function renamings.
redirects += [
    ['manual/relax_disp_cpmg_frq.html', '%s/manual/relax_disp_cpmg_setup.html'%url],
    ['manual/relax_disp_set_grid_r20_from_min_r2eff.html', '%s/manual/relax_disp_r20_from_min_r2eff.html'%url],
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
