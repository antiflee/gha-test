import os
import yaml
from pathlib import Path

# Ensure "configs" directory exists
configs_path = Path('configs')
configs_path.mkdir(exist_ok=True)

# Prepare the output config.yaml file
output_config = {
    'rules': []
}

# Process all the YAML files in the "anomaly-rules" folder
anomaly_rules_path = Path('anomaly-rules')
for rule_file in anomaly_rules_path.glob('*.yaml'):
    with open(rule_file, 'r') as file:
        data = yaml.safe_load(file)
        
        # Extract the rule information
        for group in data['groups']:
            for rule in group['rules']:
                alert = rule['alert']
                expr = rule['expr']

                # Add the extracted values to the output data structure
                output_data['rules'].append({'alert': alert, 'expr': expr})

# Write the output config to "configs/config.yaml"
with open(configs_path / 'config.yaml', 'w') as output_file:
    yaml.dump(output_config, output_file, default_flow_style=False)