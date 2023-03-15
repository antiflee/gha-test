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
        rule_data = yaml.safe_load(file)
        
        # Extract the rule information
        for group in rule_data.get('groups', []):
            group_name = group.get('name')
            for rule in group.get('rules', []):
                rule_name = rule.get('alert')
                rule_expr = rule.get('expr')
                rule_summary = rule.get('annotations', {}).get('summary')

                # Add the extracted information to the output config
                output_config['rules'].append({
                    'group_name': group_name,
                    'rule_name': rule_name,
                    'rule_expr': rule_expr,
                    'rule_summary': rule_summary
                })

# Write the output config to "configs/config.yaml"
with open(configs_path / 'config.yaml', 'w') as output_file:
    yaml.dump(output_config, output_file, default_flow_style=False)