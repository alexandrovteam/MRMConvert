# MRMConvert: a workflow for generating regular LC-MS data from the ones acquired in MRM mode.

MRMConvert is created to increase reusability of existing tools for LC-MS data analysis, at the same time, preserving the exceptional quantification features of MRM instruments.

The workflow is being developed by [Alexandrov Team](http://www.embl.de/research/units/scb/alexandrov/index.html) at EMBL Heidelberg ([contact information](http://www.embl.de/research/units/scb/alexandrov/contact/index.html)).

Developer: Ivan Protsyuk

Principal investigator: Theodore Alexandrov

## Description

For each reaction in an MRM experiment, the original data contains the m/z value of a precursor ion and the sequence of m/z-intensity pairs, corresponding to the m/z value of a fragment being monitored and its intensity in a particular scan. The conversion procedure, implemented in the workflow, considers every reaction and constructs an ion chromatogram for the precursor ion using intensities of the fragment ion. All reactions from a single MRM experiment are processed this way and saved into a single mzML file. The algorithm is implemented as a KNIME workflow and can be [downloaded](https://github.com/iprotsyuk/srmconvert/blob/master/MRM_Conversion.knwf) from this repository. The workflow was tested on data acquired with Thermo Fischer Triple Quadrupole instrument. Unexpected issues may arise when using it with data from other instruments.

The main functional part of the workflow is encapsulated in a single node `Convert MRM to MS1`. In its configuration dialog, you can find the `Precursor count` parameter, which should be set according to your MRM data acquisition settings. By default, it is set to `126` meaning that the conversion procedure will split the sequence of MRM scans into groups of 126 scans each and produce one MS1 spectrum for every group. These spectra will be merged into an LC-MS data file in mzML format.

## System requirements

Only 64-bit operating systems are supported; MS Windows, Linux or Apple OS X. A workstation should provide a level of performance sufficient to run KNIME Analytics plaform and Python interpreter.

Note that the workflow makes use of multiple CPU cores to parallelize the conversion procedure.

## Installation

In order to run the workflow, you will need to have KNIME Analytics platform and Python 2.7 interpreter installed.

Find the installation instructions in the [Optimus worfklow repository](https://github.com/MolecularCartography/Optimus#installation), which also runs within KNIME environment.

## License

The content of this project is licensed under the Apache 2.0 licence, see LICENSE.md.
