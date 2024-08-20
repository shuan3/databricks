#%python
import json
notebook_widgets=dbutils.notebook.entry.getCurrentBindings()
sample_inputs={key:notebook_widgets[key] for key in notebook_widgets}
inputs=sample_inputs.pop("inputs",{})
if inputs:
    sample_inputs=sample_inputs | json.load(inputs)
print(f"Processed notebook params \n {sample_inputs}")

if sample_inputs['feed']=='reference':
    print(f'Processing {feed}')
    main.run_ref_feed(**sample_inputs)
elif sample_inputs['feed']=='package':
    main.run_feed(**sample_inputs)