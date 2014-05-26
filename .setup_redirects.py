#! /usr/bin/env python

# This Python script is for setting up all of the meta refresh redirects required for the relax website.

# The list of redirects to build.  The first element is the old page, the second is the new page.
redirects = [
        ['api/3.1/lib.dispersion.B14-module.html', 'api/3.2/lib.dispersion.B14-module.html'],
        ['linux_devel.html', ''],
        ['manual/Citations.html', 'manual/Preface_citing_relax.html'],
        ['manual/Consistency_testing_script_mode_relaxation_data_lo.html', 'manual/Consistency_testing_script_mode_relaxation_data_loading.html'],
        ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interactio.html', 'manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'],
        ['manual/d_Auvergne_protocol_GUI_mode_relaxation_interaction.html', 'manual/d_Auvergne_protocol_GUI_mode_relaxation_interactions.html'],
        ['manual/relax.html', 'manual/index.html'],
        ['osx_devel.html', ''],
        ['scripts/code_validator', 'manual/Coding_conventions.html'],
]

# Loop over all redirects, automatically creating the webpage.
for old, new in redirects:
    # Open the old file for writing.
    file = open(old, 'w')

    # Add the contents.
    file.write("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Transitional//EN\">\n")
    file.write("<HTML>\n")
    file.write("<HEAD>\n")
    file.write("    <meta http-equiv=\"refresh\" content=\"0; url=http://www.nmr-relax.com/%s\">\n" % new)
    file.write("</HEAD>\n")
    file.write("</HTML>\n")
