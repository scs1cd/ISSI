### Repo containing solutions for ISSI.

#### Setup
This uses the thermal_history code from https://github.com/sam-greenwood/thermal_history

Example solutions discussed prior to the in-person meeting are found in /example_solutions/. Each solution contains the script to create the results and required parameters file.
If thermal_history is not in your $PYTHONPATH variable (see README from the thermal_history github repo about setting this) then you may need to add:

```python
import sys
sys.path.append('/full/path/to/directory/containg_thermal_history')
```
before thermal_history is imported. Windows users beware, you'll need to escape each backslash and watch out for special unicode characters if copy and pasting from the file browser, you may need to type it out manually.

Many of the scripts make use of relative filepaths in order to reference output files so it is advised to not move any scipts unless you're happy to fix any path issues.

#### Main solutions

Solutions produced during the in-person meeting are in the meeting_solutions folder. In this folder are folders for each of the 3 differently sized bodies containing a script (run.py) to produce all of the results for that body. In the run.py scripts is a toggle to switch off the thermally stable layer. If the stable layer is not included, output files have _adiabatic appended to them. Output files are not stored here on the github repo due to their size and are hosted on the ISSI cloud storage service if you are unable to run the code here.

#### Plots

The plots folder containes jupyter notebooks to produce a range of figures.

Note, for using jupyter notebook's, you may have to install jupyter first and make the thermal_history conda environment visible to jupyter. From within the correct conda environment:
```
conda install jupyter ipykernel
python -m ipykernel install --user --name thermal_history --display-name "Python (thermal_history)"
```
This should add the thermal_history environent to the list of available kernels from within jupyter.


#### Useful scripts

An aptly named folder called useful_scripts contains ... some useful scripts. `eos_setup_model.py` sets up self-consistent model parameters using Tilio's EOS and is used by the code in `meeting_solutions`. `rivoldini_eos.py` is a simple python script that can be run to print out all quantities calculated by Tilio's EOS code (specify P/T/S conditions at the top of the file). Finally, for those less interested in using python, `write_txt_files.py` takes one of the .pik output files and writes some of the more commonly needed variables to txt files. Use by calling the script from the command line, giving the .pik file as input (e.g. `python write_txt_files.py example.pik`)