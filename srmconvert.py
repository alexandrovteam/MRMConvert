# Copyright (c) 2016 Ivan Protsyuk <iprotsyuk@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
# You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and limitations under the License.

import pyopenms as ms


def convertsrm2ms1(srm_file, precursor_count, output_file):
    source_experiment = ms.MSExperiment()
    fh = ms.FileHandler()
    fh.loadExperiment(srm_file, source_experiment)

    dst_experiment = ms.MSExperiment()

    current_reaction_number = 0
    result_peaks = ([], [])
    for idx, spec in enumerate(source_experiment):
        if spec.getMSLevel() == 2:
            if current_reaction_number >= precursor_count:
                result_spectrum = ms.MSSpectrum()
                result_spectrum.setRT(source_experiment[idx - 1].getRT())
                result_spectrum.set_peaks(result_peaks)
                result_spectrum.setMSLevel(1)
                dst_experiment.addSpectrum(result_spectrum)

                current_reaction_number = 0
                result_peaks = ([], [])

            result_peaks[0].append(spec.getPrecursors()[0].getMZ())
            ms2_peaks_intensities = spec.get_peaks()[1]
            result_peaks[1].append(ms2_peaks_intensities[0] if ms2_peaks_intensities.size > 0 else 0.0)
            current_reaction_number += 1

    fh.storeExperiment(output_file, dst_experiment)
