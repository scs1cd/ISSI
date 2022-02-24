### Repo containing solutions for ISSI.

This uses the thermal_history code from https://github.com/sam-greenwood/thermal_history

Example solutions are found in /example_solutions/. Each solution contains the script to create the results and required parameters file.
If thermal_history is not in your $PYTHONPATH variable (see README from the thermal_history github repo about setting this) then you may need to add:

```python
import sys
sys.path.append('/full/path/to/directory/containg_thermal_history')
```
before thermal_history is imported. Windows users beware, you'll need to escape each backslash (e.g. C:\\user\\folder) and watch out for special unicode characters if copy and pasting from the file browser, you may need to type it out manually.
