### Repo containing solutions for ISSI.

This uses the thermal_history code from https://github.com/sam-greenwood/thermal_history

Example solutions are found in /example_solutions/. Each solution contains the script to create the results and required parameters file.
If thermal_history is not in your $PYTHONPATH variable (see README from the thermal_history github repo about setting this) then you may need to add:

```python
import sys
sys.path.append('/full/path/to/directory/containg_thermal_history')
```
before thermal_history is imported. Windows users beware, you'll need to escape each backslash and watch out for special unicode characters if copy and pasting from the file browser, you may need to type it out manually.


Solutions produced during the in-person meeting are in the meeting_solutions folder.

Note, for using jupyter notebook's, you may have to install jupyter first and make the thermal_history conda environment visible to jupyter. From within the correct conda environment:
```
conda install jupyter ipykernel
python -m ipykernel install --user --name thermal_history --display-name "Python (thermal_history)"
```
This should add the thermal_history environent to the list of available kernels from within jupyter.
